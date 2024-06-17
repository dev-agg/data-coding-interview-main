"""
Contains pytest fixtures. When pytest runs it will automatically load all the fixtures
from all modules named `conftest.py` found in the directory paths containing the test.

Reference: https://docs.pytest.org/en/stable/explanation/fixtures.html
"""
import pytest
import os.path

from pathlib import Path


@pytest.fixture
def test_files_path() -> Path:
    """Returns a Path to the test_files directory."""
    return Path(os.path.dirname(__file__)) / "test_files"
