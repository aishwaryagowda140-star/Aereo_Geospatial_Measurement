# Aereo Geospatial Measurement API

A backend REST API that allows users to upload geospatial files and calculate **area** and **distance** using Python, FastAPI, GeoPandas, and Shapely.

## 🚀 Features

- Upload geospatial files through REST API
- Calculate polygon area
- Calculate line distance
- Return measurements in meters and kilometers
- Validate uploaded file types
- Validate geospatial data and coordinate reference systems
- Automatically remove temporary uploaded files after processing
- Health check endpoint
- Interactive Swagger API documentation
- Clean error responses for invalid files

## 🛠️ Technologies Used

- Python
- FastAPI
- GeoPandas
- Shapely
- Uvicorn
- Git & GitHub

## 📁 Supported File Types

The API currently accepts:

- `.geojson`
- `.json`
- `.shp`

## 🔗 API Endpoints

### 1. Health Check

```text
GET /health