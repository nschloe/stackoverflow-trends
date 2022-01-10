import json
from pathlib import Path

from _main import fetch_data, plot_per_day

this_dir = Path(__file__).resolve().parent

with open(this_dir / "groups.json") as f:
    groups = json.load(f)

# make unique and sort
all_tags = [item for lst in groups.values() for item in lst]
all_tags = sorted(list(set(all_tags)))

tag_data = fetch_data(all_tags, cache_dir=this_dir / ".." / "cache")

plot_dir = this_dir / ".." / "plots"
plot_dir.mkdir(exist_ok=True)

for group_name, tags in groups.items():
    # cut chosen such that rust is just part of the crew :)
    plt = plot_per_day({tag: tag_data[tag] for tag in tags}, cut=0.018)

    plt.title("Daily number of questions on StackOverflow", fontsize=14)

    xlim = plt.gca().get_xlim()
    ylim = plt.gca().get_ylim()
    plt.text(
        xlim[0],
        -(ylim[1] - ylim[0]) * 0.1,
        "@nschloe / so-trends | Nico Schlömer | CC BY",
        fontsize="x-small",
        verticalalignment="top",
    )
    plt.savefig(plot_dir / f"{group_name}.svg", bbox_inches="tight", transparent=True)
    # plt.show()
    plt.close()
