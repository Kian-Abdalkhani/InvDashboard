from pandas_datareader import data as pdr
import yfinance as yfin

class TickerDownloader():

    def download_data(self, ticker):

        #make pandas datareader work with yahoo finance
        yfin.pdr_override()
        
        try:
            test = pdr.get_data_yahoo(ticker,actions=True)
        #if dataframe could not be made
        except:
            return ValueError("Value entered is not a valid ticker symbol")
        else:
            #if dataframe returned was empty
            if test.empty:
                return ImportError("No values available for the ticker symbol")
            else:
                return test

class Ticker(TickerDownloader):

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.price_data = self.download_data(ticker)
        self.price_data = self.__generate_price_frame()

        # checks if symbol is etf
        self.pays_dividend = not self.price_data[(self.price_data["Dividends"] > 0)].empty
        if self.__is_ETF():
            self.__class__ = Etf
        else:
            self.__class__ = Stock
   
    def __str__(self):
        return f"TICKER: {self.ticker}"
    
    #generate the price dataframe
    def __generate_price_frame(self):

        #drop unecessary columns and round adjusted close to the nearest cent
        df = self.price_data.drop(columns=["Stock Splits","Open",
                                             "High","Low","Close"])
        df["Adj Close"] = df["Adj Close"].round(2)

        return df
            
    def __is_ETF(self):
        try:
            self.price_data.drop(columns=["Capital Gains"])
        except:
            return False
        else:
            return True

class Etf(Ticker):
    def __init__(self, ticker):
        super().__init__(ticker)

        # ETF specific checks and cleaning
        self.price_data = self.price_data.drop(columns=["Capital Gains"])

        if self.pays_dividend:
            self.__class__ = DividendEtf

class Stock(Ticker):
    def __init__(self, ticker):
        super().__init__(ticker)

        if self.pays_dividend:
            self.__class__ = DividendStock

class Dividend(Ticker):
    def __init__(self, ticker):
        super().__init__(ticker)

        # Identify dividend payers and calculate related data
        self.dividend_data,self.div_payments_yearly = self.__generate_div_frame()

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

class DividendEtf(Etf,Dividend):
    def __init__(self, ticker):
        super().__init__(ticker)
        Dividend.__init__(ticker)

class DividendStock(Stock,Dividend):
    def __init__(self, ticker):
        super().__init__(ticker)
        Dividend.__init__(ticker)

class StockAnalysis:
    #useful stock metrics
    AVG_YEARLY_TRADING_DAYS = 252
    VOLATILITY_INDEXES = {"S&P":"^VIX","NASDAQ":"^VXN","DOW":"^VXD","RUS":"^RVX"}
    STOCK_INDEXES = {"S&P":"^GSPC","NASDAQ":"^IXIC","DOW":"^DJI","RUS":"^RUT"}
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def calculate_cagr(self):
        # Implement CAGR calculation
        pass

    def comparison_metrics(self):
        # Implement comparison metrics calculation
        pass

tick = Ticker("JEPQ")
print(tick.__class__)


