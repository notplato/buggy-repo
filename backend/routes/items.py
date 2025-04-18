from bson import ObjectId
from fastapi import APIRouter, HTTPException
from models import Item

router = APIRouter()  # This was previously wrong


async def get_items_collection():
    from db import init_db

    return init_db()["items_collection"]


@router.get("/")
async def get_items():
    collection = await get_items_collection()
    items = []
    async for item in collection.find():
        item["_id"] = str(item["_id"])
        items.append(item)
    return items


@router.post("/")
async def create_item(item: Item):
    collection = await get_items_collection()
    result = await collection.insert_one(item.dict())
    return {"id": str(result.inserted_id)}


# This post should not be there, causing error
# @router.post("/")
# async def create_item(item: Item):
#     return {"id": "Item Inserted"}
# I want a chocolate
# fixed delete to delete an item
@router.delete("/{item_id}")
async def delete_item(item_id: str):  # ✅ Corrected
    collection = await get_items_collection()
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count:
        return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
