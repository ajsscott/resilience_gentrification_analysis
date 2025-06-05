# Sample Input Data

This folder contains truncated, publicly shareable sample datasets used in the *NYC Green Gentrification* project. These files allow others to understand the data structure, explore the methodology, and test the codebase without requiring access to full proprietary or sensitive datasets.

## Files Included

### `sample_acs.csv`
- **Description**: Extract from the merged American Community Survey (ACS) dataset, combining multiple socio-economic indicators across NYC census tracts and years.
- **Fields** (representative): `GEOID`, `year`, `median_rent`, `education_rate`, `poverty_rate`, `population`, etc.
- **Source**: U.S. Census Bureau ACS 5-Year Estimates (2013–2023)

### `sample_tracts.csv`
- **Description**: Summary dataset for NYC census tracts used as the spatial unit of analysis in the tract-level panel.
- **Fields** (representative): `GEOID`, `borough`, `geometry`, `resilience_exposure`, `treated_year`, etc.
- **Source**: NYC Tiger Geospatial Data (2023 snapshot)

### `sample_evictions.csv`
- **Description**: Extract from NYC eviction filing records.
- **Fields**: `GEOID`, `year`, `eviction_count`, `eviction_rate`, etc.
- **Source**: NYC Open Data Eviction Dataset (2025 snapshot)

### `sample_resilience_projects.csv`
- **Description**: Resilience infrastructure project point data (location, type, and description).
- **Fields**: `project_name`, `agency`, `geometry`, `project_type`, `start_date`, etc.
- **Source**: NYC Recovery and Resiliency Project Database (2025 snapshot)

## ⚠️ Disclaimer

These datasets are samples for demonstration purposes only. They represent the schema and structure of the full analysis but may not contain statistically representative or complete records.

## 📌 Usage

These files are used in the early steps of the notebook workflows:
- `01_data-cleaning.ipynb`
- `02_eda.ipynb`
- `03_spatial-modeling.ipynb`

For full details on data preprocessing and modeling, see the top-level [README.md](../README.md) and the project [report](../../academic_report/StraumanScott_661_Resilience-Gentrification-NYC-report.pdf).
