from fastapi import FastAPI, UploadFile, File
import shutil
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume

app = FastAPI()

@app.post("/analyze-resume")

async def analyze(file: UploadFile = File(...)):

    file_location = f"resumes/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_location)

    result = analyze_resume(text)

    return result