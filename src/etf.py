import pandas as pd
from .ticker import Ticker

class Etf(Ticker):
    def __init__(self, tick: Ticker) -> None:
        
        
        # ETF specific checks and cleaning
        self._price_data = tick.priceData.drop(columns=["Capital Gains"])
        # if not self.paysDividends:
        #     self.dividend_data: pd.DataFrame = pd.DataFrame()
        #     self.div_payments_yearly: int = 0
        
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()