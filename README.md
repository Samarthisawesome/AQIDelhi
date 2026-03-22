# AQI Tracker & Visualization

A Streamlit web application for exploring and visualizing Air Quality Index (AQI) data for New Delhi from 2020 to 2024.

## Features

- **Interactive Data Exploration** — Browse the raw dataset and view summary statistics via sidebar toggles.
- **Flexible Visualizations** — Plot any two numerical columns against each other using your choice of chart type.
- **Supported Plot Types:**
  - Scatter plot
  - Line chart
  - Bar chart
  - Histogram (with KDE overlay)
  - Box plot

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- pandas
- matplotlib
- seaborn

Install all dependencies with:

```bash
pip install streamlit pandas matplotlib seaborn
```

## Dataset

The app expects a CSV file at the following path relative to the project root:

```
AQIDelhi/delhi_combined.csv
```

Ensure the file exists and contains numerical columns representing AQI metrics before running the app.

## Usage

Run the app using the Streamlit CLI:

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

### Sidebar Controls

| Control | Description |
|---|---|
| Show Dataframe | Displays a preview of the full dataset |
| Show Summary Statistics | Shows descriptive statistics (mean, std, min/max, etc.) |
| Select X-axis | Choose the column for the X-axis |
| Select Y-axis | Choose the column for the Y-axis |
| Select plot type | Pick from scatter, line, bar, histogram, or boxplot |

## Project Structure

```
.
├── app.py               # Main Streamlit application
├── AQIDelhi/
│   └── delhi_combined.csv   # AQI dataset
└── README.md
```

## Notes

- Only numerical columns are available for axis selection. If no numerical columns are detected, a warning is displayed.
- For histogram and box plot types, only the X-axis selection is used.
