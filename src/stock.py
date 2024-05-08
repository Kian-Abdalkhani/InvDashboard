"""
file that has all the different types of ticker symbols that are publicly traded

"""
import pandas as pd
import ticker_data_handler as tdh
from dataclasses import dataclass
import atexit

@dataclass
class TickerData:
    """Represents processed price data for a ticker."""
    data: pd.DataFrame

    def __post_init__(self):
        self.data = self.__generate_price_frame(self.data)

    @staticmethod
    def __generate_price_frame(data: pd.DataFrame):

        data = data.drop(columns=["Stock Splits", "Open", "High", "Low", "Close"])
        data["Adj Close"] = data["Adj Close"].round(2)
        return data


class Ticker:
    def __init__(self, ticker: str, pays_dividends: bool = False,is_etf: bool = True):
        self.ticker: str = ticker
        self.pays_dividends: bool = False
        self.is_etf: bool = True
        self.price_data = TickerData(tdh.download_data(ticker)).data
    
    def __str__(self):
        return f"--{self.ticker}-- \n Dividends: {self.pays_dividends}"
    

class Etf(Ticker):
    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.is_etf = True
        self.dividend_data: pd.DataFrame = pd.DataFrame()
        self.div_payments_yearly: int = 0
        
        # ETF specific checks and cleaning
        self.price_data = self.price_data.drop(columns=["Capital Gains"])
        

class Stock(Ticker):
    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.is_etf: bool = False
        self.dividend_data: pd.DataFrame = pd.DataFrame()
        self.div_payments_yearly: int = 0

class Dividend(Ticker):
    def __init__(self, ticker: str):
        super().__init__(ticker)
        
        self.pays_dividends = True
        self.dividend_data: pd.DataFrame
        self.div_payments_yearly: int
        self.dividend_data,self.div_payments_yearly = self.__generate_div_frame__()

    def __generate_div_frame__(self) -> tuple[pd.DataFrame, int]:

        #filter out all rows without dividend payments
        df: pd.DataFrame = self.price_data[(self.price_data["Dividends"] > 0)]
        df = df.drop(columns=["Volume"])

        #add a column for div yield
        df["Days Between"] = df.index
        df["Days Between"] = df["Days Between"].diff()
        avg_days = df["Days Between"].dt.days.median()
        div_payments_yearly: int = 0
        
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

class DividendEtf(Dividend,Etf):
    def __init__(self, ticker: str):
        super().__init__(ticker) 
        Etf(ticker).__init__(ticker)
        
class DividendStock(Dividend,Stock):
    def __init__(self, ticker: str):
        super().__init__(ticker)
        Stock(ticker).__init__(ticker)

def id_ticker(ticker: str):
    '''class uses ticker_data_handler and the ticker to determine the type of investment'''
    tick_id = tdh.download_data(ticker)
    if tdh.etf(tick_id):
        return DividendEtf(ticker=ticker) if tdh.pays_dividends(tick_id) else Etf(ticker=ticker)
    else:
         return DividendStock(ticker=ticker) if tdh.pays_dividends(tick_id) else Stock(ticker=ticker)

#
@atexit.register        
def clear_cache():
    '''ensures cache is clear at the end of every run'''
    tdh.download_data.cache_clear()
    
def main() -> None:
    pass
      
if __name__ == "__main__":
    main()


