# Climate Analysis: Don Bosco, Villas de Andalucía (2000-2025)

## 📋 Description

This project develops a comprehensive analysis of climate behavior in **Don Bosco, Villas de Andalucía**, Panama City, during the period 2000-2025. The program collects, processes, and analyzes historical climate data to identify trends, anomalies, and correlations in precipitation variation and other climate parameters, considering global climate phenomena (El Niño, La Niña) and local factors.

## 🎯 Objectives

- **Collect** historical climate data from multiple reliable sources (NOAA, NASA, IDEAM/ETESA).
- **Analyze** trends and anomalies in rainfall intensity.
- **Correlate** climate variables with global phenomena and local factors.
- **Visualize** results with high-quality graphs and geographic maps.

## 📁 Project Structure

```
clima_don_bosco_andalucia/
├── config.py                 # Centralized configuration (Don Bosco location)
├── climate_data.py           # Data collection, cleaning, and analysis
├── visualization.py          # Graph and map generation
├── main.py                   # Main execution script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore                # Files ignored by Git
├── data/                     # Processed data
│   ├── raw/                  # Raw downloaded data
│   └── processed/            # Clean and processed data
├── plots/                    # Generated graphs (PNG)
└── notebooks/                # Jupyter notebooks for analysis
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Navigate to the project folder**:
```bash
cd TheoreticalResearch/clima_don_bosco_andalucia
```

2. **Create a virtual environment** (required to avoid system conflicts):
```bash
python3 -m venv venv
```

3. **Activate the virtual environment**:
```bash
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

**Note**: Always make sure to activate the virtual environment before running the code. You'll see `(venv)` in your prompt when it's activated.

**Note**: Installing `cartopy` may require system dependencies. On Ubuntu/Debian:
```bash
sudo apt-get install libproj-dev proj-data proj-bin libgeos-dev
```

## 📊 Usage

### Complete Execution

**Important**: Make sure you have the virtual environment activated before running.

To run the complete analysis:

```bash
# Activate virtual environment (if not activated)
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows

# Run complete analysis
python main.py
```

This script:
1. Downloads climate data from NOAA
2. Downloads ENSO indices
3. Cleans and processes data
4. Performs statistical analysis
5. Generates visualizations

### Modular Usage

#### 1. Data Collection and Analysis

```python
from climate_data import (
    fetch_noaa_data, clean_climate_data, aggregate_to_monthly,
    calculate_precipitation_trends, detect_anomalies_zscore,
    correlate_with_enso
)
from config import START_YEAR, END_YEAR, LOCATION

# Download and process data
df_climate = fetch_noaa_data(START_YEAR, END_YEAR, LOCATION)
df_clean = clean_climate_data(df_climate)
df_monthly = aggregate_to_monthly(df_clean)

# Analysis
trends = calculate_precipitation_trends(df_monthly)
df_anomalies = detect_anomalies_zscore(df_monthly, 'precipitation_mm')
```

#### 2. Visualization

```python
from visualization import (
    plot_time_series, plot_precipitation_anomalies, plot_enso_correlation
)

# Time series
plot_time_series(df_monthly, 'date', 'precipitation_mm',
                title='Monthly Precipitation - Don Bosco, Villas de Andalucía',
                save_path='precipitacion_temporal.png')

# Anomalies
plot_precipitation_anomalies(df_monthly, save_path='anomalias.png')
```

### Jupyter Notebook

An example notebook is included in `notebooks/analysis_example.ipynb` for interactive analysis.

## 📈 Data Sources

### NOAA (National Oceanic and Atmospheric Administration)
- **Dataset**: Global Historical Climatology Network (GHCN)
- **Variables**: Precipitation, temperature, humidity
- **Access**: Public API (with limitations) or manual download

### NASA Earthdata
- **Datasets**: MODIS (vegetation indices), climate products
- **Access**: Requires account and authentication
- **Format**: NetCDF/HDF

### ENSO Indices
- **Source**: Climate Prediction Center (NOAA)
- **Index**: Oceanic Niño Index (ONI)
- **Access**: Public

### Note on Real Data
This project includes functions to download real data, but due to limitations in accessing public APIs, it may generate simulated data based on real patterns for development and testing. For production, it is recommended to:

1. Obtain API access credentials
2. Download complete datasets manually
3. Use local data from institutions like ETESA (Panama)

## 🔬 Analysis Methodology

### Descriptive Statistics
- Central tendency measures (mean, median)
- Dispersion measures (standard deviation, range)
- Shape measures (skewness, kurtosis)

### Trend Analysis
- Linear regression to identify long-term trends
- Statistical significance tests (p-value)
- Coefficient of determination (R²)

### Anomaly Detection
- **Z-Score Method**: Identifies values exceeding statistical thresholds
- **STL Decomposition**: Separates seasonal, trend, and residual components

### Correlation with Climate Phenomena
- Pearson correlation with ENSO indices (ONI)
- Analysis of extreme events during El Niño/La Niña

## 📊 Generated Visualizations

The project generates the following types of graphs:

1. **Time Series**: Precipitation vs. time with trend line
2. **Anomalies**: Bar charts showing deviations from the mean
3. **Heat Maps**: Monthly precipitation by year
4. **Annual Boxplots**: Precipitation distribution by year
5. **ENSO Correlation**: Relationship between precipitation and ONI indices
6. **Location Maps**: Where the study area is located
7. **Correlation Matrices**: Correlations between multiple variables

All graphs are exported in high resolution (300 DPI) in PNG format.

## 📚 References and Bibliography

This analysis uses data and references from:
- NOAA Climate Data Online
- NASA Earthdata
- IPCC Reports (AR6)
- Academic publications on Panama's climate
- Studies on ENSO and its regional impact

## 🔧 Configuration

Main configurations are found in `config.py`:

- **Location**: Coordinates of Don Bosco, Villas de Andalucía, Panama
- **Analysis period**: Start and end years
- **Thresholds**: For anomaly detection (Z-Score, STL)
- **Paths**: Data and graph directories
- **Visualization parameters**: DPI, format, sizes

## 🐛 Troubleshooting

### Error installing Cartopy
```bash
# Ubuntu/Debian
sudo apt-get install libproj-dev proj-data proj-bin libgeos-dev

# macOS (with Homebrew)
brew install proj geos

# Then reinstall cartopy
pip install --upgrade cartopy
```

### Data not downloading correctly
- Check internet connection
- Public APIs may have rate limitations
- The code includes simulated data as a backup for development

## 📝 Contributions

This project is educational and for research. To contribute:

1. Fork the repository
2. Create branch for new functionality
3. Make changes and test
4. Send Pull Request with detailed description

## 📄 License

This project is provided for educational and research purposes. The data used may be subject to licenses from their respective sources (NOAA, NASA, etc.).

## 👤 Author

Computational Climate Analysis - Research Project

## 🙏 Acknowledgments

- NOAA for providing public climate data
- NASA for access to satellite data
- Scientific community for open-source tools

---

**Last update**: 2025
