import json
import pathlib
from datetime import datetime

import matplotlib.pyplot as plt


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()


def plot(filename):
    filename = pathlib.Path(filename)
    assert filename.is_file(), f"{filename} not found."

    with open(filename) as f:
        content = json.load(f)

    data = content["data"]
    data = {datetime.fromisoformat(key): value for key, value in data.items()}

    plt.plot(list(data.keys()), list(data.values()), "-", label=content["repository"])
    plt.legend()
    plt.grid()
