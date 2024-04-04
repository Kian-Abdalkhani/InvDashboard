from pandas_datareader import data as pdr
import yfinance as yfin


class Stock():

    AVG_YEARLY_TRADING_DAYS = 252
    VOLATILITY_INDEXES = {"S&P":"^VIX","NASDAQ":"^VXN","DOW":"^VXD","RUS":"^RVX"}
    STOCK_INDEXES = {"S&P":"^GSPC","NASDAQ":"^IXIC","DOW":"^DJI","RUS":"^RUT"}

    def __init__(self, ticker):

        #create variable for ticker
        self.ticker = ticker

        #make pandas datareader work with yahoo finance
        yfin.pdr_override()

        #if ticker is not valid, return an error
        if self.__valid_ticker() == False:
            raise ValueError("Entered ticker symbol not valid")
        
        self.price_data = pdr.get_data_yahoo(self.ticker,actions=True)
        
        #check if ticker is an etf and if it pays dividends and remove unalike column
        self.isETF = self.__etf_check()
        if self.isETF:
            self.price_data = self.price_data.drop(columns=["Capital Gains"])
        
        #generate the dataframes
        self.price_data = self.__generate_price_frame()
        self.pays_dividend = not self.price_data[(self.price_data["Dividends"] > 0)].empty
        if self.pays_dividend == True:
            self.dividend_data,self.div_payments_yearly = self.__generate_div_frame()


    
    #returns whether ticker exists or not
    def __valid_ticker(self):
        try:
            test = pdr.get_data_yahoo(self.ticker,actions=True)
        except:
            return False
        else:
            if test.empty:
                return False
            else:
                return True
    
    #check if ticker is an ETF or not
    def __etf_check(self):
        try:
            self.price_data.drop(columns=["Capital Gains"])
        except:
            return False
        else:
            return True
    
    #generate the price dataframe
    def __generate_price_frame(self):

        #drop unecessary columns and round adjusted close to the nearest cent
        df = self.price_data.drop(columns=["Stock Splits","Open",
                                             "High","Low","Close"])
        df["Adj Close"] = df["Adj Close"].round(2)

        return df

    #generate dividend dataframe
    def __generate_div_frame(self):

        #filter out all rows without dividend payments
        df = self.price_data[(self.price_data["Dividends"] > 0)]
        df = df.drop(columns=["Volume"])

        #add a column for div yield
        df["Days Between"] = df.index.diff()
        avg_days = df["Days Between"].median()
        avg_days = avg_days.days

        #monthly
        if avg_days <= 70:
            div_payments_yearly = 12
        #quarterly
        elif 135 >= avg_days > 70:
            div_payments_yearly = 4
        #semi-annual
        elif 240 >= avg_days > 135:
            div_payments_yearly = 2
        #annually
        elif avg_days > 240:
            div_payments_yearly = 1

        df["Year Dividend Payment"] = df['Dividends'].rolling(div_payments_yearly).sum()
        df["Dividend Yield"] = df["Year Dividend Payment"] / df["Adj Close"]
        df["Dividend Yield"] = df["Dividend Yield"].round(5)

        return df,div_payments_yearly

    #generates data for CAGR on series passed in
    def __cagr(self):
        pass
    

    def __comparison_metrics(self):
        pass

    def __str__(self):
        return f"TICKER: {self.ticker}"




tick = Stock("^VIX")
print(tick.price_data["Adj Close"].median())


