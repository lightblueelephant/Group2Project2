# Stock Signal Predictor

This program uses machine learning to try to predict the future movement of an individual stock. The program uses two years of historcal stock data to train a predictive model. The user inputs their stock ticker and the program outputs a prediction for the user to either buy if the stock is predicted to increase in price or to short it if it's predicted to decrease in price.

---

## Technologies

This application is compatible with Python 3.9.

The OS, Requests, JSON, Pandas, datetime, hvplot and FinTA libraries were used along with matplotlib and must be installed in order to run the program correctly. Stock data will be pulled from Alpaca so the user will need to install the Alpaca API. The Scikit-learn and imbalanced-learn libraries will have to be installed for machine learning.

OS provides a way to use operating system dependent functionality such as command line operations.

Requests allows the program a simple way to send http requests.

JSON is used for encoding and decoding JSON data in a Python environment.

Pandas is used for data science and analysis and machine learning.

datetime is used to classify specific date and time information, especially when relating to timezones, DST and microsecond timing.

hvpolt is used for visualizing robust and interactive data plots and graphs.

FinTA can be used to run over 80 trading indicators through datasets for analysis.

Matplotlib allows for the visualization of data in the form of plots and graphs.

Scikit-learn implements machine learning and is a simple and efficient tool for predictive data analysis. Imbalanced-learn is used along with Scikit-learn to help process imbalanced datasets.

The Alpaca API allows the program to access historical or real-time stock market data.

This program will work on Windows, MacOS and Linux with Python 3.9 installed. The program is a Jupyter Notebook and the user will need to run the program in a code editor such as Juypter Lab or Visual Studio Code.

## Links to Documentation

Documentation for the OS library can be found [here.](https://docs.python.org/3/library/os.html)

Documentation for the Requests library can be found [here.](https://requests.readthedocs.io/en/latest/)

Documentation for the JSON library can be found [here.](https://docs.python.org/3/library/json.html)

Documentation for the Pandas library can be found [here.](https://pandas.pydata.org/docs/)

Documentation for the datetime library can be found [here.](https://docs.python.org/3/library/datetime.html)

Documentation for the hvplot library can be found [here.](https://hvplot.holoviz.org/user_guide/index.html)

Documentation for the FinTA library can be found [here.](https://openbase.com/python/finta)

Documentation for matplotlib can be found [here.](https://matplotlib.org/stable/users/index)

Documentation for the Alpaca API can be found [here.](https://alpaca.markets/deprecated/docs/api-documentation/)

Documentation for Scikit-Learn can be found [here.](https://scikit-learn.org/stable/user_guide.html)

Documentation for Imbalanced-learn can be found [here.](https://imbalanced-learn.org/stable/user_guide.html)

---

## Installation Guide

You must install the following libraries and dependencies before running the program.

To install the pathlib, pandas and matplotlib libraries type the following into your CLI:

```
python
-m pip install requests
pip install pandas
pip install hvplot
pip install finta
pip install -U matplotlib
pip install alpaca-py
pip install -U scikit-learn
pip install -U imbalanced-learn
```
---

## Usage

Clone or download the files from the Github repository.

To run the program open your code editor and navigate to the folder containing the file "shared_notebook.ipynb".

In cell 4, input the stock ticker you want to use.

Run the cells in sequence from top to bottom.

The output displays a recommendation based on the prediciton for the user to either purchase or short the stock.

---

## Contributors

Developed by:

Austin

Dan Poreda
danporeda@yahoo.com

Megan Colip

Graham Johnstone
Email: johnstonegr@gmail.com

---

## License
This code is published under the Creative Commons License, 2021.

