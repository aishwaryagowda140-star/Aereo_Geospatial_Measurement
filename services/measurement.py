import geopandas as gpd


def load_geospatial_file(file_path):
    """
    Load and validate a geospatial file.
    """

    try:
        data = gpd.read_file(file_path)
    except Exception as e:
        raise ValueError(f"Unable to read the geospatial file: {e}")

    if data.empty:
        raise ValueError("The uploaded file contains no geographic data.")

    if data.geometry is None:
        raise ValueError("The uploaded file does not contain geometry data.")

    if data.geometry.is_empty.all():
        raise ValueError("The uploaded file contains no valid geometry.")

    if data.crs is None:
        raise ValueError(
            "The uploaded file does not contain a coordinate reference system (CRS)."
        )

    return data


def get_geometry_info(data):
    """
    Get basic information about the uploaded geospatial data.
    """

    geometry_types = data.geometry.geom_type.unique().tolist()

    return {
        "geometry_types": geometry_types,
        "feature_count": len(data)
    }


def calculate_area(file_path):
    """
    Calculate the total area of all geometries in a geospatial file.
    """

    data = load_geospatial_file(file_path)

    projected_data = data.to_crs("EPSG:3857")

    total_area = projected_data.geometry.area.sum()

    geometry_info = get_geometry_info(data)

    return {
        "geometry_types": geometry_info["geometry_types"],
        "feature_count": geometry_info["feature_count"],
        "area_square_meters": round(float(total_area), 2),
        "area_square_kilometers": round(float(total_area) / 1_000_000, 4)
    }


def calculate_distance(file_path):
    """
    Calculate the total distance of all geometries in a geospatial file.
    """

    data = load_geospatial_file(file_path)

    projected_data = data.to_crs("EPSG:3857")

    total_distance = projected_data.geometry.length.sum()

    geometry_info = get_geometry_info(data)

    return {
        "geometry_types": geometry_info["geometry_types"],
        "feature_count": geometry_info["feature_count"],
        "distance_meters": round(float(total_distance), 2),
        "distance_kilometers": round(float(total_distance) / 1000, 4)
    }