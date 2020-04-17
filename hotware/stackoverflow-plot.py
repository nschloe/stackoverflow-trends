import json
import os
from datetime import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt

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


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def get_middle_times(lst):
    return [
        datetime.fromtimestamp(
            (
                datetime.timestamp(datetime.fromisoformat(item[0]))
                + datetime.timestamp(datetime.fromisoformat(item[1]))
            )
            / 2
        )
        for item in lst
    ]


def get_num_questions_per_day(lst):
    return [
        item[2]
        / (
            (
                datetime.fromisoformat(item[1]) - datetime.fromisoformat(item[0])
            ).total_seconds()
            / 3600
            / 24
        )
        for item in lst
    ]


this_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(this_dir, "groups.json"), "r") as f:
    groups = json.load(f)


# plot total questions
with open(os.path.join(this_dir, "data", "none.json"), "r") as f:
    lst = json.load(f)
all_q = [item[2] for item in lst]
#
x = get_middle_times(lst)
y = get_num_questions_per_day(lst)
#
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.grid()
plt.ylim(0)
plt.title("Total number of questions per day")
plt.savefig("all.svg", transparent=True, bbox_inches="tight")
plt.close()

absolute = False
for title, tags in groups.items():
    all_x = []
    all_data = []
    all_labels = []
    for tag in tags:
        filename = os.path.join(this_dir, "data", f"{tag}.json")
        if not os.path.exists(filename):
            continue
        with open(filename, "r") as f:
            lst = json.load(f)

        all_x.append(get_middle_times(lst))

        if absolute:
            all_data.append(get_num_questions_per_day(y))
        else:
            # percentage over all questions on stackoverflow
            all_data.append(
                [
                    item[2] / num_all_questions * 100
                    for item, num_all_questions in zip(lst, all_q)
                ]
            )

        all_labels.append(f"[{tag}]")

    # sort by last value
    last_values = [d[-1] for d in all_data]
    i = argsort(last_values)[::-1]
    all_x = [all_x[j] for j in i]
    all_data = [all_data[j] for j in i]
    all_labels = [all_labels[j] for j in i]

    plt.figure(figsize=(8, 5))
    for x, data, label in zip(all_x, all_data, all_labels):
        plt.plot(x, data, label=label)

    plt.grid()
    plt.ylim(0)
    if absolute:
        plt.title("Questions per day")
    else:
        plt.title("% of all questions that month")
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    # plt.show()
    plt.savefig(f"{title}.svg", transparent=True, bbox_inches="tight")
    plt.close()
