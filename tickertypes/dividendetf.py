import pandas as pd
from .dividend_mixin import DividendMixin
from .etf import Etf

class DividendEtf(Etf,DividendMixin):
    def __init__(self, ticker: str) -> None:
        Etf.__init__(self,ticker)
        DividendMixin.__init__(self,ticker)
             
def main() -> None:
    pass
      
if __name__ == "__main__":
    main()