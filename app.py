import streamlit as st
import pandas as pd
import sweetviz as sv
import tempfile
import os

st.set_page_config(page_title="CSV Profiling App", layout="wide")
st.title("📊 CSV Data Profiling Web App")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.dataframe(df.head())

    st.info("🔎 Generating Data Profiling Report...")

    # SAFE MODE Sweetviz (prevents crash)
    report = sv.analyze(df, pairwise_analysis="off")

    tmp_dir = tempfile.mkdtemp()
    report_path = os.path.join(tmp_dir, "report.html")
    report.show_html(report_path, open_browser=False)

    with open(report_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=900, scrolling=True)
