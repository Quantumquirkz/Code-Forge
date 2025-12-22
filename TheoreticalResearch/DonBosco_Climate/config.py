"""
Centralized configuration for climate analysis of Don Bosco, Villas de Andalucía.
"""

# Coordinates of Don Bosco, Villas de Andalucía, Panama
LOCATION = {
    'latitude': 8.9824,  # Latitude of Don Bosco, Panama City
    'longitude': -79.5199,  # Longitude of Don Bosco, Panama City
    'name': 'Don Bosco, Villas de Andalucía, Panama'
}

# Year range for analysis
START_YEAR = 2000
END_YEAR = 2025

# Directory paths
DATA_DIR = "data"
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
PLOTS_DIR = "plots"
NOTEBOOKS_DIR = "notebooks"

# API URLs and endpoints
NOAA_BASE_URL = "https://www.ncei.noaa.gov/access/services/data/v1"
NASA_EARTHDATA_BASE_URL = "https://cmr.earthdata.nasa.gov/search"
EM_DAT_BASE_URL = "https://public.emdat.be/api"

# Visualization parameters
PLOT_DPI = 300  # Resolution for plots
PLOT_FORMAT = 'png'  # Export format
FIG_SIZE = (12, 6)  # Standard figure size

# Analysis parameters
Z_SCORE_THRESHOLD = 2.5  # Threshold for anomaly detection using Z-Score
STL_SEASONAL = 12  # Seasonal period for STL decomposition (monthly)
