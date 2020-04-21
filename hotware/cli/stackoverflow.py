import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt

from ..__about__ import __version__
from ..stackoverflow import update_file
from ..tools import plot_per_day


def tag_history(argv=None):
    args = parse_args(argv)

    # get the data
    filenames = []
    for tag in args.tags:
        p = Path(".") if args.cache_dir is None else Path(args.cache_dir)
        filenames.append(p / ("stackoverflow-" + tag + ".json"))
        update_file(filenames[-1], tag=tag, title="StackOverflow tags")

    # plot it
    plot_per_day(filenames)
    plt.title("Daily number of questions on StackOverflow")
    plt.show()


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="StackOverflow tag history",
        # Needed for line break in --version:
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("tags", nargs="+", type=str, help="tags to analyze")

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output image file (optional, default: show plot)",
    )

    parser.add_argument(
        "-d",
        "--cache-dir",
        type=str,
        help="Cache directory (optional, default: current directory)",
    )

    version = "\n".join(
        [
            "hotware {} [Python {}.{}.{}]".format(
                __version__,
                sys.version_info.major,
                sys.version_info.minor,
                sys.version_info.micro,
            ),
            "Copyright (C) 2020 Nico Schlömer <nico.schloemer@gmail.com>",
        ]
    )

    parser.add_argument(
        "--version",
        "-v",
        help="display version information",
        action="version",
        version=version,
    )
    return parser.parse_args(argv)
