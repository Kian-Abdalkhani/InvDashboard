import pandas as pd
from .dividend import Dividend
from .stock import Stock
from .ticker import Ticker

class DividendStock(Dividend,Stock):
    def __init__(self, tick: Ticker) -> None:
        self._tick = tick
        self._ticker = tick.ticker
        super().__init__(tick)
        
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()