import json
import pathlib
from datetime import datetime

import matplotlib.pyplot as plt

import cleanplotlib as cpl


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()


def plot(filenames):
    times = []
    values = []
    labels = []
    for filename in filenames:
        filename = pathlib.Path(filename)
        assert filename.is_file(), f"{filename} not found."

        with open(filename) as f:
            content = json.load(f)

        data = content["data"]
        data = {datetime.fromisoformat(key): value for key, value in data.items()}

        times.append(list(data.keys()))
        values.append(list(data.values()))
        if "repository" in content:
            labels.append(content["repository"])
        else:
            labels.append(content["tag"])

    cpl.multiplot(times, values, labels)


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


def plot_per_day(filenames):
    times = []
    values = []
    labels = []
    for filename in filenames:
        filename = pathlib.Path(filename)
        assert filename.is_file(), f"{filename} not found."

        with open(filename) as f:
            content = json.load(f)

        data = content["data"]
        data = {datetime.fromisoformat(key): value for key, value in data.items()}

        t = list(data.keys())
        v = list(data.values())
        times.append(_get_middle_times(t))
        values.append(_get_avg_per_day(t, v))

        if "repository" in content:
            labels.append(content["repository"])
        else:
            labels.append(content["tag"])

    cpl.multiplot(times, values, labels)
