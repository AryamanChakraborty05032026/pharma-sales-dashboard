# 📊 Pharmaceutical Sales Analytics Dashboard

An interactive data visualization platform built with Python and Streamlit to analyze pharmaceutical sales trends. This project transforms raw transactional data into actionable insights, tracking drug category performance across various time granularities.

## 🚀 Key Features
Multi-Level Granularity: Toggle between Hourly, Daily, Weekly, and Monthly views to observe sales patterns at different scales.

ATC Category Tracking: Specialized monitoring for key drug classifications:

   -> M01AB/M01AE: Anti-inflammatory and antirheumatic products.

   -> N02BA/N02BE: Analgesics and antipyretics.

   -> R03/R06: Drugs for obstructive airway diseases and antihistamines.

Seasonality Insights: Automated analysis of Respiratory drugs (R03) to identify peak sales months and seasonal demand.

Historical Deep-Dive: Dedicated logic to identify top-performing drug categories for specific years, such as the 2017 sales peak.

## 🔗 Data Source
The datasets used in this project are sourced from [Pharmaceutical Sales Data](https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data) on Kaggle. It represents 6 years of transactional data from a pharmacy, classified using the Anatomical Therapeutic Chemical (ATC) classification system.

##  Files
| File | Description |
|------|-------------|
| `app.py` | The core Streamlit application containing the dashboard logic. |
| `salesdaily.csv` | Dataset containing daily sales data. |
| `saleshourly.csv` | Dataset containing hourly sales data. |
| `salesweekly.csv` | Dataset containing weekly sales data. |
| `salesmonthly.csv` | Dataset containing monthly sales data. |
| `Pharma_sales_data_kaggle.ipynb` | Jupyter Notebook used for initial data exploration and prototyping. |

##  How to Run
Follow these steps to launch the dashboard on your local machine:

1. Open your Terminal
   Navigate to your project folder on the desktop:
```
  cd C:\Users\baymax\Desktop\pharma-sales-dashboard
```

2. Install Dependencies
   Run the following command to install the required libraries:
```
   pip install pandas matplotlib streamlit
```

3. Launch the Application
   Start the Streamlit server to view the dashboard:
```
   python -m streamlit run app.py
```

##  Requirements
- pandas
- matplotlib
- streamlit
