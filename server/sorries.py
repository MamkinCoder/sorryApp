from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional

from beanie.odm.operators.update.general import CurrentDate


class Sorry(Document):
    text: str
    forgives: int
    condemns: int
    ts: datetime = datetime.now()

    CurrentDate({ts, True})

    class Settings:
        name = "sorries"


    class Config:
        schema_extra = {
            "example": {
                "text": "I am sorry for being naughty.",
                "forgives": 100,
                "condemns": 5,
                "ts": datetime.now()
            }
        }


class UpdateSorry(BaseModel):
    text: Optional[str]
    forgives: Optional[str]
    condemns: Optional[float]
    ts: datetime = datetime.now()

    CurrentDate({ts, True})

    class Config:
        schema_extra = {
            "example": {
                "text": "I am sorry for being the best!",
                "forgives": 1,
                "condemns": 100,
                "ts": datetime.now()
            }
        }
