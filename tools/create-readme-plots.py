import json
from pathlib import Path

import sotrends

this_dir = Path(__file__).parents[0]

with open(this_dir / "groups.json") as f:
    data = json.load(f)

# make unique and sort
all_tags = [item for lst in data.values() for item in lst]
all_tags = sorted(list(set(all_tags)))

tag_data = sotrends.fetch_data(all_tags)

for group_name, tags in data.items():
    plt = sotrends.plot({tag: tag_data[tag] for tag in tags})

    xlim = plt.gca().get_xlim()
    ylim = plt.gca().get_ylim()
    plt.text(
        xlim[0],
        -(ylim[1] - ylim[0]) * 0.1,
        "StackOverflow API via nschloe/sotrends | Nico Schlömer @nschloe | CC BY",
        fontsize="x-small",
        verticalalignment="top",
    )
    plt.savefig(f"{group_name}.svg", bbox_inches="tight", transparent=True)
    # plt.show()
    plt.close()
