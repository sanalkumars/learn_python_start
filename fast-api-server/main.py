from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    print("Response from server will be sending ")
    return {"message": "Welcome, this is my first Python web server"}
