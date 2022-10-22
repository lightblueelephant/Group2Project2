from flask import Flask, render_template, request, session, redirect
import os
import requests
import json
import pandas as pd
import datetime
from datetime import date
from datetime import timedelta
import alpaca_trade_api as tradeapi
from termcolor import colored
from finta import TA
from pandas.tseries.offsets import DateOffset
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
import hashlib
import streamlit as st

def predict_stock(ticker, api_key, secret_key):

    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version="v2")

        # end_date_1 = datetime.date.today() - datetime.timedelta(days=1)
        # start_date_1 = end_date_1 - datetime.timedelta(days=720)

        # end_date = end_date_1.isoformat()
        # start_date = start_date_1.isoformat()

    start_date = pd.Timestamp("2019-10-01", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2022-10-20", tz="America/New_York").isoformat()


    timeframe = "1Day"

    df = alpaca.get_bars(
        ticker,
        timeframe,
        start = start_date,
        end = end_date,
    ).df

    # return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

        #create OHLCV df; drop 'trade_count' and 'vwap'columns
    df = df.drop(['trade_count', 'vwap'], axis=1)

    # Use the pct_change function to generate the returns from "close"
    df["actual_returns"] = df["close"].pct_change()

    # Drop all NaN values from the DataFrame
    df = df.dropna()

    # Generate the Input Features, X
    # Create additional technical indicators
    df['sma_slow'] = TA.SMA(df, 100)
    df['sma_fast'] = TA.SMA(df, 4)
    df["ssma"] = TA.SSMA(df)
    df["ema"] = TA.EMA(df, 50)
    df["dema"] = TA.DEMA(df)
    df["tema"] = TA.TEMA(df)
    df["trima"] = TA.TRIMA(df)
    df["trix"] = TA.TRIX(df)
    df["vama"] = TA.VAMA(df)
    df["kama"] = TA.KAMA(df)
    df["zlema"] = TA.ZLEMA(df)
    df["wma"] = TA.WMA(df)

    df = df.dropna()

    # Assign a copy of the technical variable columns to a new DataFrame called `X` and shift values.
    # The shifted 'X' values will align a prior day's X values with the next day's 'y'/returns/trading signal,
    # to train the predictive model. 
    X = df[['sma_slow', 'sma_fast', 'ssma', 'ema', 'dema', 'tema', 'trima', 'trix', 'vama', 'kama', 'zlema', 'wma']].shift().dropna().copy()

    # Initialize a `signal` column
    df['signal'] = 0.0

    # signal values will be based on the daily returns: positive returns yield '1', negative returns '-1'
    df.loc[(df['actual_returns'] >= 0), 'signal'] = 1
    df.loc[(df['actual_returns'] < 0), 'signal'] = -1

    # Copy the 'signal' column to a new Series called `y`.
    y = df['signal']
    # return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

    cum_returns = {}
    for i in range(1,100):

        training_begin = X.index.min()
        training_end = X.index.min() + DateOffset(weeks=i)
        
        # Slice the 'X' dataframe and 'y' Series into congruous training datasets.
        X_train = X.loc[training_begin:training_end]
        y_train = y.loc[training_begin:training_end]

    # Slice the testing 'X' and 'y' datasets, starting from the end of the training data until the most recent index. 
        X_test = X.loc[training_end:]
        y_test = y.loc[training_end:]

    # Use StandardScaler to scale the X_train and X_test data.
        scaler = StandardScaler()
        X_scaler = scaler.fit(X_train)
        X_train_scaled = X_scaler.transform(X_train)
        X_test_scaled = X_scaler.transform(X_test)
        
        lrm=LogisticRegression()
        lrm.fit(X_train_scaled, y_train)
        testing_predictions = lrm.predict(X_test_scaled)
        
        lr_predictions_df = pd.DataFrame(index=X_test.index)
        lr_predictions_df['predicted_returns'] = testing_predictions

    # Add in actual returns and calculate trading returns
        lr_predictions_df['actual_returns'] = df['actual_returns']
        lr_predictions_df['trading_algorithm_returns'] = lr_predictions_df['actual_returns'] * lr_predictions_df['predicted_returns']
        lr_predictions_df['actual_cumulative'] = (1 + lr_predictions_df['actual_returns']).cumprod()
        lr_predictions_df['algo_cumulative'] = (1 + lr_predictions_df['trading_algorithm_returns']).cumprod()

        final_result_actual = lr_predictions_df['actual_cumulative'][df.index[-1]]
        final_result_algo = lr_predictions_df['algo_cumulative'][df.index[-1]]
            
            
        if final_result_algo > final_result_actual:
            cum_returns[i] = final_result_algo

    max_value = max(cum_returns, key=cum_returns.get)

    training_begin = X.index.min()
    training_end = X.index.min() + DateOffset(weeks=max_value)
        

    X_train = X.loc[training_begin:training_end]
    y_train = y.loc[training_begin:training_end]


    X_test = X.loc[training_end:]
    y_test = y.loc[training_end:]


    scaler = StandardScaler()
    X_scaler = scaler.fit(X_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
        
    lrm=LogisticRegression()
    lrm.fit(X_train_scaled, y_train)
    testing_predictions = lrm.predict(X_test_scaled)

    if testing_predictions[-1] > 0:
        result = "This stock is predicted to increase in value. It's a recommended buy."
    else:
        result = "This stock is predicted to decrease in value. It's recommended to sell or short."

    return result
################################################################################
# Streamlit Code


# Create the application header using a markdown string
st.markdown("Get A Buy/Sell Recommendation On A Stock")

################################################################################
# Step 2:
# Add a Streamlit `text_area` component to accept data from the user.

# @TODO:
# Add a Streamlit `text_area` component to accept data from the user
# Be sure to convert the input data to a string
# Use the `encode` function to encode the input data
ticker = str(st.text_area("Enter Stock Ticker"))
alpaca_api_key = str(st.text_area("Enter Alpaca API Key"))
alpaca_secret_key = str(st.text_area("Enter Alpaca API Secret Key"))

# @TODO:
# Use the Streamlit `write` function to display the length (`len) of the input
# data back to the user

if st.button("Make Recommendation"):
    recommendation = predict_stock(ticker, alpaca_api_key, alpaca_secret_key)
    st.write(recommendation)


