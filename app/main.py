from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os
from app.ingest import ingest_pdf
from app.rag import get_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Ingest it into ChromaDB
    ingest_pdf(file_path)
    
    return {"message": f"✅ {file.filename} uploaded and ingested successfully"}

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    answer = get_answer(request.question)
    return {"answer": answer}

@app.get("/")
async def root():
    return {"message": "RAG Chatbot API is running!"}