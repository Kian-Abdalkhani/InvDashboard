import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from functools import cache

@cache
def generate_error_code(ticker:str):
    raise ValueError(f"No values available for '{ticker}'")

@cache
def valid_ticker(ticker:str) -> bool:
        """throws error if invalid ticker is input"""
        data = __fetch_yf_price_data__(ticker)
        if data.empty:
            generate_error_code(ticker)
            return False
        else:
            return True
        
@cache
def __fetch_yf_price_data__(ticker:str) -> pd.DataFrame:
        """communicates with API to return price dataframe"""
        data = pd.DataFrame()
        yf.pdr_override()
        yf_data =  pdr.get_data_yahoo(ticker,actions=True)
        if yf_data.empty == False and type(yf_data) == pd.DataFrame:
            data = yf_data
        
        return data
            
@cache
def __fetch_yf_fin_data__(ticker:str) -> dict:
        """communicates with API to return financial statements"""
        
        yf_tick = yf.Ticker(ticker)
        
        fin_statements = {"IS_Q":yf_tick.quarterly_income_stmt.copy(),
                          "IS_Y":yf_tick.income_stmt.copy(),
                          "BS_Q":yf_tick.quarterly_balance_sheet.copy(),
                          "BS_Y":yf_tick.balance_sheet.copy(),
                          "CF_Q":yf_tick.quarterly_cash_flow.copy(),
                          "CF_Y":yf_tick.cash_flow.copy()}
        
        for key, df in fin_statements.items():
            with pd.option_context("future.no_silent_downcasting", True):
                fin_statements[key] = df.fillna(0.0).astype("float64")

        
        return fin_statements
                
@cache         
def __fetch_yf_expense_ratio_data__(ticker:str) -> float:
    '''returns the expense ratio of a given ETF'''
    
    response = requests.get(f"https://finance.yahoo.com/quote/{ticker}/")
    soup = BeautifulSoup(response.text,"html.parser")
    
    value = 0.0
    for li in soup.find_all('li', class_="last-md yf-tx3nkj"):
        if "Expense Ratio (net)" in li.text.strip():
            for value_element in li.find_all('span', class_="value yf-tx3nkj"):
                exp_ratio = value_element.text.strip().replace("%","")
                value = float(exp_ratio)

    return value

def main():
    __fetch_yf_fin_data__("AAPL")

if __name__ == "__main__":
    main()
            
'''make sure that this code also:
'''