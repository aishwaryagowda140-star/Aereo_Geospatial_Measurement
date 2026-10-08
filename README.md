# Aereo Geospatial Measurement API

A backend API for measuring geographic data from uploaded geospatial files.

## Features

* Upload geospatial files through an API
* Calculate polygon area
* Calculate line distance
* Return measurements in meters and kilometers
* Validate supported file formats
* Provide API health status
* Interactive Swagger API documentation

## Technologies Used

* Python
* FastAPI
* GeoPandas
* Shapely
* Uvicorn

## Supported File Types

* `.geojson`
* `.json`
* `.shp`

## API Endpoints

### Health Check

`GET /health`

Returns the current API health status.

### Area Measurement

`POST /measure/area`

Uploads a geospatial file and calculates its area.

### Distance Measurement

`POST /measure/distance`

Uploads a geospatial file and calculates its total distance/length.

## Running the Project

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Open the Swagger documentation:

`http://127.0.0.1:8000/docs`

## Project Structure

```text
Aereo_Geospatial_Measurement/
│
├── main.py
├── requirements.txt
├── README.md
│
├── services/
│   └── measurement.py
│
├── uploads/
│
├── test_files/
│   ├── sample.geojson
│   └── sample_line.geojson
│
└── venv/
```

## Example

The API accepts a GeoJSON polygon for area measurement and a GeoJSON LineString for distance measurement.

The result is returned as JSON with the uploaded filename and calculated measurement.

## Project Status

Core area and distance measurement functionality has been implemented and tested using FastAPI Swagger UI.
