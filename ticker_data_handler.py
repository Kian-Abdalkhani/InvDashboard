from pandas_datareader import data as pdr
import yfinance as yfin
import pandas as pd
from functools import lru_cache

class Ticker:
    """Analyzes data received from yfinance to identify key characteristics of the ticker"""
    
    def __init__(self,ticker: str) -> None:
        
        #removes any spaces in the ticker input
        self.ticker: str = ticker
        while " " in self.ticker:
            self.ticker = self.ticker.replace(" ","")
            
        self.price_data: pd.DataFrame = self.__download_data__()
        self.isETF: bool = self.etf()
        self.pays_dividend: bool = self.dividends()

    @lru_cache()
    def __generate_price_frame__(self) -> pd.DataFrame:
        """removes unecessary columns in the data for ease of use"""

        df = self.price_data.drop(columns=["Stock Splits", "Open", "High", "Low", "Close"])
        df["Adj Close"] = df["Adj Close"].round(2)
        return df

    @lru_cache()
    def __download_data__(self) -> pd.DataFrame:
        """downloads data from yahoo finance and returns error if unable"""

        #makes pandas_datareader work with yfinance
        yfin.pdr_override()
        
        try:
            df = pdr.get_data_yahoo(self.ticker,actions=True)
        except:
            raise ValueError("Value entered is not a valid ticker symbol")
        else:
            if df.empty:
                raise ValueError("No values available for the ticker symbol")
            else:
                df = df.drop(columns=["Stock Splits", "Open", "High", "Low", "Close"])
                df["Adj Close"] = df["Adj Close"].round(2)
                if type(df) == pd.DataFrame:
                    return df
                else:
                    raise ValueError("Data received from API appears to be improperly formatted")
            
    @lru_cache()
    def dividends(self) -> bool:
        """returns if symbol pays dividends in the last year"""
        today = pd.Timestamp.today()
        dividends = self.price_data[(self.price_data["Dividends"] > 0) & (self.price_data.index >= today - pd.DateOffset(years=1))]
        return not dividends.empty

    @lru_cache()
    def etf(self) -> bool:
        """returns if symbol is an etf or not"""
        return "Capital Gains" in self.price_data.columns

    def clear_cache(self) -> None:
        """clears cache for the data cached in the class object"""
        self.__download_data__.cache_clear()
        self.__generate_price_frame__.cache_clear()
        self.dividends.cache_clear()
        self.etf.cache_clear()
    
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()