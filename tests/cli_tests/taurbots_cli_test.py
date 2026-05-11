"""Tests for the initial Taurbots command-line skeleton."""

from __future__ import annotations

import subprocess
import sys
import unittest

from taurbots.cli.main import main


class TaurbotsCliTest(unittest.TestCase):
    def test_main_without_arguments_prints_help(self) -> None:
        self.assertEqual(main([]), 0)

    def test_python_module_help_succeeds(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "taurbots", "--help"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("simulator-agnostic", result.stdout)

    def test_version_succeeds(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "taurbots", "--version"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("taurbots", result.stdout)

    def test_placeholder_subcommand_help_succeeds(self) -> None:
        for command in ("doctor", "prmrl", "benchmark"):
            with self.subTest(command=command):
                result = subprocess.run(
                    [sys.executable, "-m", "taurbots", command, "--help"],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("Placeholder", result.stdout)

    def test_placeholder_subcommand_reports_deferred_implementation(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "taurbots", "doctor"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("intentionally deferred", result.stdout)


if __name__ == "__main__":
    unittest.main()
