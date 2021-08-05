import json
import pathlib

from rich.progress import Progress

import stacktags


def update_groups():
    this_dir = pathlib.Path(__file__).resolve().parent
    with open(this_dir / "groups.json") as f:
        data = json.load(f)

    tags = sorted(set([tag for group in data.values() for tag in group]))

    with Progress() as progress:
        task = progress.add_task("tag", total=len(tags))

        for tag in tags:
            progress.update(task, description=tag)
            stacktags.stackoverflow.update_file(
                this_dir / "data" / (tag + ".json"),
                tag=tag,
                license="CC BY",
                creator="Nico Schlömer",
            )
            progress.advance(task)


if __name__ == "__main__":
    update_groups()
