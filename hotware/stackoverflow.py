import json
import pathlib
from datetime import datetime

import requests

import cleanplotlib as cpl

# tags = [item for lst in groups.values() for item in lst]
# tags += [None]

# groups["all"] = [None]


def update():

    exit(1)

    data = response.json()
    lst.append([fromdate.isoformat(), todate.isoformat(), data["total"]])

    p = "all" if tag is None else tag
    print("{:<16}: {:<6}  ({} -- {})".format(p, lst[-1][2], lst[-1][0], lst[-1][1]))

    with open(filename, "w") as f:
        json.dump(lst, f, indent=2)
    return


def update_file(
    filename, tag=None, title="StackOverflow tags", creator=None, license=None,
):
    try:
        with open(filename, "r") as f:
            content = json.load(f)
    except FileNotFoundError:
        # start from stackoverflow launch, Sep 15, 2008
        fromdate = datetime(2008, 9, 15)
        content = {
            "title": title,
            "tag": tag,
            "creator": creator,
            "license": license,
            "data": {fromdate.isoformat(): 0},
        }
    else:
        if title is not None:
            assert content["title"] == title
        if tag is not None:
            assert content["tag"] == tag
        if creator is not None:
            assert content["creator"] == creator
        if license is not None:
            assert content["license"] == license

        fromdate = datetime.fromisoformat(list(content["data"].keys())[-1])

    tag = content["tag"]

    epoch = datetime(1970, 1, 1)
    now = datetime.utcnow()

    todate = datetime(
        fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
    )

    has_new_data = False
    while todate < now:
        has_new_data = True
        url = "https://api.stackexchange.com/questions"
        # https://stackoverflow.com/a/22101249/353337
        fromts = int((fromdate - epoch).total_seconds())
        tots = int((todate - epoch).total_seconds())
        params = {
            "site": "stackoverflow",
            "fromdate": fromts,
            "todate": tots,
            "filter": "total",
        }
        if tag is not None:
            params["tagged"] = tag
        response = requests.get(url, params)
        assert response.ok, (response, response.reason)

        data = response.json()
        cumsum = list(content["data"].values())[-1] + data["total"]
        to_iso = todate.isoformat()
        content["data"][to_iso] = cumsum

        p = "all" if tag is None else tag
        from_iso = fromdate.isoformat()
        print("{:<16}: {:<6}  ({} -- {})".format(p, data["total"], from_iso, to_iso))

        fromdate = todate
        todate = datetime(
            fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
        )

    if has_new_data:
        with open(filename, "w") as f:
            json.dump(content, f, indent=2, ensure_ascii=False)


def plot(filenames):
    times = []
    stars = []
    labels = []
    for filename in filenames:
        filename = pathlib.Path(filename)
        assert filename.is_file(), f"{filename} not found."

        with open(filename) as f:
            content = json.load(f)

        data = content["data"]
        data = {datetime.fromisoformat(key): value for key, value in data.items()}

        times.append(list(data.keys()))
        stars.append(list(data.values()))
        labels.append(content["name"])

    cpl.multiplot(times, stars, labels)
