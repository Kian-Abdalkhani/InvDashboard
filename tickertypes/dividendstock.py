import pandas as pd
from .stock import Stock
from .dividend_mixin import DividendMixin

class DividendStock(Stock,DividendMixin):
    def __init__(self, ticker: str) -> None:
        Stock.__init__(self,ticker)
        DividendMixin.__init__(self,ticker)
        
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()