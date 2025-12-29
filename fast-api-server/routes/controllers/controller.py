def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

def create_item(item: dict):
    return {"item": item, "message": "Item created successfully"}

def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item, "message": "Item updated successfully"}

def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deleted successfully"}