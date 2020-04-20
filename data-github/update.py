import argparse
import json
import pathlib
from datetime import timedelta

import hotware


def update_groups():
    args = parse_args()

    this_dir = pathlib.Path(__file__).resolve().parent
    with open(this_dir / "groups.json") as f:
        data = json.load(f)

    for group in data.values():
        print()
        for repo in group:
            print(repo, "...")
            hotware.github.update_file(
                this_dir / "data" / "{}.json".format(repo.replace("/", "_")),
                max_interval_length=timedelta(days=30),
                repo=repo,
                license="CC BY",
                creator="Nico Schlömer",
                token=args.token,
            )


def parse_args():
    parser = argparse.ArgumentParser(description="GitHub star history")
    parser.add_argument(
        "--token", "-t", type=str, help="GitHub access token (for more requests)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    update_groups()
