from fastapi import FastAPI, UploadFile, File, HTTPException
from services.measurement import calculate_area, calculate_distance
import os
import shutil

app = FastAPI(
    title="Aereo Geospatial Measurement API",
    description="Backend API for measuring area and distance from uploaded geospatial files.",
    version="1.0.0"
)

ALLOWED_EXTENSIONS = {".geojson", ".json", ".shp"}


def validate_file(filename):
    if not filename:
        raise ValueError("No file was provided.")

    extension = os.path.splitext(filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Unsupported file type. Allowed types: .geojson, .json, .shp"
        )


@app.get("/")
def home():
    return {
        "message": "Aereo Geospatial Measurement API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/measure/area")
async def measure_area(file: UploadFile = File(...)):
    try:
        validate_file(file.filename)

        file_path = os.path.join("uploads", file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = calculate_area(file_path)

        return {
            "filename": file.filename,
            "measurement": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.post("/measure/distance")
async def measure_distance(file: UploadFile = File(...)):
    try:
        validate_file(file.filename)

        file_path = os.path.join("uploads", file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = calculate_distance(file_path)

        return {
            "filename": file.filename,
            "measurement": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )