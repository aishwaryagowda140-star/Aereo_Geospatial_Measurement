import geopandas as gpd


def calculate_area(file_path):
    """
    Calculate the area of all geometries in a geospatial file.
    """

    data = gpd.read_file(file_path)

    if data.empty:
        raise ValueError("The uploaded file contains no geographic data.")

    if data.geometry.is_empty.all():
        raise ValueError("The uploaded file contains no valid geometry.")

    # Convert to a projected coordinate system suitable for area calculation
    projected_data = data.to_crs("EPSG:3857")

    total_area = projected_data.geometry.area.sum()

    return {
        "area_square_meters": round(float(total_area), 2),
        "area_square_kilometers": round(float(total_area) / 1_000_000, 4)
    }
def calculate_distance(file_path):
    """
    Calculate the total length of all geometries in a geospatial file.
    """

    data = gpd.read_file(file_path)

    if data.empty:
        raise ValueError("The uploaded file contains no geographic data.")

    if data.geometry.is_empty.all():
        raise ValueError("The uploaded file contains no valid geometry.")

    # Convert to a projected coordinate system suitable for distance calculation
    projected_data = data.to_crs("EPSG:3857")

    total_distance = projected_data.geometry.length.sum()

    return {
        "distance_meters": round(float(total_distance), 2),
        "distance_kilometers": round(float(total_distance) / 1000, 4)
    }