'''file that has all the different types of ticker symbols that are publicly traded'''

import pandas as pd
from tickertypes.ticker import Ticker
from tickertypes.etf import Etf
from tickertypes.dividendetf import DividendEtf
from tickertypes.dividendstock import DividendStock
from tickertypes.stock import Stock

def id_ticker(ticker: str):
    '''class uses ticker_data_handler and the ticker to determine the type of investment'''
    ticker = ticker.strip().upper()
    tick = Ticker(ticker)
    if tick.isEtf:
        return DividendEtf(ticker) if tick.paysDividends else Etf(ticker)
    else:
        return DividendStock(ticker) if tick.paysDividends else Stock(ticker)
    
def main() -> None:
    pass
      
if __name__ == "__main__":
    main()


