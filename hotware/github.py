import json
import pathlib
import urllib
from datetime import datetime, timedelta, timezone

import requests


def update_stars(
    filename,
    max_interval_length,
    repo=None,
    token=None,
    title="GitHub stars",
    creator=None,
    license=None,
):
    filename = pathlib.Path(filename)
    if filename.is_file():
        with open(filename) as f:
            content = json.load(f)

        if repo is not None:
            assert content["repository"] == repo
        if title is not None:
            assert content["title"] == title
        if creator is not None:
            assert content["creator"] == creator
        if license is not None:
            assert content["license"] == license

        data = content["data"]
    else:
        data = {}
        assert repo is not None

    data = {datetime.fromisoformat(key): value for key, value in data.items()}

    data = update_github_star_data(
        data, repo, max_interval_length=max_interval_length, token=token,
    )

    d = {}
    if title is not None:
        d["title"] = title
    d["repository"] = repo
    if creator is not None:
        d["creator"] = creator
    if license is not None:
        d["license"] = license

    d["data"] = dict(zip([t.isoformat() for t in data.keys()], data.values()))

    with open(filename, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

    return


def update_github_star_data(
    data, repo, max_interval_length=timedelta(0), max_num_data_points=None, token=None
):
    # argument validation
    assert max_interval_length > timedelta(0) or max_num_data_points is not None
    if max_num_data_points is not None:
        assert max_num_data_points > 1

    url = f"https://api.github.com/repos/{repo}/stargazers"
    # Send those headers to get starred_at
    headers = {"Accept": "application/vnd.github.v3.star+json"}

    if token is not None:
        headers["Authorization"] = f"token {token}"

    # Get last page. It'd be lovely if we could always get all stargazers (plus times),
    # but GitHubs limits is 40k right now (Apr 2020).
    r = requests.get(
        f"https://api.github.com/repos/{repo}/stargazers",
        headers=headers,
        params={"per_page": 1},
    )
    assert r.ok, f"{r.url}, status code {r.status_code}"
    #
    last_page_url, info = r.headers["link"].split(",")[1].split(";")
    assert info.strip() == 'rel="last"'
    last_page = int(
        urllib.parse.parse_qs(urllib.parse.urlsplit(last_page_url.strip()[1:-1]).query)[
            "page"
        ][0]
    )

    # https://stackoverflow.com/a/969324/353337
    date_fmt = "%Y-%m-%dT%H:%M:%S%z"

    # get times of first and last paged star
    r = requests.get(url, headers=headers, params={"page": 1, "per_page": 1})
    assert r.ok, f"{r.url}, status code {r.status_code}"
    time_first = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

    r = requests.get(url, headers=headers, params={"page": last_page, "per_page": 1})
    assert r.ok, f"{r.url}, status code {r.status_code}"
    time_last = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

    times = list(data.keys())
    stars = list(data.values())

    if len(data) == 0:
        times = [time_first, time_last]
        stars = [1, last_page]
        extra_times = []
        extra_stars = []
    else:
        assert time_first in times
        assert time_last in times

        # separate the data that can be retrieved via page bisection and the extra data
        k0 = times.index(time_first)
        assert k0 == 0
        k1 = times.index(time_last)
        extra_times = times[k1 + 1 :]
        extra_stars = stars[k1 + 1 :]
        times = times[: k1 + 1]
        stars = stars[: k1 + 1]

    num_data_points = len(times) + len(extra_times)
    while True:
        # find longest interval
        max_length = timedelta(0)
        k = -1
        for i, (previous, current) in enumerate(zip(times, times[1:])):
            if current - previous > max_length:
                k = i
                max_length = current - previous
        assert k >= 0

        if max_length < max_interval_length:
            break
        if max_num_data_points is not None and num_data_points >= max_num_data_points:
            break

        # call at midpoint of the interval k
        mp = (stars[k] + stars[k + 1]) // 2

        r = requests.get(url, headers=headers, params={"page": mp, "per_page": 1})
        assert r.ok
        time = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

        # sort this into the arrays
        times.insert(k + 1, time)
        stars.insert(k + 1, mp)

        num_data_points += 1

    # re-append extra data
    times += extra_times
    stars += extra_stars

    # get number of stars right now
    r = requests.get(f"https://api.github.com/repos/{repo}", headers=headers)
    assert r.ok, f"{r.url}, status code {r.status_code}"
    now_num_stars = r.json()["stargazers_count"]
    now = datetime.now(timezone.utc)
    now = now.replace(microsecond=0)

    if now - times[-1] > max_interval_length:
        times.append(now)
        stars.append(now_num_stars)

    return dict(zip(times, stars))
