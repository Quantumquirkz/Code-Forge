"""
Simplified module for climate data visualization.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Optional, List, Dict
import os

try:
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    CARTOPY_AVAILABLE = True
except ImportError:
    CARTOPY_AVAILABLE = False

from config import PLOTS_DIR, PLOT_DPI, FIG_SIZE, LOCATION


def setup_style():
    """Configures plot style."""
    try:
        plt.style.use('seaborn-v0_8-darkgrid')
    except OSError:
        try:
            plt.style.use('seaborn-darkgrid')
        except OSError:
            plt.style.use('default')
    sns.set_palette("husl")
    plt.rcParams.update({
        'figure.figsize': FIG_SIZE,
        'figure.dpi': PLOT_DPI,
        'font.size': 10,
        'axes.labelsize': 12,
        'axes.titlesize': 14
    })


def ensure_plots_dir():
    """Ensures that plots directory exists."""
    os.makedirs(PLOTS_DIR, exist_ok=True)


def plot_time_series(df: pd.DataFrame, date_col: str, value_col: str,
                     title: str = "Time Series", ylabel: str = "Value",
                     save_path: Optional[str] = None, show_trend: bool = True) -> plt.Figure:
    """Creates time series plot with trend."""
    setup_style()
    ensure_plots_dir()
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    
    df_clean = df.dropna(subset=[date_col, value_col]).sort_values(date_col)
    ax.plot(df_clean[date_col], df_clean[value_col], linewidth=1.5, alpha=0.7, label='Data')
    
    if show_trend and len(df_clean) > 1:
        from scipy import stats
        dates_num = mdates.date2num(df_clean[date_col])
        slope, intercept, r_value, _, _ = stats.linregress(dates_num, df_clean[value_col])
        trend_line = intercept + slope * dates_num
        ax.plot(df_clean[date_col], trend_line, '--', color='red', linewidth=2,
                label=f'Trend (R²={r_value**2:.3f})')
    
    mean_value = df_clean[value_col].mean()
    ax.axhline(y=mean_value, color='green', linestyle=':', linewidth=2, label=f'Mean ({mean_value:.2f})')
    
    ax.set_xlabel('Date', fontweight='bold')
    ax.set_ylabel(ylabel, fontweight='bold')
    ax.set_title(title, fontweight='bold', pad=20)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(os.path.join(PLOTS_DIR, save_path), dpi=PLOT_DPI, format='png', bbox_inches='tight')
    return fig


def plot_precipitation_anomalies(df: pd.DataFrame, date_col: str = 'date',
                                 precip_col: str = 'precipitation_mm',
                                 save_path: Optional[str] = None) -> plt.Figure:
    """Creates precipitation anomalies plot."""
    setup_style()
    ensure_plots_dir()
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    
    df_clean = df.dropna(subset=[date_col, precip_col]).sort_values(date_col)
    mean_precip = df_clean[precip_col].mean()
    anomalies = df_clean[precip_col] - mean_precip
    colors = ['red' if x < 0 else 'blue' for x in anomalies]
    
    ax.bar(df_clean[date_col], anomalies, color=colors, alpha=0.6, width=20)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
    std = df_clean[precip_col].std()
    ax.axhline(y=std, color='red', linestyle='--', linewidth=1, label='+1 Std Dev')
    ax.axhline(y=-std, color='red', linestyle='--', linewidth=1, label='-1 Std Dev')
    
    ax.set_xlabel('Date', fontweight='bold')
    ax.set_ylabel('Precipitation Anomaly (mm)', fontweight='bold')
    ax.set_title('Precipitation Anomalies - Don Bosco, Villas de Andalucía (2000-2025)', fontweight='bold', pad=20)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3, axis='y')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(os.path.join(PLOTS_DIR, save_path), dpi=PLOT_DPI, format='png', bbox_inches='tight')
    return fig


def plot_enso_correlation(df_climate: pd.DataFrame, df_enso: pd.DataFrame,
                          climate_col: str = 'precipitation_mm',
                          save_path: Optional[str] = None) -> plt.Figure:
    """Plots correlation between climate variables and ENSO indices."""
    setup_style()
    ensure_plots_dir()
    
    df_merged = pd.merge(df_climate, df_enso, on='date', how='inner').dropna(subset=[climate_col, 'oni_index'])
    if len(df_merged) == 0:
        return plt.figure()
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    ax1_twin = ax1.twinx()
    line1 = ax1.plot(df_merged['date'], df_merged[climate_col], color='blue', linewidth=1.5, label='Precipitation')
    ax1.set_xlabel('Date', fontweight='bold')
    ax1.set_ylabel('Precipitation (mm)', color='blue', fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='blue')
    
    line2 = ax1_twin.plot(df_merged['date'], df_merged['oni_index'], color='red', linewidth=1.5, label='ONI Index')
    ax1_twin.set_ylabel('ONI Index', color='red', fontweight='bold')
    ax1_twin.tick_params(axis='y', labelcolor='red')
    ax1_twin.axhline(y=0, color='gray', linestyle='--', linewidth=1)
    ax1.set_title('Precipitation vs. ENSO Index (ONI)', fontweight='bold', pad=20)
    ax1.grid(True, alpha=0.3)
    
    from scipy import stats
    slope, intercept, r_value, p_value, _ = stats.linregress(df_merged['oni_index'], df_merged[climate_col])
    x_line = np.linspace(df_merged['oni_index'].min(), df_merged['oni_index'].max(), 100)
    y_line = intercept + slope * x_line
    
    ax2.scatter(df_merged['oni_index'], df_merged[climate_col], alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
    ax2.plot(x_line, y_line, 'r--', linewidth=2, label=f'Regression (R²={r_value**2:.3f}, p={p_value:.3f})')
    ax2.set_xlabel('ONI Index', fontweight='bold')
    ax2.set_ylabel('Precipitation (mm)', fontweight='bold')
    ax2.set_title('Correlation: Precipitation vs. ENSO Index', fontweight='bold', pad=20)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(os.path.join(PLOTS_DIR, save_path), dpi=PLOT_DPI, format='png', bbox_inches='tight')
    return fig


def plot_heatmap_monthly_precipitation(df: pd.DataFrame, date_col: str = 'date',
                                       precip_col: str = 'precipitation_mm',
                                       save_path: Optional[str] = None) -> plt.Figure:
    """Creates monthly precipitation heatmap by year."""
    setup_style()
    ensure_plots_dir()
    
    df['year'] = pd.to_datetime(df[date_col]).dt.year
    df['month'] = pd.to_datetime(df[date_col]).dt.month
    pivot_table = df.pivot_table(values=precip_col, index='year', columns='month', aggfunc='mean')
    pivot_table.columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    fig, ax = plt.subplots(figsize=(14, 10))
    sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlGnBu', cbar_kws={'label': 'Precipitation (mm)'},
                linewidths=0.5, linecolor='gray', ax=ax)
    ax.set_xlabel('Month', fontweight='bold')
    ax.set_ylabel('Year', fontweight='bold')
    ax.set_title('Heatmap: Monthly Precipitation - Don Bosco, Villas de Andalucía', fontweight='bold', pad=20)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(os.path.join(PLOTS_DIR, save_path), dpi=PLOT_DPI, format='png', bbox_inches='tight')
    return fig


def plot_annual_boxplot(df: pd.DataFrame, date_col: str = 'date',
                        precip_col: str = 'precipitation_mm',
                        save_path: Optional[str] = None) -> plt.Figure:
    """Creates annual precipitation boxplot."""
    setup_style()
    ensure_plots_dir()
    
    df['year'] = pd.to_datetime(df[date_col]).dt.year
    years = sorted(df['year'].unique())
    data_list = [df[df['year'] == year][precip_col].dropna().values for year in years]
    
    fig, ax = plt.subplots(figsize=(16, 6))
    bp = ax.boxplot(data_list, labels=years, patch_artist=True)
    colors = plt.cm.viridis(np.linspace(0, 1, len(bp['boxes'])))
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Precipitation (mm)', fontweight='bold')
    ax.set_title('Precipitation Distribution by Year - Don Bosco, Villas de Andalucía', fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, axis='y')
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(os.path.join(PLOTS_DIR, save_path), dpi=PLOT_DPI, format='png', bbox_inches='tight')
    return fig


def plot_correlation_matrix(df: pd.DataFrame, variables: List[str],
                            title: str = "Correlation Matrix",
                            save_path: Optional[str] = None) -> plt.Figure:
    """Creates correlation matrix between variables."""
    setup_style()
    ensure_plots_dir()
    
    correlation_matrix = df[variables].dropna().corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8}, vmin=-1, vmax=1, ax=ax)
    ax.set_title(title, fontweight='bold', pad=20)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(os.path.join(PLOTS_DIR, save_path), dpi=PLOT_DPI, format='png', bbox_inches='tight')
    return fig


def plot_location_map(location: Optional[Dict] = None, save_path: Optional[str] = None) -> Optional[plt.Figure]:
    """Creates map showing the location of the study area."""
    if not CARTOPY_AVAILABLE:
        return None
    
    if location is None:
        location = LOCATION
    
    setup_style()
    ensure_plots_dir()
    
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)
    ax.add_feature(cfeature.LAND, alpha=0.5)
    ax.add_feature(cfeature.OCEAN, alpha=0.5)
    ax.plot(location['longitude'], location['latitude'], marker='o', markersize=15,
           color='red', transform=ccrs.PlateCarree(), label=location.get('name', 'Location'))
    ax.set_extent([-85, -75, 5, 12], crs=ccrs.PlateCarree())
    ax.set_title(f'Study Location: {location.get("name", "Don Bosco, Villas de Andalucía")}', fontweight='bold', pad=20, fontsize=14)
    ax.gridlines(draw_labels=True, alpha=0.5)
    ax.legend()
    plt.tight_layout()
    
    if save_path:
        plt.savefig(os.path.join(PLOTS_DIR, save_path), dpi=PLOT_DPI, format='png', bbox_inches='tight')
    return fig
