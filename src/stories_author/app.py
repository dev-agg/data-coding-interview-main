"""
This is the public version of `app.py` - that will be made available in the public git repos.

The candidate will be asked to make improvements.
"""
import csv
from datetime import date
from pathlib import Path

from . import models

import logging
logger = logging.getLogger(__name__)


def transform(
    output_stories_author_csv_p: Path,
    stories_csv_p: Path,
    users_csv_p: Path,
    modified_dt: date
):
    """
    Joins records from stories_csv_p [models.Story] with the users_csv_p [models.User] records
    on `Story.author_id=User.id`. Only Story records that that have been modified on the given
    modified_dt date [Story.modified_ts=modified_dt] are selected.

    The result is then outputted as CSV to output_stories_author_csv_p [models.StoryAuthor].
    """

    # Read input csv files
    with stories_csv_p.open() as stories_csv_f, \
            users_csv_p.open() as users_csv_f:

        stories_csv_r = csv.DictReader(stories_csv_f)
        story_models = [models.Story(**row) for row in stories_csv_r]

        users_csv_r = csv.DictReader(users_csv_f)
        user_models = [models.User(**row) for row in users_csv_r]

    # List used to track rows that will be outputted
    output_rows = []

    for story in story_models:
        if story.modified_ts.date() != modified_dt:
            continue

        for user in user_models:
            if user.id == story.author_id:
                story_author = models.StoryAuthor(
                    id=story.id,
                    title=story.title,
                    summary=story.summary,
                    author_id=user.id,
                    author_name=user.name,
                    author_profile=user.profile,
                    author_email=user.email)
                output_rows.append(dict(story_author))

    # Save output_rows to output csv file
    with output_stories_author_csv_p.open('w') as output_f:
        output_w = csv.DictWriter(output_f, models.StoryAuthor.model_fields.keys())
        output_w.writeheader()
        output_w.writerows(output_rows)