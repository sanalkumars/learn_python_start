from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
import controllers.controller as mainController

router = APIRouter()

# Simple auth dependency (example - in real app, use JWT or similar)
def verify_token(token: str = None):
    if token != "secret":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return token

@router.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return mainController.read_item(item_id, q)

@router.post("/items/")
def post_item(item: dict):
    return mainController.create_item(item)

@router.put("/items/{item_id}")
def put_item(item_id: int, item: dict):
    return mainController.update_item(item_id, item)

@router.delete("/items/{item_id}")
def del_item(item_id: int):
    return mainController.delete_item(item_id)

# Protected route with auth
@router.get("/protected/")
def protected_route(token: str = Depends(verify_token)):
    return {"message": "This is protected", "token": token}

# File upload route
@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "content_type": file.content_type}