from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class Sorry(Document):
    text: str
    forgives: int
    condemns: int
    date: datetime = datetime.now()

    class Settings:
        name = "sorries"


    class Config:
        schema_extra = {
            "example": {
                "text": "I am sorry for being naughty.",
                "forgives": 100,
                "condemns": 5,
                "date": datetime.now()
            }
        }


class UpdateSorry(BaseModel):
    text: Optional[str]
    forgives: Optional[str]
    condemns: Optional[float]
    date: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "text": "I am sorry for being the best!",
                "forgives": 1,
                "condemns": 100,
                "date": datetime.now()
            }
        }
