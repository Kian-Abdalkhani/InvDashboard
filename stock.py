import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin
import datetime as dt


class Stock():
    def __init__(self, ticker):
        #make pandas datareader work with yahoo finance
        yfin.pdr_override()

        #test if the ticker is valid
        try:
            self.price_data = pdr.get_data_yahoo(ticker,actions=True)
        except:
            raise ValueError("Invalid ticker")
        
        #check if ticker is an etf
        try:
            self.price_data = self.price_data.drop(columns=["Capital Gains"])
        except:
            self.isETF = False
        else:
            self.isETF = True
        
        #remove all unecessary columns from the data sets
        self.price_data = self.price_data.drop(columns=["Stock Splits","Open",
                                                         "High","Low","Close"])
        
        self.price_data["Adj Close"] = self.price_data["Adj Close"].round(2)

        #create a dividend_data value that only stores data for days in which dividend is paid out
        self.dividend_data = self.price_data[(self.price_data["Dividends"] > 0)]
        self.dividend_data = self.dividend_data.drop(columns=["Volume"])

        #add a column for trailing dividend yield and a variable for dividend payout schedule
        self.dividend_data["Days Between"] = self.dividend_data.index.diff()
        latest_div = self.dividend_data["Days Between"][-1]
        latest_div = latest_div.days
        #latest_div = int(latest_div)

        #monthly
        if latest_div <= 70:
            self.div_payments_yearly = 12
        #quarterly
        elif 135 >= latest_div > 70:
            self.div_payments_yearly = 4
        #semi-annual
        elif 240 >= latest_div > 135:
            self.div_payments_yearly = 2
        #annually
        elif latest_div > 240:
            self.div_payments_yearly = 1

        self.dividend_data["Year Dividend Payment"] = self.dividend_data['Dividends'].rolling(self.div_payments_yearly).sum()
        self.dividend_data["Dividend Yield"] = self.dividend_data["Year Dividend Payment"] / self.dividend_data["Adj Close"]
        self.dividend_data["Dividend Yield"] = self.dividend_data["Dividend Yield"].round(5)




test = Stock(ticker="JEPQ")
print(test.dividend_data)


