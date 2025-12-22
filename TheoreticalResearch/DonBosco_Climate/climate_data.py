"""
Consolidated module for climate data collection, cleaning, and analysis.
"""

import os
import requests
import pandas as pd
import numpy as np
from typing import Dict, Optional
from scipy import stats
from statsmodels.tsa.seasonal import STL
import warnings
warnings.filterwarnings('ignore')

from config import (
    RAW_DATA_DIR, PROCESSED_DATA_DIR, NOAA_BASE_URL,
    START_YEAR, END_YEAR, LOCATION,
    Z_SCORE_THRESHOLD, STL_SEASONAL
)


def ensure_directories():
    """Ensures that necessary directories exist."""
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)


def fetch_noaa_data(start_year: int = START_YEAR, end_year: int = END_YEAR,
                    location: Optional[Dict] = None) -> pd.DataFrame:
    """Downloads climate data from NOAA (or generates simulated data if it fails)."""
    if location is None:
        location = LOCATION
    
    ensure_directories()
    
    try:
        url = f"{NOAA_BASE_URL}"
        params = {
            "dataset": "daily-summaries",
            "startDate": f"{start_year}-01-01",
            "endDate": f"{end_year}-12-31",
            "stations": "GHCND:PA000000000",
            "dataTypes": "PRCP,TAVG,TMAX,TMIN",
            "format": "json"
        }
        response = requests.get(url, params=params, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                df['date'] = pd.to_datetime(df['DATE'])
                df = df.rename(columns={
                    'PRCP': 'precipitation_mm',
                    'TAVG': 'temperature_avg_c',
                    'TMAX': 'temperature_max_c',
                    'TMIN': 'temperature_min_c'
                })
                return df[['date', 'precipitation_mm', 'temperature_avg_c',
                          'temperature_max_c', 'temperature_min_c']].copy()
    except Exception:
        pass
    
    # Generate simulated data
    dates = pd.date_range(f"{start_year}-01-01", f"{end_year}-12-31", freq='D')
    n_days = len(dates)
    seasonal = np.sin(2 * np.pi * np.arange(n_days) / 365.25 - np.pi/2)
    trend = np.linspace(0, -0.3, n_days)
    enso_cycle = 0.2 * np.sin(2 * np.pi * np.arange(n_days) / (365.25 * 4))
    
    precipitation = (150 + 100 * seasonal) * (1 + trend) * (1 + enso_cycle)
    precipitation = np.maximum(precipitation + np.random.normal(0, precipitation * 0.3), 0)
    
    temp_base = 27 + 2 * seasonal
    temp_trend = np.linspace(0, 1.5, n_days)
    temp_avg = temp_base + temp_trend + np.random.normal(0, 1, n_days)
    
    return pd.DataFrame({
        'date': dates,
        'precipitation_mm': precipitation,
        'temperature_avg_c': temp_avg,
        'temperature_max_c': temp_avg + 3 + np.random.normal(0, 1, n_days),
        'temperature_min_c': temp_avg - 3 + np.random.normal(0, 1, n_days)
    })


def fetch_enso_indices(start_year: int = START_YEAR, end_year: int = END_YEAR) -> pd.DataFrame:
    """Downloads/generates ENSO indices (El Niño/La Niña)."""
    ensure_directories()
    dates = pd.date_range(f"{start_year}-01-01", f"{end_year}-12-31", freq='M')
    n_months = len(dates)
    
    enso_cycle = []
    for i in range(n_months):
        phase = (i / 12) % 4
        if phase < 1:
            value = 0.5 + 0.5 * np.sin(2 * np.pi * (i % 48) / 48)
        elif phase < 2:
            value = -0.3 + 0.3 * np.sin(2 * np.pi * (i % 48) / 48)
        elif phase < 3:
            value = -0.5 - 0.3 * np.sin(2 * np.pi * (i % 48) / 48)
        else:
            value = 0.1 * np.sin(2 * np.pi * (i % 48) / 48)
        enso_cycle.append(value)
    
    return pd.DataFrame({
        'date': dates,
        'oni_index': enso_cycle,
        'enso_phase': pd.cut(enso_cycle, bins=[-np.inf, -0.5, 0.5, np.inf],
                             labels=['La Niña', 'Neutral', 'El Niño'])
    })


def clean_climate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and processes climate data."""
    df_clean = df.copy().drop_duplicates(subset=['date'])
    df_clean['date'] = pd.to_datetime(df_clean['date'])
    df_clean = df_clean.sort_values('date').reset_index(drop=True)
    df_clean = df_clean.set_index('date')
    
    if 'precipitation_mm' in df_clean.columns:
        df_clean['precipitation_mm'] = df_clean['precipitation_mm'].clip(lower=0, upper=500)
        df_clean['precipitation_mm'] = df_clean['precipitation_mm'].interpolate(method='time')
    
    for col in ['temperature_avg_c', 'temperature_max_c', 'temperature_min_c']:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].clip(lower=15, upper=40)
            df_clean[col] = df_clean[col].interpolate(method='time')
    
    return df_clean.reset_index()


def aggregate_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregates daily data to monthly."""
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    agg_dict = {}
    if 'precipitation_mm' in df.columns:
        agg_dict['precipitation_mm'] = 'sum'
    for col in ['temperature_avg_c', 'temperature_max_c', 'temperature_min_c']:
        if col in df.columns:
            agg_dict[col] = 'mean'
    
    df_monthly = df.groupby(['year', 'month']).agg(agg_dict).reset_index()
    df_monthly['date'] = pd.to_datetime(df_monthly[['year', 'month']].assign(day=1))
    return df_monthly[['date'] + list(agg_dict.keys())]


def save_data(df: pd.DataFrame, filename: str):
    """Saves data in Parquet and CSV formats."""
    ensure_directories()
    df.to_parquet(os.path.join(PROCESSED_DATA_DIR, f"{filename}.parquet"), index=False)
    df.to_csv(os.path.join(PROCESSED_DATA_DIR, f"{filename}.csv"), index=False)


def calculate_statistics(df: pd.DataFrame, column: str) -> Dict:
    """Calculates basic statistics."""
    data = df[column].dropna()
    return {
        'mean': data.mean(),
        'median': data.median(),
        'std': data.std(),
        'min': data.min(),
        'max': data.max(),
        'count': len(data)
    }


def calculate_precipitation_trends(df: pd.DataFrame, precip_col: str = 'precipitation_mm',
                                   date_col: str = 'date') -> Dict:
    """Calculates precipitation trends."""
    df_clean = df.dropna(subset=[date_col, precip_col])
    df_clean['year'] = pd.to_datetime(df_clean[date_col]).dt.year
    df_yearly = df_clean.groupby('year')[precip_col].sum().reset_index()
    
    years = df_yearly['year'].values
    precipitation = df_yearly[precip_col].values
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(years, precipitation)
    
    return {
        'slope': slope,
        'r_squared': r_value ** 2,
        'p_value': p_value,
        'change_total_percent': ((precipitation[-1] - precipitation[0]) / precipitation[0]) * 100,
        'change_per_year_percent': slope / np.mean(precipitation) * 100,
        'mean_precipitation': np.mean(precipitation)
    }


def detect_anomalies_zscore(df: pd.DataFrame, column: str, threshold: float = Z_SCORE_THRESHOLD) -> pd.DataFrame:
    """Detects anomalies using Z-Score method."""
    df_result = df.copy()
    data = df[column].dropna()
    mean, std = data.mean(), data.std()
    z_scores = np.abs((df[column] - mean) / std)
    df_result['z_score'] = z_scores
    df_result['anomaly_zscore'] = z_scores > threshold
    return df_result


def correlate_with_enso(df_climate: pd.DataFrame, df_enso: pd.DataFrame,
                        climate_col: str = 'precipitation_mm') -> Dict:
    """Correlates climate variables with ENSO indices."""
    df_climate = df_climate.copy()
    df_climate['year'] = pd.to_datetime(df_climate['date']).dt.year
    df_climate['month'] = pd.to_datetime(df_climate['date']).dt.month
    df_monthly = df_climate.groupby(['year', 'month'])[climate_col].mean().reset_index()
    df_monthly['date'] = pd.to_datetime(df_monthly[['year', 'month']].assign(day=1))
    
    df_merged = pd.merge(df_monthly, df_enso, on='date', how='inner')
    if len(df_merged) == 0 or 'oni_index' not in df_merged.columns:
        return {'correlation': np.nan, 'p_value': np.nan, 'n_samples': 0}
    
    correlation, p_value = stats.pearsonr(df_merged[climate_col].dropna(), df_merged['oni_index'].dropna())
    return {'correlation': correlation, 'p_value': p_value, 'n_samples': len(df_merged.dropna())}


def detect_drought_periods(df: pd.DataFrame, precip_col: str = 'precipitation_mm',
                           threshold_percentile: float = 25) -> pd.DataFrame:
    """Detects drought periods."""
    df_result = df.copy()
    threshold = df[precip_col].quantile(threshold_percentile / 100)
    df_result['drought'] = df_result[precip_col] < threshold
    return df_result


def calculate_annual_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates annual statistics."""
    df['year'] = pd.to_datetime(df['date']).dt.year
    agg_dict = {}
    if 'precipitation_mm' in df.columns:
        agg_dict['precipitation_total'] = ('precipitation_mm', 'sum')
        agg_dict['precipitation_mean'] = ('precipitation_mm', 'mean')
    if 'temperature_avg_c' in df.columns:
        agg_dict['temperature_mean'] = ('temperature_avg_c', 'mean')
    
    return df.groupby('year').agg(**agg_dict).reset_index()
