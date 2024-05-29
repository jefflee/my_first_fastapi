from typing import Optional
from fastapi import FastAPI

app = FastAPI()  # Create a Fast API application


@app.get("/")
def read_root():
    """ hello world """
    return {"Hello": "World"}


@app.get("/asyncapi")
async def read_root_async():
    """ async hello world """
    return {"async": "Hello World"}


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Optional[str] = None):
    """ Get a user by id """
    return {"user_id": user_id, "q": q}
