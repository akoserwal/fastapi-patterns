from fastapi import FastAPI
from interfaces.user_router import user_router

app = FastAPI()

# Include the User router
app.include_router(user_router, prefix="/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI DDD Project"}
