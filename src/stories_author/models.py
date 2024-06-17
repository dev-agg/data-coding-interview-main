"""
Contains Pydantic models required by the package.
To learn more the Pydantic library, see https://docs.pydantic.dev/latest/.

These models are used to simplify reading and writing CSVs.
Usage example:
```
import csv
from pathlib import Path

from . import models

def read_stories_model(stories_csv_path: Path):
    with stories_csv_path.open() as stories_csv_f:
        csv_r = csv.DictReader(csv_f)
        for row in csv_r:
            try:
                model = models.Story(**row)
            except models.ValidationError:
                print(f"Failed to validate csv row: {row}. Skipping.")
                pass
            yield Model

def write_story_author_models(
    output_csv_path: Path
    story_author_models: List[models.StoryAuthorModel]):

    with output_csv_path.open('w') output_csv_f:
        csv_w = csv.DictWriter(csv_f, models.StoryAuthorModel.model_fields.keys())
        csv_w.writeheader()

        for story_author in story_author_models:
            row = dict(story_author)
            csv_w.writerow(row)
```
"""
from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator, ValidationError

__all__ = ('ValidationError', 'Story', 'User', 'StoryAuthor')


class csv_model(BaseModel):
    """A BaseModel that converts empty field string values to None (null).
    This is desirable for deserializing CSV records."""
    @field_validator('*')
    def empty_str_to_none(cls, v):
        if v == '':
            return None
        return v


class Story(csv_model):
    """Story models a Wattpad story."""
    id: int
    created_ts: datetime
    modified_ts: datetime
    author_id: int
    title: str
    summary: str


class User(csv_model):
    """User models a Wattpad user."""
    id: int
    created_ts: datetime
    modified_ts: datetime
    name: str
    profile: str
    email: EmailStr


class StoryAuthor(csv_model):
    """StoryAuthor models the aggregation of Story and User models
    that are joined on `Story.author_id=User.id`."""
    id: int
    title: str
    summary: str
    author_id: int
    author_name: str
    author_profile: str
    author_email: str
