import unittest
from pandas.api.types import infer_dtype
import numpy as np
from yf_api_calls import valid_ticker,__fetch_yf_expense_ratio_data__,__fetch_yf_fin_data__,__fetch_yf_price_data__


TEST_TICKERS = ["SCHD","TLSA","AAPL","MSFT"]
TEST_TICKER_ETF = "SCHD"
TEST_TICKER_STOCK = "AAPL"

class TestValidTicker(unittest.TestCase):
    '''to test valid_ticker function'''
    def test_valid_ticker_valids(self):
        '''to ensure that ticker symbols that do exist are identified as such'''
        valid_tickers = TEST_TICKERS
        actual_result = []
        for tick in valid_tickers:
            try:
                valid_ticker(tick)
            except:
                pass
            else:
                actual_result.append(tick)
        expected_result = ["SCHD","TLSA","AAPL","MSFT"]
        self.assertEqual(expected_result,actual_result)
        
    def test_valid_ticker_invalids(self):
        '''to ensure that ticker symbols that do not exist are identified as such'''
        invalid_tickers = ["0(SD)",".ew1,",".SPY","';*)"]
        actual_result = []
        for tick in invalid_tickers:
            try:
                valid_ticker(tick)
            except:
                pass
            else:
                actual_result.append(tick)
        expected_result = []
        self.assertEqual(expected_result,actual_result)
    
    def test_valid_ticker_spaces(self):
        '''to ensure that leading or trailing spaces are disregarded'''
        space_tickers = [" VOO "," VOO","VOO ","VOO"]
        actual_result = []
        for tick in space_tickers:
            try:
                valid_ticker(tick)
            except:
                pass
            else:
                actual_result.append(tick)
                
    def test_empty_ticker(self):
        '''ensures that a blank input return an error'''
        blank_ticker = ""
        actual_result: bool
        try:
            valid_ticker(blank_ticker)
        except:
            actual_result = True
        else:
            actual_result = False
        
        expected_result = True    
        self.assertEqual(expected_result, actual_result)
    
class TestFetchingPriceData(unittest.TestCase):
    '''to test __fetch_yf_price_data__ function'''
    
    def test_fetch_yf_price_data(self):
        '''ensures that dataframe received from yfinance is accurate'''
        tick = __fetch_yf_price_data__(TEST_TICKER_ETF)
        actual_result = str(tick.index[0])
        expected_result = "2011-10-20 00:00:00"
        self.assertEqual(expected_result, actual_result)
        
class TestFetchingFinData(unittest.TestCase):
    '''to test __fetch_yf_fin_data__ function'''
    
    def test_fetch_yf_fin_data_keys(self):
        '''to test if all of the keys are being returned from the API call'''
        actual_result = list(__fetch_yf_fin_data__(TEST_TICKER_STOCK).keys())
        expected_result = ["IS_Q","IS_Y","BS_Q","BS_Y","CF_Q","CF_Y"]
        self.assertEqual(expected_result, actual_result)
    
    def test_fetch_yf_fin_data_nan_values(self):
        '''to test if all NaN values were replaced with zeros within the fin statements'''
        test = __fetch_yf_fin_data__(TEST_TICKER_STOCK).values()
        result = []
        for num in test:
            if num.isnull().values.any():
                result.append(num)
        self.assertTrue(not result,f"{result} should not be NaN values")
        
    def test_fetch_yf_fin_data_value_type(self):
        '''to test if all values in the financial statements are floats'''
        test = __fetch_yf_fin_data__(TEST_TICKER_STOCK)
        actual_results = []
        for key,val in test.items():
             self.assertTrue(val.dtypes.apply(lambda x: np.issubdtype(x, np.floating)).all(), f"Not all columns in {key} are floating-point types")       
        
    '''NOTE: I am not testing the values of the statement items since
             since all financial statements will not be available always.'''

class TestFetchingExpRatio(unittest.TestCase):
    '''to test __fetch_yf_expense_ratio_data__ function'''
    
    def test_fetch_yf_expense_ratio_data(self):
        '''to test if accurate expense ratios are returned'''
        actual_result = __fetch_yf_expense_ratio_data__(TEST_TICKER_ETF)
        #double check if test ever fails, ratio might've changed for SCHD
        expected_result = 0.06
        self.assertEqual(expected_result, actual_result)
        
if __name__ == '__main__':
  unittest.main()