from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

notes = []

@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes")
def add_note(note: dict):
    notes.append(note)
    return {"message": "Note added"}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
        return {"message": "Note deleted"}
    return {"error": "Invalid note ID"}
