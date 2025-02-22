import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objs as go
import yfinance as yf
# Set page title
st.set_page_config(page_title='Crypto Prediction App',page_icon=":chart_with_upwards_trend:")
# Define function to get stock data
@st.cache
def load_data(ticker):
    data = yf.download(ticker, start='2023-01-01')
    return data
# Define function to make stock predictions
@st.cache
# Define function to make stock predictions
@st.cache
# Define function to make stock predictions
@st.cache
def make_prediction(data, years):
    # Rename columns to fit Prophet format
    data = data[['Close']]
    data = data.rename(columns={'Close': 'y'})
    data['ds'] = data.index

    # Train Prophet model
    model = Prophet()
    model.fit(data)

    # Make predictions
    future = model.make_future_dataframe(periods=365*years)
    forecast = model.predict(future)

    # Get last date and prediction for that date
    last_date = forecast['ds'].iloc[-1]
    prediction = forecast.loc[forecast['ds'] == last_date, 'yhat'].iloc[0]

    return prediction


# Define Streamlit app


# Define Streamlit app
# Define Streamlit app
def main():
    # Set app title
    st.title('Crypto Prediction')

    # Get user input
    stocks = (  'RVN-INR', 'CHZ-INR', 'MATIC-INR', 'ALGO-INR',  'DASH-INR', 'BTG-INR', 'KAVA-INR', 'ZIL-INR','BTC-INR', 'ETH-INR', 'ADA-INR', 'BNB-INR', 'XRP-INR')
    ticker = st.selectbox("Select dataset for prediction", stocks)
    years = st.slider('Select number of years to predict', min_value=1, max_value=10, value=2)

    # Load data
    data = load_data(ticker)

    # Display data
    st.subheader('Historical Data')
    st.write(data)

    # Make prediction
    prediction = make_prediction(data, years)

    # Display prediction
    st.subheader(f'Predicted closing price for {ticker} on the last day of {years} years from now')
    st.write(f'Predicted closing price: {round(prediction, 2)}')

    
# Run the app
if __name__ == '__main__':
    main()
