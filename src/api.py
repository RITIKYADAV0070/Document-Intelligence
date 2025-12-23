from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.main import main as run_pipeline
import json

app = FastAPI(
    title="Document Intelligence API",
    description="AI-based extraction of CRIF & GSTR-3B documents",
    version="1.0"
)

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
def extract_documents():
    run_pipeline()
    with open("outputs/final_output.json") as f:
        return json.load(f)
