from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_all_items():
    # Dummy data - in real app, fetch from database
    return {"items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}], "message": "Fetching all items"}

@router.get("/items/{item_id}")
def get_item(item_id: int):
    # Dummy response
    return {"item_id": item_id, "name": f"Item {item_id}"}

@router.post("/items")
def create_item(item: dict):
    # Dummy creation
    return {"message": "Item created", "item": item}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"message": f"Item {item_id} updated", "item": item}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}