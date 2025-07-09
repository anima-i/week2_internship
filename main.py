from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User (BaseModel):
    name: str 
    age: int = Field(..., gt=0, description="Age must be a positive integer")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def say_hello(name: str):
    return{"message": f"Hello {name}"}

@app.get("/sum")
def calculate_sum(a: int, b: int):
    return{"sum": a + b}

@app.post("/user")
def create_user(user: User):
    return {"message": f"User {user.name} created successfully", "age": user.age}

