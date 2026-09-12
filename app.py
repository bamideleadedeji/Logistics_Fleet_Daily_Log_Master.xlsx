import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Logistics & Delivery Fleet Dispatch Suite",
    page_icon="🚚",
    layout="wide",
)

st.title("🚚 International Logistics & Delivery Fleet Audit Suite")
st.caption(
    "Interactive Web Engine | Built for Dispatch Operators, Mini-Fleets &"
    " Couriers"
)

# Sidebar - Sales & Monetization CTA
st.sidebar.header("🚀 Get the Full Master Template")
st.sidebar.info(
    "Need the offline Excel & Google Sheets master file with automated"
    " P&L formulas?"
)
st.sidebar.markdown(
    "[👉 Buy Master Template on"
    " Gumroad](https://bamidele38.gumroad.com/l/sme-daily-tracker)"
)

# Session State Initializer
if "df_fleet" not in st.session_state:
  st.session_state.df_fleet = pd.DataFrame({
      "Trip ID": ["TRP-001", "TRP-002", "TRP-003", "TRP-004"],
      "Driver Name": ["John Miller", "John Miller", "David Chen", "David Chen"],
      "Vehicle ID": ["Van-01", "Van-01", "Bike-02", "Bike-02"],
      "Origin": [
          "Central Hub",
          "North District",
          "Metro Station",
          "West Suburb",
      ],
      "Destination": [
          "North District",
          "East Terminal",
          "West Suburb",
          "Central Hub",
      ],
      "Delivery Fee ($)": [45.0, 35.0, 25.0, 20.0],
      "COD Collected ($)": [250.0, 0.0, 120.0, 0.0],
      "Fuel Expense ($)": [15.0, 10.0, 8.0, 5.0],
      "Tolls / Expenses ($)": [5.0, 0.0, 2.5, 0.0],
  })

# 1. Interactive Transaction Log
st.subheader("1. Daily Dispatch & Expense Tracker")
st.write(
    "Edit trips, fuel allocations, and COD amounts directly in the table below:"
)

edited_df = st.data_editor(
    st.session_state.df_fleet, num_rows="dynamic", use_container_width=True
)

# Calculations
edited_df["Net Remittance ($)"] = (
    edited_df["Delivery Fee ($)"]
    + edited_df["COD Collected ($)"]
    - (edited_df["Fuel Expense ($)"] + edited_df["Tolls / Expenses ($)"])
)

# 2. Executive Summary Metrics
st.markdown("---")
st.subheader("2. Fleet Remittance & Financial Audit")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Delivery Fees", f"${edited_df['Delivery Fee ($)'].sum():,.2f}")
col2.metric(
    "Total Cash On Delivery (COD)", f"${edited_df['COD Collected ($)'].sum():,.2f}"
)
col3.metric("Total Fuel Spent", f"${edited_df['Fuel Expense ($)'].sum():,.2f}")
col4.metric(
    "Net Office Remittance", f"${edited_df['Net Remittance ($)'].sum():,.2f}"
)

# 3. Visualization
st.markdown("---")
st.subheader("3. Expense vs. Revenue by Vehicle")
fig = px.bar(
    edited_df,
    x="Vehicle ID",
    y=["Delivery Fee ($)", "Fuel Expense ($)"],
    barmode="group",
    title="Revenue vs Fuel Allowance per Vehicle",
)
st.plotly_chart(fig, use_container_width=True)
