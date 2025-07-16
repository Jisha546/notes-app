from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/notes")
def get_notes():
    return [{"id": 1, "content": "This is a note"}]
