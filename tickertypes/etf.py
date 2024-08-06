import pandas as pd
from tickertypes.ticker import Ticker
from yf_api_calls import __fetch_yf_expense_ratio_data__

class Etf(Ticker):
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker)
        self.priceData = self.priceData.drop(columns=["Capital Gains"])
    
    @property
    def expenseRatio(self) -> float:
        return __fetch_yf_expense_ratio_data__(self.ticker)
    
    @property
    def fin_statements(self) -> dict:
        return {}

def main() -> None:
    pass
    
if __name__ == "__main__":
    main()