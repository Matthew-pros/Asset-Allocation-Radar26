import streamlit as st
from asset_radar.config import ASSETS
from asset_radar.data_loader import fetch_prices
from asset_radar.analytics import calculate_z_scores

st.title("📊 Asset Allocation Radar")

data = fetch_prices(ASSETS.keys(), years=5)
z_scores = calculate_z_scores(data)

st.dataframe(
    [{"Asset": ASSETS[k][0], "Z-Score": round(v,2)} for k,v in z_scores.items()]
)
