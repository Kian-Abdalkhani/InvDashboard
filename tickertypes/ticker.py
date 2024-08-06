import pandas as pd
from yf_api_calls import valid_ticker,__fetch_yf_price_data__

class Ticker:
    """retreive data from yfinance and identify key characteristics of the ticker"""

    def __init__(self,ticker: str) -> None:
        self._ticker_: str = ticker
        valid_ticker(self._ticker_)
        
    @property
    def ticker(self):
        return self._ticker_
    
    @property
    def priceData(self) -> pd.DataFrame:
        self._priceData_ = __fetch_yf_price_data__(self._ticker_).drop(columns=
                ["Stock Splits", "Open", "High", "Low", "Close"])
        self._priceData_["Adj Close"] = self._priceData_["Adj Close"].round(2)
        return self._priceData_
    
    @priceData.setter
    def priceData(self,value: pd.DataFrame):
        """allows etf class to drop the 'Capital Gains' column to keep structure"""
        if len(value.columns) == len(self.priceData.drop(columns=["Capital Gains"])):
            self.priceData = value
        else:
            return ValueError("cannot change pricing data")
        
    @property
    def currentPrice(self):
        return float(self.priceData["Adj Close"].iloc[-1])
      
    @property
    def paysDividends(self) -> bool:
        today = pd.Timestamp.today()
        dividends = self.priceData[(self.priceData["Dividends"] > 0) & (self.priceData.index >= today - pd.DateOffset(years=1))]
        return not dividends.empty

    @property
    def isEtf(self) -> bool:
        return "Capital Gains" in self.priceData.columns
    
    @property
    def divFrequency(self) -> int:
        return 0
    
    @property
    def dividendData(self) -> pd.DataFrame:
        return pd.DataFrame()
        
    @property
    def dividend_yield(self) -> float:
        return 0.0
    
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