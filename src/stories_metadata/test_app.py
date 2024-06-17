import datetime
from pathlib import Path

from chispa import assert_df_equality
from pyspark.sql import SparkSession

from . import app, data_sources


def test_build_output_df(spark: SparkSession, test_files_path: Path):

    # Setup test inputs
    input_stories_df = spark.read.csv(
        str(test_files_path / "input-stories.csv"),
        header=True,
        schema=data_sources.stories["schema"]
    )

    input_stories_metadata_df = spark.read.csv(
        str(test_files_path / "input-stories-metadata.csv"),
        header=True,
        schema=data_sources.stories_metadata["schema"]
    )

    # Expected output dataframe
    expected_output_stories_metadata_df = spark.read.csv(
        str(test_files_path / "expected-stories-metadata.csv"),
        header=True,
        schema=data_sources.stories_metadata["schema"]
    )

    # Build actual ouput dataframe with the function under test.
    # Note the `processing_dt` value for defining your test cases.
    processing_dt = datetime.date(2024, 3, 1)
    actual_stories_metadata_df = app.build_output_df(
        processing_dt,
        input_stories_df,
        input_stories_metadata_df,
    )

    # Assert that actual output dataframe equals expected dataframe
    assert_df_equality(
        actual_stories_metadata_df, expected_output_stories_metadata_df,
        ignore_nullable=True, ignore_row_order=True, ignore_column_order=True
    )
