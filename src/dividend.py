import pandas as pd

class Dividend():
    
    @staticmethod
    def get_dividend_frequency(df_price_data: pd.DataFrame) -> int:
        #add a column for div yield
        df_price_data["Days Between"] = df_price_data.index
        df_price_data["Days Between"] = df_price_data["Days Between"].diff()
        avg_days = df_price_data["Days Between"].dt.days.median()
        
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
    
    def get_dividend_data(self,df_price_data: pd.DataFrame) -> pd.DataFrame:
        """takes in the price data from the Ticker object and returns """

        #filter out all rows without dividend payments
        df: pd.DataFrame = df_price_data[(df_price_data["Dividends"] > 0)]
        df = df.drop(columns=["Volume"])

        div_frequency = self.get_dividend_frequency(df)

        df["Year Dividend Payment"] = df['Dividends'].rolling(div_frequency).sum()
        df["Dividend Yield"] = df["Year Dividend Payment"] / df["Adj Close"]
        df["Dividend Yield"] = df["Dividend Yield"].round(5)

        return df
    
    
def main() -> None:
    pass
    
if __name__ == "__main__":
    main()