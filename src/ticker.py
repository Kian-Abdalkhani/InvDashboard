import pandas as pd
from functools import cache
from pandas_datareader import data as pdr
import yfinance as yf


class Ticker:
    """retreive data from yfinance and identify key characteristics of the ticker"""
    
    def __init__(self,ticker: str) -> None:
        self._ticker: str = ticker
        self.valid_ticker()
        
    @property
    def ticker(self):
        return self._ticker.strip().upper()
    
    @property
    def priceData(self) -> pd.DataFrame:
        self._priceData = self.fetch_yf_price_data().drop(columns=
                ["Stock Splits", "Open", "High", "Low", "Close"])
        self._priceData["Adj Close"] = self._priceData["Adj Close"].round(2)
        return self._priceData
    
    @priceData.setter
    def priceData(self,value):
        """allows etf class to drop the 'Capital Gains' column to keep structure"""
        if value == self.priceData.drop(columns=["Capital Gains"]):
            self.priceData = value
        else:
            return ValueError("cannot change pricing data")
      
    @property
    def paysDividends(self) -> bool:
        today = pd.Timestamp.today()
        dividends = self.priceData[(self.priceData["Dividends"] > 0) & (self.priceData.index >= today - pd.DateOffset(years=1))]
        return not dividends.empty

    @property
    def isEtf(self) -> bool:
        return "Capital Gains" in self.priceData.columns

    @cache
    def fetch_yf_price_data(self) -> pd.DataFrame:
        """communicates with API to return dataframe"""
        yf.pdr_override()
        data =  pdr.get_data_yahoo(self.ticker,actions=True)
        if data.empty:
            raise ValueError(f"No values available for '{self.ticker}'")
        elif type(data) == pd.DataFrame:
            return data
        else:
            raise ValueError(f"Data received from API for '{self.ticker}' appears to be improperly formatted")
        
    @cache        
    def valid_ticker(self) -> bool:
        """throws error if invalid ticker is input"""
        try:
            self.fetch_yf_price_data()
        except:
            raise ValueError("Value entered is not a valid ticker symbol")
        else:
            return True
    
    def __hash__(self) -> int:
        return hash(self.ticker)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value,self.__class__):  
            return self.ticker == value.ticker
        else:
            return False
    
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()