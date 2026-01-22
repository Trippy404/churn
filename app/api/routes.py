from fastapi import APIRouter, UploadFile, File, Form
import pandas as pd
from app.ml.pipeline import ChurnPipeline

router = APIRouter(prefix="/api")

@router.post("/run")
async def run_pipeline(
    file: UploadFile = File(...),
    target: str = Form(...),
    algorithm: str = Form(...)
):
    df = pd.read_csv(file.file)

    pipeline = ChurnPipeline(algorithm)
    results = pipeline.execute(df, target)

    return results
