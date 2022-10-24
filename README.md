# Stock Signal Predictor

This program uses machine learning to try to predict the future movement of an individual stock. The program uses two years of historcal stock data to train a predictive model.  Several ML models including SVC, AdaBoost, and RandomForest were tested in the code development, but the LogisticRegression model from Scikit-Learn was chosen for overall outperformace of other models. Model training in machine learning is a process that requires fine-tuning, and in this program, the size of the training-data is the variable that yeilds different performative results, with different values. So, this app attempts to assist the user in finding the optimal training window size for a model-predicted outcome. The program starts with user input of a stock ticker, which the program uses to retrieve 2 years of the stock's OHLCV historical data from the most recent market-close date, into a dataframe. The predictive trading signal column is created based on the (shifted) daily returns. The program then utilizes 12 functions of different moving averages from the Finta TA library, and records those metrics into a dataframe for model training. Next, the program iterates through a model-training process where the iterating variable is the amount of weeks designated for training data, starting with 1 week, up to 100 weeks. With each iteration, the cumulative returns of the actual security, and the cumulative returns of the algorithmic trading strategy are compared; if the algorithmic trading strategy outperforms the security's cumulative return, then that iteration's week size and algo-cumulative-return size are recorded into a dictionary (key = weeks, value = returns). After the iteration process is complete, the dictionary's highest return value is identified, and it's key (number of weeks) is extracted into a variable to finally train the model for user output.  The program uses a local web app called "Flask" for a clean and simple user experience.

---

## Technologies

This application is compatible with Python 3.9.

The OS, Requests, JSON, Pandas, datetime, hvplot and FinTA libraries were used along with matplotlib and must be installed in order to run the program correctly. Stock data will be pulled from Alpaca so the user will need to install the Alpaca API. The Scikit-learn and imbalanced-learn libraries will have to be installed for machine learning. Flask for Python must be installed in order to enable user input.

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

Flask for Python allows the code to be run behind a clean and simple web app within a virtual environment.

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

Documentation for Flask can be found [here.](https://flask.palletsprojects.com/en/2.2.x/)

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
pip install Flask
```
---

## Usage

Clone or download the files from the Github repository.

You must create a virtual enviroment in order to use Flask.
Using your CLI, navigate to the directory containing the jupyter notebook file and type the following into your command prompt -

For MacOS / Linux users -
```
mkdir stock_signal_predictor
cd stock_signal_predictor
python3 -m venv venv
```

For Windows users -
```
mkdir stock_signal_predictor
cd stock_signal_predictor
py -3 -m venv venv
```

The virtual environment will then have to be activated. To do this type the following into your command prompt -

For MacOS / Linux users -
```
. venv/bin/activate
```

For Windows users -
```
venv\Scripts\activate
```

The final step is to load the Flask app and the notebook file associated with it. Type the following into your command prompt -
```
flask --app app run
```

The program will open in a web browser window with a prompt to enter a stock ticker of the users choice.
Once the user enters their ticker symbol, they press the "Submit" button. The program then returns an output that displays a recommendation based on the prediciton for the user to either purchase or sell / short the stock.

---

## Contributors

Developed by:

Austin

Dan Poreda
Email: danporeda@yahoo.com

Megan Colip

Graham Johnstone
Email: johnstonegr@gmail.com

---

## License
This code is published under the Creative Commons License, 2022.
