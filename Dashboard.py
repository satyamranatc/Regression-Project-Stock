import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression

from ApiData import GetData

class StockMarketAnalysis:
    def __init__(self):
        # GetData()
        if not os.path.exists("./Data"):
            os.makedirs("./Data")
        DataFolder = os.listdir("./Data")
        self.dfS = []

        for D in DataFolder:
            self.dfS.append({
                "CompanyName": D.split("_")[0],
                "data": pd.read_csv("./Data/"+D)
            })

        st.set_page_config(layout="wide", page_title="Stock Analysis Dashboard")
        self.CompnayList = [i["CompanyName"] for i in self.dfS]
        CompnaySelected = st.multiselect("Select multiple:", self.CompnayList)
        if len(CompnaySelected) == 0:
            CompnaySelected = ["TSLA"]
        self.CompnaySelected = CompnaySelected

    def Start(self):
        # Application title and description
        st.title("Stock Market Analysis Dashboard")
        st.markdown("### Analysis of AAPL, GS, TSLA, IBM, MSFT, GOOG, and JPM stocks")


        for DataSet in self.dfS:
            if DataSet["CompanyName"] in self.CompnaySelected:
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

                X = DataSet["data"][["Open","Close","Low","Volume"]]
                y = DataSet["data"]["High"]
                
                model = LinearRegression()
                model.fit(X,y)      

                OpenValue = st.number_input("Open Value For Predication: ")
                CloseValue = st.number_input("Close Value For Predication: ")
                LowValue = st.number_input("Low Value For Predication: ")
                VolumeValue = st.number_input("Volume Value For Predication: ")

                def Predict():
                    result = model.predict([[OpenValue,CloseValue,LowValue,VolumeValue]])
                    st.write(result)

                st.button("Predict High",on_click=Predict)




        st.markdown("---")
        st.markdown("*Data source: CSV files in the Data directory*")



SMA = StockMarketAnalysis()
SMA.Start()