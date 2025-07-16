from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = []


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def add_todo(item: str):
    todos.append(item)
    return {"message": "Added", "todos": todos}
