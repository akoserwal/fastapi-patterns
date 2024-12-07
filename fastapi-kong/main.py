from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello")
async def root():
    return {"message": "Hello World"}


@app.get("/api/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
