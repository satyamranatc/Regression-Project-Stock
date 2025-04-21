import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

DataFolder = os.listdir("./Data")
dfS = []

for D in DataFolder:
    dfS.append({
        "CompanyName": D.split("_")[0],
        "data":pd.read_csv("./Data/"+D)
    })



# Set page configuration
st.set_page_config(layout="wide", page_title="Stock Analysis Dashboard")
CompnayList = []
for i in dfS:
    CompnayList.append(i["CompanyName"])

CompnaySelected = st.multiselect("Select multiple:", CompnayList)

if len(CompnaySelected) <= 0:
    CompnaySelected.append("TSLA")


# Application title and description
st.title("Stock Market Analysis Dashboard")
st.markdown("### Analysis of AAPL, GS, TSLA, IBM, MSFT, GOOG, and JPM stocks")


for DataSet in dfS:
    if DataSet["CompanyName"] in CompnaySelected:
        st.markdown("### Analysis dashboard for: " + DataSet["CompanyName"])
        fig, ax = plt.subplots(figsize=(5, 3))  # Reduced size
        ax.scatter(DataSet["data"]["Open"], DataSet["data"]["Close"],alpha=0.7, c='#3B82F6')
        z = np.polyfit(DataSet["data"]["Open"], DataSet["data"]["Close"], 1)
        p = np.poly1d(z)
        ax.plot(DataSet["data"]["Open"], p(DataSet["data"]["Open"]), "r--", alpha=0.8)

        ax.set_title("Open Vs Close")
        ax.set_xlabel("Open")
        ax.set_ylabel("Close")


        st.pyplot(fig)
        st.table(DataSet["data"])
        st.markdown("---")

        OpenValue = st.number_input("Open Value For Predication: ")
        VolumeValue = st.number_input("Volume Value For Predication: ")
        st.button("Predict High")



st.markdown("---")
st.markdown("*Data source: CSV files in the Data directory*")
