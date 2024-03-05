import streamlit as st
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

st.set_page_config(page_title="Dashboard Brazil E-Commerce")

st.header("Dashboard Brazil E-Commerce")

st.subheader("Quetion Goals")
st.markdown("""

- Viewing the percentage of payment types made by Users.
- Viewing the top 10 cities with the highest orders each year.
- Viewing the growth of orders each month throughout the year.

""")

tab1, tab2, tab3 = st.tabs(["Quetions 1", "Quetions 2", "Quetions 3"])

with tab1:
    st.subheader("Viewing the percentage of payment types made by Users.")
    st.image("image/visualize_quetion_1.png", use_column_width=True)

with tab2:
    st.subheader("Viewing the top 10 cities with the highest orders each year.")
    st.image("image/visualize_quetion_2_fullData.png", use_column_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 10 Cities in 2016")
        st.image("image/visualize_quetion_2_2016.png", use_column_width=True)

    with col2:
        st.markdown("### 10 Cities in 2017")
        st.image("image/visualize_quetion_2_2017.png", use_column_width=True)

    st.divider()

    st.markdown("### 10 Cities in 2018")
    st.image("image/visualize_quetion_2_2018.png", use_column_width=True)

with tab3:
    st.subheader("Viewing the growth of orders each month throughout the year.")
    st.image("image/visualize_quetion_3.png", use_column_width=True)

st.divider()

st.subheader("Other Visualize")
with st.expander("Other Visualize"):
    
    st.subheader("Geolocation Order Customer")
    st.image("image/geolocation.png", use_column_width=True)

    st.divider()

    st.subheader("Correlation (price & freight_value & size_of_product)")
    st.image("image/correlation_full.png", use_column_width=True)