'''file that has all the different types of ticker symbols that are publicly traded'''

import pandas as pd
from src import (Ticker,DividendEtf,DividendStock,Etf,Stock)

def id_ticker(ticker: str):
    '''class uses ticker_data_handler and the ticker to determine the type of investment'''
    tick = Ticker(ticker)
    if tick.isEtf:
        return DividendEtf(tick) if tick.paysDividends else Etf(tick)
    else:
        return DividendStock(tick) if tick.paysDividends else Stock(tick)
    
def main() -> None:
    pass
      
if __name__ == "__main__":
    main()


