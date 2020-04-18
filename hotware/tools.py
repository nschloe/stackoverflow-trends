import json
import pathlib
from datetime import datetime

import matplotlib.pyplot as plt


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()


def plot(filename, mode):
    filename = pathlib.Path(filename)
    assert filename.is_file(), f"{filename} not found."

    with open(filename) as f:
        content = json.load(f)

    data = content["data"]
    data = {datetime.fromisoformat(key): value for key, value in data.items()}

    times = list(data.keys())
    stars = list(data.values())
    if mode == "cumulative":
        plt.plot(times, stars, "-", label=content["repository"])
        plt.ylabel("num stars")
    else:
        assert mode == "update"

        vals = []
        for k in range(len(times) - 1):
            dt = (times[k + 1] - times[k]).total_seconds() / 3600 / 24 / 30
            vals.append((stars[k + 1] - stars[k]) / dt)
        vals = [0] + vals

        # The first few values are often very large. Don't plot them.
        x = times[3:]
        y = vals[3:]

        plt.step(x, y, "-", label=content["repository"])
        # plt.plot(x, y, "-", label=content["repository"])
        plt.ylabel("avg num stars per 30 days")

    plt.legend()
    plt.grid()
