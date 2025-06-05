# Notebooks – NYC Resilience Gentrification Analysis

This folder contains the core computational notebooks used in the analysis of climate resilience projects and their relationship to gentrification and displacement risk in New York City. The workflow is organized chronologically and methodologically — from raw data merging to spatial econometric modeling.

---

## Overview of Workflow

### 00_acs_merge.ipynb
**Purpose**: Merge ACS (American Community Survey) datasets across years and variable groups.  
- Combines education, income, race, poverty, and rent data across 2013–2023.
- Reshapes wide-format ACS files into a long panel format by `GEOID` and `year`.
- Resulting output forms the socioeconomic base for all tract-level models.

### 01_data_cleaning.ipynb
**Purpose**: Clean and harmonize spatial, eviction, resilience project, and parcel datasets.  
- Spatial joins of PLUTO and ACRIS data by BBL.
- Mapping resilience points to census tracts.
- Creation of treatment indicators based on proximity to resilience projects and project year.

### 02_eda.ipynb
**Purpose**: Exploratory data analysis of ACS-eviction-resilience trends.  
- Visualizations of rent, poverty, and eviction distributions by resilience exposure.
- Moran's I tests and spatial autocorrelation diagnostics.
- Time-series plots to understand pre/post-treatment differences.

### 03_spatial_modeling.ipynb
**Purpose**: Estimate spatial error models (SEM) and test for resilience-driven gentrification spillovers.  
- Constructs spatial weight matrices (Queen contiguity).
- Runs SEM using PySAL’s GMM estimator.
- Evaluates rent and eviction response to resilience project exposure, accounting for spatial lag diffusion.
- Outputs include model coefficients, diagnostics, and residual spatial plots.

---

## Variable Engineering Highlights

- `treated`: Binary flag indicating post-resilience project exposure.
- `years_since_treatment`: Continuous time-since variable for temporal modeling.
- `eviction_rate`, `log_rent`, `poverty_rate`: Normalized outcome variables used in panel regressions.
- `W_log_rent`: Spatial lag of log median rent for SEM models.

---

## Execution Instructions

Run each notebook in order:

```bash
jupyter notebook 00_acs_merge.ipynb
# then
jupyter notebook 01_data_cleaning.ipynb
# then
jupyter notebook 02_eda.ipynb
# finally
jupyter notebook 03_spatial_modeling.ipynb
