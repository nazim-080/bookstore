from fastapi import FastAPI

app = FastAPI(title="Bookstore")


@app.get("/")
def hello():
    return "Hello world"

