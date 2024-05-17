"""
file that has all the different types of ticker symbols that are publicly traded

"""
import pandas as pd
from ticker_data_handler import Ticker


class Etf(Ticker):
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker)
        
        self.dividend_data: pd.DataFrame = pd.DataFrame()
        self.div_payments_yearly: int = 0
        
        # ETF specific checks and cleaning
        self.price_data = self.price_data.drop(columns=["Capital Gains"])
        

class Stock(Ticker):
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker)
        
        self.dividend_data: pd.DataFrame = pd.DataFrame()
        self.div_payments_yearly: int = 0

class Dividend(Ticker):
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker)
        
        
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
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker) 
        Etf(ticker).__init__(ticker)
        
class DividendStock(Dividend,Stock):
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker)
        Stock(ticker).__init__(ticker)

def id_ticker(ticker: str):
    '''class uses ticker_data_handler and the ticker to determine the type of investment'''
    tick_id = Ticker(ticker)
    if tick_id.isETF:
        return DividendEtf(ticker=ticker) if tick_id.pays_dividend else Etf(ticker=ticker)
    else:
        return DividendStock(ticker=ticker) if tick_id.pays_dividend else Stock(ticker=ticker)
    
def main() -> None:
    test = id_ticker("VIXM")
    print(isinstance(test,Etf))
    
      
if __name__ == "__main__":
    main()


