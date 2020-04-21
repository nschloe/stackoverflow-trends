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
    filenames = [this_dir / "data" / (tag + ".json") for tag in group]

    # hotware.plot(filenames)
    # plt.title("Number of tags on StackOverflow", fontsize=14)

    hotware.plot_per_day(filenames, cut=0.05)
    plt.title("Daily number of questions on StackOverflow", fontsize=14)

    # plt.title("% of all questions that month", fontsize=14)
    plt.show()
    # plt.savefig(
    #     "stackoverflow-" + group_name + ".svg", transparent=True, bbox_inches="tight"
    # )
    plt.close()
