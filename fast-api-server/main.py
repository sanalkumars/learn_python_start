from fastapi import FastAPI
from main_routes.route import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def greet():
    print("Response from server will be sending ")
    return {"message": "Welcome, this is my first Python web server"}
