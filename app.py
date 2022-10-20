# -*- coding: utf-8 -*-
import os
import requests
import json
import pandas as pd
import datetime
from datetime import date
from datetime import timedelta
import hvplot
import alpaca_trade_api as tradeapi
import pwinput
from termcolor import colored
import fire
import questionary

def run():
    """The main function for running the script."""

    print("Welcome to the Group 2 Project 2 machine learning project. This tool will show the practical uses of machine learning and artificial intelligence to predict a stock price on a specific date chosen by the user")
    print("\nTo use this service, you must have an Alpaca API and secrey key. You can sign up for one here [INSERT URL]")

    valid = False

    while valid == False:
        alpaca_api_key = pwinput.pwinput(prompt='\nPlease enter your Alpaca API Key: ', mask='*')
        alpaca_secret_key = pwinput.pwinput(prompt='\nPlease enter your Alpaca Secret Key: ', mask='*')

        if alpaca_api_key and alpaca_secret_key:
            print(colored('Keys accepted', 'green'))
            valid = True

    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version="v2")

    ticker = questionary.text("Please enter the desired ticker to evaluate:").ask()

    end_date_1 = datetime.date.today() - datetime.timedelta(days=1)
    start_date_1 = end_date_1 - datetime.timedelta(days=720)

    end_date = end_date_1.strftime('%Y-%m-%d')
    start_date = start_date_1.strftime('%Y-%m-%d')

    timeframe = "1Day"

    df = alpaca.get_bars(
        ticker,
        timeframe,
        start = start_date,
        end = end_date,
    ).df

    df.drop(['trade_count', 'vwap'], axis=1)

    print(f"\n{df}")


if __name__ == "__main__":
    fire.Fire(run)
