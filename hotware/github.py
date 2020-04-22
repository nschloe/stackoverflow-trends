import json
import pathlib
import urllib
from datetime import datetime, timedelta, timezone

import requests


def update_file(
    filename,
    max_interval_length,
    repo=None,
    token=None,
    title="GitHub stars",
    creator=None,
    license=None,
    verbose=False,
):
    filename = pathlib.Path(filename)
    if filename.is_file():
        with open(filename) as f:
            content = json.load(f)

        if repo is not None:
            assert content["name"] == repo
        if title is not None:
            assert content["title"] == title
        if creator is not None:
            assert content["creator"] == creator
        if license is not None:
            assert content["license"] == license

        now = datetime.utcnow()
        if now - datetime.fromisoformat(content["last updated"]) < max_interval_length:
            return

        data = content["data"]
    else:
        data = {}
        assert repo is not None

    data = {datetime.fromisoformat(key): value for key, value in data.items()}

    data = update_github_star_data(
        data,
        repo,
        max_interval_length=max_interval_length,
        token=token,
        verbose=verbose,
    )

    d = {}
    if title is not None:
        d["title"] = title
    d["name"] = repo
    if creator is not None:
        d["creator"] = creator
    if license is not None:
        d["license"] = license

    d["data"] = dict(zip([t.isoformat() for t in data.keys()], data.values()))

    with open(filename, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

    return


def update_github_star_data(
    data,
    repo,
    max_interval_length=timedelta(0),
    max_num_data_points=None,
    token=None,
    verbose=False,
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
        url,
        headers=headers,
        params={"per_page": 1},
    )
    assert r.ok, f"{r.url}, status code {r.status_code}, {r.reason}"
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
    assert r.ok, f"{r.url}, status code {r.status_code}, {r.reason}"
    time_first = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

    r = requests.get(url, headers=headers, params={"page": last_page, "per_page": 1})
    assert r.ok, f"{r.url}, status code {r.status_code}, {r.reason}"
    time_last = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

    times = list(data.keys())
    stars = list(data.values())

    if len(data) == 0:
        times = [time_first, time_last]
        stars = [1, last_page]
        extra_times = []
        extra_stars = []
    else:
        assert time_first == times[0]

        # break off the extra data
        k1 = 0
        for time in times:
            if time_last < time:
                break
            k1 += 1
        extra_times = times[k1:]
        extra_stars = stars[k1:]
        times = times[:k1]
        stars = stars[:k1]

        # append new data if necessary
        if time_last > times[-1]:
            times.append(time_last)
            stars.append(last_page)

    num_data_points = len(times) + len(extra_times)
    while True:
        # find longest interval with stars more than one apart
        max_length = timedelta(0)
        k = -1
        for i in range(len(times) - 1):
            if abs(stars[i + 1] - stars[i]) < 2:
                continue
            length = times[i + 1] - times[i]
            if length > max_length:
                k = i
                max_length = length
        assert k >= 0

        if max_length < max_interval_length:
            break
        if max_num_data_points is not None and num_data_points >= max_num_data_points:
            break

        # call at midpoint of the interval k
        mp = (stars[k] + stars[k + 1]) // 2

        r = requests.get(url, headers=headers, params={"page": mp, "per_page": 1})
        assert r.ok, f"{r.url}, status code {r.status_code}, {r.reason}"
        time = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

        if verbose:
            print(f"{time}: {mp}")

        # sort this into the arrays
        times.insert(k + 1, time)
        stars.insert(k + 1, mp)

        num_data_points += 1

    # re-append extra data
    times += extra_times
    stars += extra_stars

    # check if we can remove some data (especially if we have two equal times)
    new_times = [times[0]]
    new_stars = [stars[0]]
    for k in range(len(times) - 1):
        if times[k + 1] - new_times[-1] > max_interval_length:
            new_times.append(times[k])
            new_stars.append(stars[k])
    new_times.append(times[-1])
    new_stars.append(stars[-1])

    # get number of stars right now
    now = datetime.now(timezone.utc)
    if now - new_times[-1] > max_interval_length:
        r = requests.get(f"https://api.github.com/repos/{repo}", headers=headers)
        assert r.ok, f"{r.url}, status code {r.status_code}, {r.reason}"
        now_num_stars = r.json()["stargazers_count"]
        now = now.replace(microsecond=0)
        new_times.append(now)
        new_stars.append(now_num_stars)

    return dict(zip(new_times, new_stars))
