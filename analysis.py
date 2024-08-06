import datetime as dt
from functools import cache
import pandas as pd
from tickertypes import *

#useful stock metrics
AVG_YEARLY_TRADING_DAYS = 252
VOLATILITY_INDEXES = {"S&P":"^VIX","NASDAQ":"^VXN","DOW":"^VXD","RUS":"^RVX"}
STOCK_INDEXES = {"S&P":"^GSPC","NASDAQ":"^IXIC","DOW":"^DJI","RUS":"^RUT"}

def calculate_cagr(df: pd.Series, years: int) -> float:
    """
    Calculate the Compound Annual Growth Rate (CAGR) for a given DataFrame.
    
    :param df: DataFrame with a DatetimeIndex and 'Adj Close' column
    :param years: Number of years to calculate CAGR for
    :return: CAGR as a float
    """
    
    end_date: dt.datetime = dt.datetime.today()
    start_date: dt.datetime = end_date - dt.timedelta(days=int(years * 365.25))  # Using 365.25 to account for leap years
    
    # Filter DataFrame efficiently
    df_filtered = df.loc[start_date <= df.index]
    df_filtered = df_filtered.loc[end_date >= df_filtered.index]
    
    # Calculate actual number of years
    actual_years = (end_date - start_date).days / 365.25
    
    # Calculate CAGR
    start_value = df_filtered.iloc[0]
    end_value = df_filtered.iloc[-1]
    
    cagr = (end_value / start_value) ** (1 / actual_years) - 1
    
    return cagr

#
def total_return():
    '''calculates total return over the timespan identified'''
    pass

@cache
def comparison_metrics():
    # Implement comparison metrics calculation
    pass

def main():
    pass

if __name__ == "__main__":
    main()