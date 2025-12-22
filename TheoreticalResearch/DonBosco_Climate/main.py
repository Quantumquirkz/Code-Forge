"""
Main script for climate analysis of Don Bosco, Villas de Andalucía.
Studies climate behavior and precipitation variations (2000-2025).
"""

import sys
from datetime import datetime
from config import START_YEAR, END_YEAR, LOCATION, PROCESSED_DATA_DIR, PLOTS_DIR

# Import consolidated modules
from climate_data import (
    fetch_noaa_data, fetch_enso_indices, clean_climate_data,
    aggregate_to_monthly, save_data, calculate_statistics,
    calculate_precipitation_trends, detect_anomalies_zscore,
    correlate_with_enso, detect_drought_periods, calculate_annual_statistics
)
from visualization import (
    plot_time_series, plot_precipitation_anomalies, plot_enso_correlation,
    plot_heatmap_monthly_precipitation, plot_annual_boxplot,
    plot_correlation_matrix, plot_location_map
)


def main():
    """Main function."""
    print("=" * 80)
    print("CLIMATE ANALYSIS: DON BOSCO, VILLAS DE ANDALUCÍA (2000-2025)")
    print("=" * 80)
    print(f"\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Location: {LOCATION['name']} ({LOCATION['latitude']}, {LOCATION['longitude']})")
    print(f"Period: {START_YEAR} - {END_YEAR}\n")
    
    # Step 1: Data collection and processing
    print("-" * 80)
    print("STEP 1: DATA COLLECTION AND PROCESSING")
    print("-" * 80)
    
    print("\n1.1. Downloading climate data...")
    df_climate = fetch_noaa_data(START_YEAR, END_YEAR, LOCATION)
    print(f"    ✓ {len(df_climate)} daily records")
    
    print("\n1.2. Downloading ENSO indices...")
    df_enso = fetch_enso_indices(START_YEAR, END_YEAR)
    print(f"    ✓ {len(df_enso)} monthly records")
    
    print("\n1.3. Cleaning and processing data...")
    df_clean = clean_climate_data(df_climate)
    df_monthly = aggregate_to_monthly(df_clean)
    print(f"    ✓ {len(df_clean)} clean daily records")
    print(f"    ✓ {len(df_monthly)} monthly records")
    
    print("\n1.4. Saving processed data...")
    save_data(df_clean, "climate_data_daily")
    save_data(df_monthly, "climate_data_monthly")
    save_data(df_enso, "enso_indices")
    print("    ✓ Data saved")
    
    # Step 2: Statistical analysis
    print("\n" + "-" * 80)
    print("STEP 2: STATISTICAL ANALYSIS")
    print("-" * 80)
    
    print("\n2.1. Basic statistics...")
    stats_precip = calculate_statistics(df_monthly, 'precipitation_mm')
    print(f"    ✓ Average precipitation: {stats_precip['mean']:.2f} mm/month")
    print(f"    ✓ Standard deviation: {stats_precip['std']:.2f} mm")
    print(f"    ✓ Range: {stats_precip['min']:.2f} - {stats_precip['max']:.2f} mm")
    
    print("\n2.2. Trend analysis...")
    trends = calculate_precipitation_trends(df_monthly)
    print(f"    ✓ Total change: {trends['change_total_percent']:.2f}%")
    print(f"    ✓ Annual change: {trends['change_per_year_percent']:.2f}%/year")
    print(f"    ✓ R²: {trends['r_squared']:.4f}, p-value: {trends['p_value']:.4e}")
    
    print("\n2.3. Anomaly detection...")
    df_anomalies = detect_anomalies_zscore(df_monthly, 'precipitation_mm')
    n_anomalies = df_anomalies['anomaly_zscore'].sum()
    print(f"    ✓ Anomalies detected: {n_anomalies} ({100*n_anomalies/len(df_anomalies):.1f}%)")
    
    print("\n2.4. ENSO correlation...")
    enso_corr = correlate_with_enso(df_monthly, df_enso, 'precipitation_mm')
    print(f"    ✓ ONI correlation: {enso_corr['correlation']:.4f}")
    print(f"    ✓ p-value: {enso_corr['p_value']:.4f}")
    
    print("\n2.5. Drought detection...")
    df_drought = detect_drought_periods(df_monthly)
    n_drought = df_drought['drought'].sum()
    print(f"    ✓ Drought months: {n_drought} ({100*n_drought/len(df_drought):.1f}%)")
    
    # Step 3: Visualization
    print("\n" + "-" * 80)
    print("STEP 3: VISUALIZATION")
    print("-" * 80)
    
    plot_files = []
    
    print("\n3.1. Time series...")
    plot_time_series(df_monthly, 'date', 'precipitation_mm',
                    title='Monthly Precipitation - Don Bosco, Villas de Andalucía (2000-2025)',
                    ylabel='Precipitation (mm)', save_path='precipitacion_temporal.png')
    plot_files.append('precipitacion_temporal.png')
    
    print("3.2. Anomalies...")
    plot_precipitation_anomalies(df_monthly, save_path='anomalias_precipitacion.png')
    plot_files.append('anomalias_precipitacion.png')
    
    print("3.3. Monthly heatmap...")
    plot_heatmap_monthly_precipitation(df_monthly, save_path='heatmap_precipitacion_mensual.png')
    plot_files.append('heatmap_precipitacion_mensual.png')
    
    print("3.4. Annual boxplot...")
    plot_annual_boxplot(df_monthly, save_path='boxplot_precipitacion_anual.png')
    plot_files.append('boxplot_precipitacion_anual.png')
    
    print("3.5. ENSO correlation...")
    plot_enso_correlation(df_monthly, df_enso, save_path='correlacion_enso.png')
    plot_files.append('correlacion_enso.png')
    
    print("3.6. Location map...")
    fig = plot_location_map(save_path='ubicacion_panama.png')
    if fig is not None:
        plot_files.append('ubicacion_panama.png')
    
    if 'temperature_avg_c' in df_monthly.columns:
        print("3.7. Correlation matrix...")
        variables = ['precipitation_mm', 'temperature_avg_c']
        if 'temperature_max_c' in df_monthly.columns:
            variables.append('temperature_max_c')
        plot_correlation_matrix(df_monthly, variables,
                               title='Correlation between Climate Variables',
                               save_path='matriz_correlacion.png')
        plot_files.append('matriz_correlacion.png')
    
    print(f"\n    ✓ {len(plot_files)} plots generated")
    
    # Final summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ Data: {len(df_monthly)} monthly records processed")
    print(f"✓ Plots: {len(plot_files)} generated")
    print(f"✓ Trend: {trends['change_total_percent']:.2f}% ({'Significant' if trends['p_value'] < 0.05 else 'Not significant'})")
    print(f"✓ Files: {PROCESSED_DATA_DIR}/ and {PLOTS_DIR}/")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
