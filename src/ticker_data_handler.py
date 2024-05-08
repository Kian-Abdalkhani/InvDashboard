from pandas_datareader import data as pdr
import yfinance as yfin
from functools import lru_cache
from pandas import DataFrame
import atexit
import stock

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

@lru_cache()
def id_ticker(ticker: str) -> object:
    tick_id = download_data(ticker)
    if etf(tick_id):
        return stock.DividendEtf(ticker=ticker) if pays_dividends(tick_id) else stock.Etf(ticker=ticker)
    else:
         return stock.DividendStock(ticker=ticker) if not pays_dividends(tick_id) else stock.Stock(ticker=ticker)
    
#to ensure cache is cleared after the program finishes
@atexit.register
def clear_cache():
    id_ticker.cache_clear()
    download_data.cache_clear()
    
def main() -> None:
    tick = id_ticker("SCHD")
    print(tick.div_payments_yearly)
    clear_cache()
    
if __name__ == "__main__":
    main()