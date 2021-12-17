from __future__ import annotations

from datetime import datetime

import matplotlib.pyplot as plt
import matplotx


def _merge(a, b):
    return {**a, **b}


plt.style.use(_merge(matplotx.styles.tab20r, matplotx.styles.dufte))


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
