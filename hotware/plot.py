import argparse
import json
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import requests


def plot(filename):
    assert num_data > 1

    args = parse_args()

    url = f"https://api.github.com/repos/{args.repo}/stargazers"
    # Send those headers to get starred_at
    headers = {"Accept": "application/vnd.github.v3.star+json"}

    if args.token:
        headers["Authorization"] = f"token {args.token}"

    # get number of stars
    url0 = f"https://api.github.com/repos/{args.repo}"
    r = requests.get(url0, headers=headers)
    assert r.ok
    total_num_stars = r.json()["stargazers_count"]

    # https://stackoverflow.com/a/969324/353337
    date_fmt = "%Y-%m-%dT%H:%M:%S%z"

    # get times of first and last star
    r = requests.get(url, headers=headers, params={"page": 1, "per_page": 1})
    assert r.ok
    time_first = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

    r = requests.get(
        url, headers=headers, params={"page": total_num_stars, "per_page": 1}
    )
    assert r.ok
    time_last = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

    times = [time_first, time_last]
    stars = [0, total_num_stars]

    for _ in range(num_data - 1):
        # find longest interval
        max_length = timedelta(0)
        k = -1
        for i, (previous, current) in enumerate(zip(times, times[1:])):
            if current - previous > max_length:
                k = i
                max_length = current - previous
        assert k >= 0

        # call at midpoint of the interval k
        mp = (stars[k] + stars[k + 1]) // 2

        r = requests.get(url, headers=headers, params={"page": mp, "per_page": 1})
        assert r.ok
        time = datetime.strptime(r.json()[0]["starred_at"], date_fmt)

        # sort this into the arrays
        times.insert(k + 1, time)
        stars.insert(k + 1, mp)

    d = {
        "title": "GitHub stars",
        "repo": args.repo,
        "data": dict(zip([t.isoformat() for t in times], stars)),
    }
    with open("{}_{}.json".format(*args.repo.split("/")), "w") as f:
        json.dump(d, f, indent=2)

    exit(1)

    plt.plot(times, stars, "-o")
    plt.grid()
    plt.show()

    return


def parse_args():
    parser = argparse.ArgumentParser(description="GitHub star history")
    parser.add_argument(
        "repo", type=str, help="GitHub repository",
    )
    parser.add_argument(
        "--token", "-t", type=str, help="GitHub access token (for more requests)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    _main()
