"""
Contains pytest fixtures. When pytest runs it will automatically load all the fixtures
from all modules named `conftest.py` found in the directory paths containing the test.

Reference: https://docs.pytest.org/en/stable/explanation/fixtures.html
"""
import pytest
import os.path

from pathlib import Path
from pyspark.sql import SparkSession


@pytest.fixture
def test_files_path() -> Path:
    """Returns a Path to the test_files directory."""
    return Path(os.path.dirname(__file__)) / "test_files"


@pytest.fixture
def spark(request) -> SparkSession:
    """Returns a new local SparkSession for the currently running test request."""
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName(request.node.name) \
        .getOrCreate()

    # Must cleanup spark so that each test gets a newly created SparkSession.
    try:
        yield spark
    finally:
        spark.stop()
