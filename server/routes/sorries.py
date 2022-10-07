from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from server.sorries import Sorry, UpdateSorry


router = APIRouter()

@router.post("/", response_description="Sorry added to the database")
async def add_sorry(sorry: Sorry) -> dict:
    await sorry.create()
    return {"message": "Sorry added successfully"}
