from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World", "University": "UMT"}

@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to this API"}