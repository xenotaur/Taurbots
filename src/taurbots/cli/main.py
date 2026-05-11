"""Lightweight command-line entry points for the Taurbots skeleton."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from taurbots import __version__

_PLACEHOLDER_MESSAGE = (
    "This Taurbots command is a placeholder. Implementation is intentionally "
    "deferred to a later focused PR."
)


def _placeholder(command_name: str) -> int:
    print(f"taurbots {command_name}: {_PLACEHOLDER_MESSAGE}")
    return 1


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level Taurbots argument parser."""
    parser = argparse.ArgumentParser(
        prog="taurbots",
        description=(
            "Taurbots is a simulator-agnostic robot-navigation research harness. "
            "This initial CLI exposes only lightweight placeholders."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"taurbots {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    doctor_parser = subparsers.add_parser(
        "doctor",
        help="show placeholder workstation diagnostics command help",
        description="Placeholder for future safe workstation diagnostics.",
    )
    doctor_parser.set_defaults(func=lambda _args: _placeholder("doctor"))

    prmrl_parser = subparsers.add_parser(
        "prmrl",
        help="show placeholder PRM-RL command help",
        description="Placeholder for the future PRM-RL algorithm workflow.",
    )
    prmrl_parser.set_defaults(func=lambda _args: _placeholder("prmrl"))

    benchmark_parser = subparsers.add_parser(
        "benchmark",
        help="show placeholder benchmark adapter command help",
        description="Placeholder for future external benchmark adapter workflows.",
    )
    benchmark_parser.set_defaults(func=lambda _args: _placeholder("benchmark"))

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the Taurbots CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 0
    return int(args.func(args))
