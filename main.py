from fastapi import FastAPI

from config import settings

app = FastAPI(title="Bookstore")


@app.get("/")
def hello():
    return "Hello World"

