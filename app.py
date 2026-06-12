import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

st.set_page_config(
    page_title="Retail Visitor Analytics",
    layout="wide"
)

st.title("🏬 Retail Visitor Analytics Dashboard")

# ==========================
# Load Data
# ==========================

visitor_total = pd.read_parquet(
    r"C:\uas-tbg\output\visitor_total\visitor_total.parquet"
)

visitor_time = pd.read_parquet(
    r"C:\uas-tbg\output\visitor_time\visitor_time.parquet"
)

ml_data = pd.read_parquet(
    r"C:\uas-tbg\output\ml_visitor\ml_visitor.parquet"
)

# ==========================
# KPI
# ==========================

total_visitors = visitor_total["total_visitors"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Visitors",
        int(total_visitors)
    )

with col2:
    st.metric(
        "Total Zones",
        len(visitor_total)
    )

# ==========================
# Zone Filter
# ==========================

selected_zone = st.selectbox(
    "Select Zone",
    visitor_total["zone"].unique()
)

# ==========================
# Visitor Per Zone
# ==========================

st.subheader("Total Visitors by Zone")

fig_zone = px.bar(
    visitor_total,
    x="zone",
    y="total_visitors"
)

st.plotly_chart(
    fig_zone,
    use_container_width=True
)

# ==========================
# Trend Chart
# ==========================

st.subheader("Visitor Trend per 15 Minutes")

filtered = visitor_time[
    visitor_time["zone"] == selected_zone
]

fig_trend = px.line(
    filtered,
    x="time_block",
    y="avg_visitors",
    markers=True
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)

# ==========================
# ML Prediction
# ==========================

st.subheader("Visitor Prediction")

with open(
    r"C:\uas-tbg\output\visitor_model.pkl",
    "rb"
) as f:
    model = pickle.load(f)

hour = st.slider(
    "Select Hour",
    0,
    23,
    12
)

prediction = model.predict([[hour]])

st.success(
    f"Predicted Visitors at Hour {hour}: {int(prediction[0])}"
)

# ==========================
# Peak Hour Analysis
# ==========================

st.subheader("Peak Hour Analysis")

peak_hour = (
    ml_data.groupby("hour")["visitor_count"]
    .mean()
    .idxmax()
)

st.info(
    f"Peak Visitor Hour: {peak_hour}:00"
)