import pandas as pd
from tickertypes.ticker import Ticker
from yf_api_calls import __fetch_yf_fin_data__

class Stock(Ticker):
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker)
    
    @property
    def expenseRatio(self) -> float:
        return 0.0
    
    @property
    def fin_statements(self) -> dict:
        return __fetch_yf_fin_data__(self.ticker)
        
        
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()