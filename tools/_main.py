from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import appdirs
import matplotlib.pyplot as plt
import matplotx
import requests
from rich.progress import Progress


class Cache:
    def __init__(self, repo: str):
        cache_dir = Path(appdirs.user_cache_dir()) / "sotrends"
        cache_dir.mkdir(parents=True, exist_ok=True)

        nrepo = repo.replace("/", "_")
        self.filename = cache_dir / f"{nrepo}.json"

    def read(self) -> dict:
        if not self.filename.is_file():
            return {}
        try:
            with open(self.filename) as f:
                content = json.load(f)
        except Exception:
            return {}
        return {datetime.fromisoformat(key): value for key, value in content.items()}

    def write(self, data: dict[datetime, int]):
        with open(self.filename, "w") as f:
            json.dump(
                {key.isoformat(): value for key, value in data.items()},
                f,
                indent=2,
                ensure_ascii=False,
            )


def fetch_data(tags: list[str] | set[str]):
    out = {}
    with Progress() as progress:
        task1 = progress.add_task("Total", total=len(tags))
        task2 = progress.add_task("Repo")
        for tag in tags:
            progress.update(task2, description=tag)
            cache = Cache(tag)

            data = cache.read()

            data = _update(data, tag, progress_task=(progress, task2))
            cache.write(data)

            out[tag] = data
            progress.advance(task1)
    return out


def _update(data, tag, progress_task):
    if data:
        fromdate = list(data.keys())[-1]
    else:
        fromdate = datetime(2008, 9, 15)
        data = {fromdate: 0}

    epoch = datetime(1970, 1, 1)
    now = datetime.utcnow()

    # next beginning of the month
    todate = datetime(
        fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
    )

    progress, task = progress_task

    if progress is not None:
        progress.update(
            task, description=tag, total=_diff_month(now, fromdate), completed=0
        )

    while todate < now:
        url = "https://api.stackexchange.com/questions"
        # https://stackoverflow.com/a/22101249/353337
        params = {
            "site": "stackoverflow",
            "fromdate": int((fromdate - epoch).total_seconds()),
            "todate": int((todate - epoch).total_seconds()),
            "filter": "total",
        }
        if tag is not None:
            params["tagged"] = tag

        try:
            response = requests.get(url, params)
        except Exception as e:
            print(e)
            break

        if not response.ok:
            print(response, response.reason)
            break

        res = response.json()
        cumsum = list(data.values())[-1] + res["total"]
        data[todate] = cumsum

        fromdate = todate
        todate = datetime(
            fromdate.year + fromdate.month // 12, (fromdate.month % 12) + 1, 1
        )

        if progress is not None:
            progress.advance(task)

    return data


# https://stackoverflow.com/a/4040338/353337
def _diff_month(d1: datetime, d2: datetime) -> int:
    return (d1.year - d2.year) * 12 + d1.month - d2.month


plt.style.use(matplotx.styles.duftify(matplotx.styles.tab20r))


# https://stackoverflow.com/a/3382369/353337
def _argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def _get_avg_per_day(times, values):
    return [
        (values[k + 1] - values[k])
        / ((times[k + 1] - times[k]).total_seconds() / 3600 / 24)
        for k in range(len(values) - 1)
    ]


def _get_middle_times(lst):
    return [
        datetime.fromtimestamp(
            (datetime.timestamp(lst[k]) + datetime.timestamp(lst[k + 1])) / 2
        )
        for k in range(len(lst) - 1)
    ]


def plot_per_day(
    data: dict[str, dict[datetime, int]], sort: bool = True, cut: float | None = None
):
    # convert to list of tuples to be able to sort
    data = list(data.items())

    if sort:
        # sort them such that the largest at the last time step gets plotted first and
        # the colors are in a nice order
        last_vals = [
            list(vals.values())[-1] - list(vals.values())[-2] for _, vals in data
        ]
        data = [data[i] for i in _argsort(last_vals)[::-1]]

    if cut is not None:
        # cut those files where the latest data is less than cut*max_latest
        last_vals = [
            list(vals.values())[-1] - list(vals.values())[-2] for _, vals in data
        ]

        max_overall = max(last_vals)
        data = [
            (tag, vals)
            for (tag, vals), last_val in zip(data, last_vals)
            if last_val > cut * max_overall
        ]

    times = []
    values = []
    labels = []
    for tag, vals in data:
        t = list(vals.keys())
        v = list(vals.values())
        times.append(_get_middle_times(t))
        values.append(_get_avg_per_day(t, v))
        labels.append(tag)

    # start plotting from the 0 before the first value
    for j, (tm, val) in enumerate(zip(times, values)):
        for i, x in enumerate(val):
            if x > 0:
                k = max(i - 1, 0)
                break
        times[j] = tm[k:]
        values[j] = val[k:]

    n = len(times)
    for k, (time, vals, label) in enumerate(zip(times, values, labels)):
        plt.plot(time, vals, label=label, zorder=n - k)

    matplotx.line_labels()

    return plt
