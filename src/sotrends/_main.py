from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import appdirs
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
        except requests.exceptions.ConnectionError as e:
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
