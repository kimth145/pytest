from fastapi import FastAPI


app = FastAPI()


@app.get("/test/{a}/{b}")
async def login(a: int, b: int):
    return a+b
