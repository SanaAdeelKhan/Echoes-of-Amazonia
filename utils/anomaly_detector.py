
import numpy as np

def detect_ndvi_anomalies(ndvi_array, threshold=1.5):
    """Detects anomalies in an NDVI array based on z-score thresholding."""
    mean = np.mean(ndvi_array)
    std = np.std(ndvi_array)
    z_scores = (ndvi_array - mean) / std
    return np.where(np.abs(z_scores) > threshold)
