from fastapi import FastAPI
from routes.user_router import user_router

app = FastAPI()

app.include_router(user_router, prefix="/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI SOLID Project"}
