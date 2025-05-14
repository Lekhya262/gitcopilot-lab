from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Welcome route
@app.get("/")
def welcome():
    return {"message": "Welcome to the Token Generator API! - Created by [Lekhya]"}

# Pydantic model for input
class TextInput(BaseModel):
    text: str

# Function to generate checksum
def generate(text: str):
    return hashlib.sha256(text.encode()).hexdigest()

# Tokenizing endpoint
@app.post("/tokenize")
def tokenize_text(input: TextInput):
    """
    Accepts input text and returns a checksum of the text.
    """
    result = generate(input.text)
    return {"checksum": result}
