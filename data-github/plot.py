import json
import pathlib

import matplotlib.pyplot as plt

import hotware

plt.rc("font", family="Helvetica World")

this_dir = pathlib.Path(__file__).resolve().parent
with open(this_dir / "groups.json") as f:
    data = json.load(f)


# https://stackoverflow.com/a/3382369/353337
def _argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


for group_name, group in data.items():
    # sort them such that the largest at the last time step gets plotted first and the
    # colors are in a nice order
    last_vals = []
    for repo in group:
        filename = this_dir / "data" / (repo.replace("/", "_") + ".json")
        with open(filename) as f:
            content = json.load(f)
        last_vals.append(list(content["data"].values())[-1])
    group = [group[i] for i in _argsort(last_vals)[::-1]]

    filenames = [
        this_dir / "data" / (repo.replace("/", "_") + ".json") for repo in group
    ]

    hotware.plot(filenames)
    plt.title("Number of GitHub stars", fontsize=14)

    # hotware.plot_per_day(filenames)
    # plt.title("Daily number of GitHub stars", fontsize=14)

    # plt.show()
    plt.savefig("github-" + group_name + ".svg", transparent=True, bbox_inches="tight")
    plt.close()
