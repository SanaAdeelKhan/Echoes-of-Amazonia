
import ee

def initialize_gee():
    """Initializes the Earth Engine API."""
    try:
        ee.Initialize()
    except Exception as e:
        ee.Authenticate()
        ee.Initialize()

def get_ndvi_image(region, start_date, end_date):
    """Fetches NDVI image from Sentinel-2 for a given region and date range."""
    collection = (ee.ImageCollection("COPERNICUS/S2_SR")
                    .filterBounds(region)
                    .filterDate(start_date, end_date)
                    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10)))
    
    ndvi = collection.map(lambda img: img.normalizedDifference(['B8', 'B4']).rename('NDVI'))
    return ndvi.median().clip(region)
