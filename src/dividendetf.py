import pandas as pd
from .dividend import Dividend
from .etf import Etf
from .ticker import Ticker

class DividendEtf(Etf,Dividend):
    def __init__(self, tick: Ticker) -> None:
        self._tick = tick
        self._ticker = tick.ticker
        super().__init__(tick)
        
    @property
    def dividend_data(self):
        return self.get_dividend_data(self.priceData)
        
def main() -> None:
    test = DividendEtf(Ticker("JEPQ"))
    
    
if __name__ == "__main__":
    main()