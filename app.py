import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Make plots look nicer
plt.style.use("seaborn-v0_8")

ATC_COLS = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]

@st.cache_data
def load_data():
    # Adjust paths if your files are elsewhere
    hourly = pd.read_csv("saleshourly.csv")
    daily = pd.read_csv("salesdaily.csv")
    weekly = pd.read_csv("salesweekly.csv")
    monthly = pd.read_csv("salesmonthly.csv")

    # Convert date columns
    for df in [hourly, daily, weekly, monthly]:
        if "datum" in df.columns:
            df["datum"] = pd.to_datetime(df["datum"], dayfirst=True, errors="coerce")

    return hourly, daily, weekly, monthly


def main():
    st.title("Pharmaceutical Sales Analytics Dashboard")

    st.sidebar.header("Controls")
    granularity = st.sidebar.selectbox(
        "Select data granularity",
        ["Daily", "Weekly", "Monthly", "Hourly"],
        index=0,
    )

    hourly, daily, weekly, monthly = load_data()

    if granularity == "Daily":
        df = daily.copy()
    elif granularity == "Weekly":
        df = weekly.copy()
    elif granularity == "Monthly":
        df = monthly.copy()
    else:
        df = hourly.copy()

    st.write(f"### Using {granularity.lower()} data")
    st.write("Showing first few rows of the selected dataset:")
    st.dataframe(df.head())

    # --- 1. Total sales quantities for each drug category (ATC) ---
    st.subheader("Total Sales by Drug Category (ATC)")

    # Some files may not have all ATC columns; keep only those that exist
    used_atc_cols = [c for c in ATC_COLS if c in df.columns]

    totals = df[used_atc_cols].sum().sort_values(ascending=False)
    st.write("Total quantity sold per ATC category (over the whole period):")
    st.write(totals)

    st.bar_chart(totals)

    # --- 2. Highest average daily sales by category (use daily data) ---
    st.subheader("Average Daily Sales by ATC Category")

    if not daily.empty:
        daily_atc_cols = [c for c in ATC_COLS if c in daily.columns]
        avg_daily = daily[daily_atc_cols].mean().sort_values(ascending=False)
        st.write("Average daily quantity sold per ATC category:")
        st.write(avg_daily)
        st.bar_chart(avg_daily)
    else:
        st.info("Daily dataset is empty or missing; cannot compute daily averages.")

    # --- 3. Which ATC 'drug' was sold most in 2017 (using daily data) ---
    st.subheader("Most Sold Drug Category in 2017 (Daily Data)")

    if "datum" in daily.columns:
        daily_2017 = daily[daily["datum"].dt.year == 2017]
        if not daily_2017.empty:
            atc_2017 = daily_2017[[c for c in ATC_COLS if c in daily_2017.columns]].sum()
            top_atc_2017 = atc_2017.idxmax()
            st.write("Total quantities per ATC in 2017:")
            st.write(atc_2017.sort_values(ascending=False))
            st.success(f"Drug category with highest total sales in 2017: **{top_atc_2017}**")
        else:
            st.info("No daily data for 2017 in the dataset.")
    else:
        st.info("No 'datum' column in daily data; cannot filter by year.")

    # --- 4. Are respiratory drugs (R03) sold more during specific months? (monthly data) ---
    st.subheader("Seasonality of Respiratory Drugs (R03)")

    if "R03" in monthly.columns and "datum" in monthly.columns:
        monthly_r03 = monthly.copy()
        monthly_r03["month"] = monthly_r03["datum"].dt.month
        r03_by_month = monthly_r03.groupby("month")["R03"].sum()

        st.write("Total R03 quantity by calendar month (1 = January, ..., 12 = December):")
        st.write(r03_by_month)

        fig, ax = plt.subplots(figsize=(8, 4))
        r03_by_month.plot(kind="bar", ax=ax)
        ax.set_xlabel("Month")
        ax.set_ylabel("Total R03 quantity")
        ax.set_title("Monthly Sales of Respiratory Drugs (R03)")
        st.pyplot(fig)
    else:
        st.info("Monthly data does not contain 'R03' or 'datum' columns.")

    st.write("---")
    st.caption("Data source: Pharma sales dataset (resampled hourly, daily, weekly, monthly).")


if __name__ == "__main__":
    main()