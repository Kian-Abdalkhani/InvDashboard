import pandas as pd
from tickertypes.ticker import Ticker

class DividendMixin(Ticker):
    
    def __init__(self,ticker: str) -> None:
        super().__init__(ticker)
        
        #create private variable to be accessed by properties
        self._dividendData_ = self.priceData.copy()
        self._dividendData_ = self._dividendData_[(self._dividendData_["Dividends"] > 0)]
    
    @property
    def divFrequency(self) -> int:
        '''return the frequency of dividend payments'''
        
        temp_freq: pd.DataFrame = self._dividendData_.copy()
        
        temp_freq["Days Between"] = temp_freq.index
        temp_freq["Days Between"] = temp_freq["Days Between"].diff()
        avg_days = temp_freq["Days Between"].dt.days.median()
        
        #monthly
        if avg_days <= 70:
            return 12
        #quarterly
        elif 135 >= avg_days > 70:
            return 4
        #semi-annual
        elif 240 >= avg_days > 135:
            return 2
        #annually
        elif 370 > avg_days > 240:
            return 1
        else:
            raise ValueError("dividend data does not show consistent yearly payments")
    
    @property
    def dividendData(self) -> pd.DataFrame:
        """returns Dataframe of all dividend payments made"""

        df: pd.DataFrame = self._dividendData_.copy()
        
        df = df.drop(columns=["Volume"])

        df["Year Dividend Payment"] = df['Dividends'].rolling(self.divFrequency).sum()
        df["Dividend Yield"] = df["Year Dividend Payment"] / df["Adj Close"]
        df["Dividend Yield"] = df["Dividend Yield"].round(5)

        return df
    
    @property
    def dividend_yield(self) -> float:
        return float(self.dividendData["Year Dividend Payment"].iloc[-1])/ self.currentPrice

    
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()