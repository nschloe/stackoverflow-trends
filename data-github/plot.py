import json
import pathlib

import matplotlib as mpl
import matplotlib.pyplot as plt

import hotware


# mpl uses category10 by default, we use cat20,
# <https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category20>,
# which basically adds one pale color version of each color in cat10.
# Change the order such that the first 10 are cat10.
mpl.rcParams["axes.prop_cycle"] = mpl.cycler(
    color=[
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
        # pale variants:
        "#aec7e8",
        "#ffbb78",
        "#98df8a",
        "#ff9896",
        "#c5b0d5",
        "#c49c94",
        "#f7b6d2",
        "#c7c7c7",
        "#dbdb8d",
        "#9edae5",
    ]
)


this_dir = pathlib.Path(__file__).resolve().parent
with open(this_dir / "groups.json") as f:
    data = json.load(f)


# https://stackoverflow.com/a/3382369/353337
def _argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


for group_name, group in data.items():
    # sort them such that the largest at the last time step gets plotted first
    last_vals = []
    for repo in group:
        filename = this_dir / "data" / (repo.replace("/", "_") + ".json")
        with open(filename) as f:
            content = json.load(f)
        last_vals.append(list(content["data"].values())[-1])
    group = [group[i] for i in _argsort(last_vals)[::-1]]

    for repo in group:
        filename = this_dir / "data" / (repo.replace("/", "_") + ".json")
        # hotware.plot(filename, "update")
        hotware.plot(filename, "cumulative")
        # plt.title(group_name)
    plt.show()
    plt.close()
