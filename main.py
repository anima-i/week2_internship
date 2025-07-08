from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def say_hello(name: str):
    return{"message": f"Hello {name}"}

@app.get("/sum")
def calculate_sum(a: int, b: int):
    return{"sum": a + b}

