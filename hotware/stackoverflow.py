import json
import os
from datetime import datetime

import requests

# tags = [item for lst in groups.values() for item in lst]
# tags += [None]

groups["all"] = [None]

now = datetime.utcnow()
epoch = datetime(1970, 1, 1)


def update(filename, fromdate, todate):
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

    exit(1)

    data = response.json()
    lst.append([fromdate.isoformat(), todate.isoformat(), data["total"]])

    p = "all" if tag is None else tag
    print("{:<16}: {:<6}  ({} -- {})".format(p, lst[-1][2], lst[-1][0], lst[-1][1]))

    with open(filename, "w") as f:
        json.dump(lst, f, indent=2)
    return


for key, tags in groups.items():
    print(key)
    for tag in tags:
        filename = "none.json" if tag is None else f"{tag}.json"
        filename = os.path.join(this_dir, "data", filename)

        try:
            with open(filename, "r") as f:
                lst = json.load(f)
        except FileNotFoundError:
            # start from stackoverflow launch, Sep 15, 2008
            lst = []
            fromdate = datetime(2008, 9, 15)
            todate = datetime(2008, 10, 1)
        else:
            fromdate = datetime.fromisoformat(lst[-1][1])
            todate = datetime(
                fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
            )

        while todate < now:
            add_data_to_file(filename, fromdate, todate)
            fromdate = todate
            todate = datetime(
                fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
            )

        # # for sneak peaks
        # now_00 = datetime(now.year, now.month, now.day, 0, 0)
        # add_data_to_file(filename, fromdate, now_00)
    print()
