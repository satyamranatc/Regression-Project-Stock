import requests
import pandas as pd

Companies = ["GOOG","MSFT","AAPL","JPM","IBM","GS","TSLA","AMZN"]


for Company in Companies:
    # API URL
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={Company}&interval=5min&apikey=O6DMM9OMXYOG6E9V&#39;"

    # Get the data
    r = requests.get(url)
    data = r.json()
    # print(data)

    # Extract the time series data
    time_series = data["Time Series (5min)"]
    time_series

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')

    # Optional: Rename columns for better readability
    df.columns = ["Open", "High", "Low", "Close", "Volume"]

    # Convert the index to datetime format
    df.index = pd.to_datetime(df.index)

    # Sort the data by datetime (ascending)
    df = df.sort_index()

    # Display the DataFrame
    # print(df)


    df.to_csv(f"./Data/{Company}_STOCK_DATA.csv",index=False)