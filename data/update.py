import json
import pathlib

from rich.progress import Progress

import stacktags


def _string_fixed_length(string, length):
    if len(string) > length:
        return string[:length]
    return string.rjust(length)


def update_groups():
    this_dir = pathlib.Path(__file__).resolve().parent
    with open(this_dir / "groups.json") as f:
        data = json.load(f)

    with Progress() as progress:
        task1 = progress.add_task("group", total=len(data))
        task2 = progress.add_task("tag", total=0)

        for group_name, tags in data.items():
            progress.update(task1, description=_string_fixed_length(group_name, 20))
            progress.update(task2, total=len(tags), completed=0)
            for tag in tags:
                progress.update(task2, description=_string_fixed_length(tag, 20))
                stacktags.stackoverflow.update_file(
                    this_dir / "data" / (tag + ".json"),
                    tag=tag,
                    license="CC BY",
                    creator="Nico Schlömer",
                )
                progress.advance(task2)
            progress.advance(task1)


if __name__ == "__main__":
    update_groups()
