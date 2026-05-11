"""Taurbots package skeleton for robot-navigation research tooling."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("taurbots")
except PackageNotFoundError:  # pragma: no cover - only used from an uninstalled tree
    __version__ = "0.0.0"

__all__ = ["__version__"]
