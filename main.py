import os
import json
import io
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session # NEW
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# NEW: Import your database components
from database import engine, get_db, Base
import models

# NEW: Tell SQLAlchemy to create the tables in your Postgres database
models.Base.metadata.create_all(bind=engine)

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI(title="Scam Checker API")

# Add this block to allow React to talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # This is Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Update your route to include the database session dependency (Depends(get_db))
@app.post("/analyze-scam")
async def analyze_scam(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = """
        You are an expert cybersecurity analyst specializing in elder-fraud prevention. Analyze the following text or screenshot. You must respond ONLY in strict JSON format with exactly three keys: 
        1. 'status' (Must be exactly 'Safe', 'Suspicious', or 'Scam').
        2. 'category' (A short 1-3 word classification like 'Bank Phishing' or 'None'). 
        3. 'explanation' (A single, highly empathetic, jargon-free sentence explaining why it is safe or dangerous, directed at an elderly user). 
        Do not include markdown formatting like ```json in your response.
        """
        
        response = model.generate_content([prompt, image])
        result_json = json.loads(response.text.strip())
        
        # NEW: Save the result to the database!
        new_scan = models.ScamCheck(
            status=result_json.get("status"),
            category=result_json.get("category"),
            explanation=result_json.get("explanation")
        )
        db.add(new_scan)   # Add to the session
        db.commit()        # Save it permanently
        db.refresh(new_scan) # Get the newly created ID
        
        return {"id": new_scan.id, "analysis": result_json}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))