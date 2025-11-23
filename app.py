import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

st.set_page_config(page_title="CSV Profiling App", layout="wide")
st.title("📊 CSV Profiling Web App")

uploaded_file = st.file_uploader("CSV file upload karo", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    profile = ProfileReport(df, title="Profiling Report", explorative=True)
    report_html = profile.to_html()

    html(report_html, height=800, scrolling=True)