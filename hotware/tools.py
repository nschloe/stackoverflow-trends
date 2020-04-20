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
        labels.append(content["repository"])

    cpl.multiplot(times, stars, labels)
