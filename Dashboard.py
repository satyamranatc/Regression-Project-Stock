import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

DataFolder = os.listdir("./Data")
dfS = []

for D in DataFolder:
    dfS.append({
        "CompanyName": D.split("_")[0],
        "data":pd.read_csv("./Data/"+D)
    })



# Set page configuration
st.set_page_config(layout="wide", page_title="Stock Analysis Dashboard")

# Application title and description
st.title("Stock Market Analysis Dashboard")
st.markdown("### Analysis of AAPL, GS, TSLA, IBM, MSFT, GOOG, and JPM stocks")



for DataSet in dfS:
    st.markdown("### Analysis dashboard for: "+DataSet["CompanyName"])
    fig,ax = plt.subplots()
    ax.scatter(DataSet["data"]["Open"], DataSet["data"]["Close"], label="Sine Wave")
    ax.set_title("Sine Curve")
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    st.pyplot(fig)
    st.markdown("---")



st.markdown("---")
st.markdown("*Data source: CSV files in the Data directory*")