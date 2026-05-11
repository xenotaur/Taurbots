"""Tests for the minimal Taurbots package import surface."""

import unittest

import taurbots


class PackageImportTest(unittest.TestCase):
    def test_package_version_is_available(self) -> None:
        self.assertIsInstance(taurbots.__version__, str)
        self.assertTrue(taurbots.__version__)


if __name__ == "__main__":
    unittest.main()
