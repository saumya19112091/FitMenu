from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    print("hello world")
    return {"hello": "world"}