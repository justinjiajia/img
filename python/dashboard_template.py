import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Load stock data
@st.cache_data
def load_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

# Default settings
DEFAULT_TICKERS = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
CURRENT_YEAR = datetime.today().year

# Configure page
st.title("Simple Stock Performance Dashboard 📊")

# Sidebar controls
# Provide your code to create a sidebar with controls
# Save the selected tickers and year range 
# with the variables selected_tickers and selected_years






# Convert years to datetime objects
start_date = datetime(selected_years[0], 1, 1)
end_date = datetime(selected_years[1], 12, 31)

# Load data
data = load_data(selected_tickers, start_date, end_date)


# Main dashboard
# Provide your code to create the main dashboard
# The moving average data can be generated with 
# data['Close'].rolling(ma_days).mean() 
# where ma_days is the variable that stores
# the user's selection of the moving average period (days) from a slider widget


# How to compute the 2 key statsitcs
# annual_returns = data['Close'].pct_change(365).iloc[-1].mean() * 100
# volatility = data['Close'].pct_change().std().mean() * 100
# Use st.metric() to display the annual returns and volatility
# https://docs.streamlit.io/develop/api-reference/data/st.metric





# Data download
st.sidebar.download_button(
    "Download Closing Prices",
    data = data['Close'].to_csv().encode('utf-8'),
    file_name = 'stock_prices.csv',
    mime='text/csv'
)