import csv
import datetime
from pathlib import Path
from typing import Any, List, OrderedDict, Union

from . import app


def test_transform(test_files_path: Path, tmp_path: Path):
    """Tests the app.transform() function."""

    # Setup test arguments for transform.
    input_stories_csv_path = test_files_path / "input-stories.csv"
    input_users_csv_path = test_files_path / "input-users.csv"
    actual_output_stories_author_csv_path = tmp_path / "actual-output-stories-auhtor.csv"
    modified_dt = datetime.date(2024, 6, 2)

    # Path to the csv file that contains the expected results.
    expected_output_stories_author_csv_path = test_files_path / "expected-output-stories-author.csv"

    # Run the function under test.
    app.transform(
        actual_output_stories_author_csv_path,
        input_stories_csv_path,
        input_users_csv_path,
        modified_dt
    )

    # Assert actual output contains the expected records.
    actual_output_rows = read_csv_rows_sorted(actual_output_stories_author_csv_path)
    expected_output_rows = read_csv_rows_sorted(expected_output_stories_author_csv_path)
    assert actual_output_rows == expected_output_rows


#
# Test Helpers

def read_csv_rows_sorted(csv_path: Path) -> List[OrderedDict[Union[str, Any], Union[str, Any]]]:
    """Reads the given csv_path and returns all its rows sorted."""
    with csv_path.open() as csv_f:
        csv_r = csv.DictReader(csv_f)
        rows = list(csv_r)
    rows.sort()
    return rows
