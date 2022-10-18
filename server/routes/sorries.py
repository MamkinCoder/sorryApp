from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from server.sorries import Sorry, UpdateSorry


router = APIRouter()

@router.post("/", response_description="Sorry added to the database")
async def add_sorry(sorry: Sorry) -> dict:
    if "Hello" in sorry.text:
        print("WHat??")
    await sorry.create()
    # if not record:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="Review record not found!"
    #     )
    return {"message": "Sorry added successfully"}


@router.get("/{id}", response_description="Sorry retrieved")
async def get_sorry(id: PydanticObjectId) -> Sorry:
    sorry = await Sorry.get(id)
    return sorry


@router.get("/", response_description="Sorries retrieved")
async def get_reviews() -> List[Sorry]:
    sorries = await Sorry.find_all().to_list()
    return sorries


@router.put("/{id}", response_description="Sorry updated")
async def update_sorry(id: PydanticObjectId, req: UpdateSorry) -> Sorry:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    sorry = await Sorry.get(id)
    if not sorry:
        raise HTTPException(
            status_code=404,
            detail="Sorry record not found!"
        )

    await sorry.update(update_query)
    return sorry


@router.delete("/{id}", response_description="Sorry deleted from the database")
async def delete_sorry(id: PydanticObjectId) -> dict:
    sorry = await Sorry.get(id)

    if not sorry:
        raise HTTPException(
            status_code=404,
            detail="Sorry record not found!"
        )

    await sorry.delete()
    return {
        "message": "Sorry deleted successfully"
    }
