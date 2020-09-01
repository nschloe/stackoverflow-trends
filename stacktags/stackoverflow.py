import json
from datetime import datetime

import requests


def update_file(
    filename,
    tag=None,
    title="StackOverflow tags",
    creator=None,
    license=None,
):
    try:
        with open(filename, "r") as f:
            content = json.load(f)
    except FileNotFoundError:
        # start from stackoverflow launch, Sep 15, 2008
        content = {"title": title, "name": tag}
        if creator is not None:
            content["creator"] = creator
        if license is not None:
            content["license"] = license
        content["data source"] = "StackOverflow API via stacktags"
        content["last updated"] = ""
        fromdate = datetime(2008, 9, 15)
        content["data"] = {fromdate.isoformat(): 0}
    else:
        if title is not None:
            assert content["title"] == title
        if tag is not None:
            assert content["name"] == tag
        if creator is not None:
            assert content["creator"] == creator
        if license is not None:
            assert content["license"] == license

        fromdate = datetime.fromisoformat(list(content["data"].keys())[-1])

    tag = content["name"]

    epoch = datetime(1970, 1, 1)
    now = datetime.utcnow()

    todate = datetime(
        fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
    )

    has_new_data = False
    while todate < now:
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
        try:
            response = requests.get(url, params)
        except requests.exceptions.ConnectionError as e:
            print(e)
            break
        if not response.ok:
            print(response, response.reason)
            break

        data = response.json()
        cumsum = list(content["data"].values())[-1] + data["total"]
        to_iso = todate.isoformat()
        content["data"][to_iso] = cumsum

        has_new_data = True

        p = "all" if tag is None else tag
        from_iso = fromdate.isoformat()
        print("{:<16}: {:<6}  ({} -- {})".format(p, data["total"], from_iso, to_iso))

        fromdate = todate
        todate = datetime(
            fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
        )

    if has_new_data:
        now = datetime.utcnow()
        now = now.replace(microsecond=0)
        content["last updated"] = now.isoformat()
        with open(filename, "w") as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
