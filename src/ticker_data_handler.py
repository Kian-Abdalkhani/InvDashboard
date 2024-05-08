from pandas_datareader import data as pdr
import yfinance as yfin
from functools import lru_cache
from pandas import DataFrame
import atexit

@lru_cache()
def download_data(ticker: str) -> DataFrame:

    #make pandas datareader work with yahoo finance
    yfin.pdr_override()
    
    try:
        test = pdr.get_data_yahoo(ticker,actions=True)
    except:
        raise ValueError("Value entered is not a valid ticker symbol")
    else:
        if test.empty:
            raise ValueError("No values available for the ticker symbol")
        else:
            return DataFrame(test)

def pays_dividends(df_ticker: DataFrame) -> bool:
    return not df_ticker[(df_ticker["Dividends"] > 0)].empty

def etf(df_ticker: DataFrame) -> bool:
    return "Capital Gains" in df_ticker.columns
    
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()