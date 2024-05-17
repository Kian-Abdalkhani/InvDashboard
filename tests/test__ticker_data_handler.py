import setup_path
import unittest
from ticker_data_handler import Ticker

class TestTicker(unittest.TestCase):
    invalid_tickers: list[str] = [" ",".ew1,",".SPY",""]
    
    
    def test_tickers_with_spaces(self):
        '''ensures that spaces within the input are disregarded'''
        space_tickers = [" V O O ", " VOO "," VOO","VOO ","VOO"]
        actual_result = []
        for tick in space_tickers:
            try:
                Ticker(tick)
            except:
                pass
            else:
                actual_result.append(tick)
        
        expected_result = space_tickers    
        self.assertEqual(expected_result, actual_result)
            
    def test_empty_ticker(self):
        '''ensures that a blank input return an error'''
        blank_ticker = ""
        actual_result: bool
        try:
            Ticker(blank_ticker)
        except:
            actual_result = True
        else:
            actual_result = False
        
        expected_result = True    
        self.assertEqual(expected_result, actual_result)
        
    def test_df_generated(self):
        '''ensures that dataframe received from yfinance is accurate'''
        test_ticker = "SCHD"
        tick = Ticker(test_ticker)
        actual_result = str(tick.price_data.index[0])
        expected_result = "2011-10-20 00:00:00"
        self.assertEqual(expected_result, actual_result)
    
    def test_etf(self):
        '''ensures that program accurately determines if ticker is etf'''
        etf_tickers: list[str] = ["JEPQ","SCHD","VOO"]
        stocks_tickers: list[str] = ["KO","AAPL","T"]
        all_tickers: list[str] = etf_tickers + stocks_tickers
        actual_result = []
        for tick in all_tickers:
            test = Ticker(tick)
            if test.etf():
                actual_result.append(test.ticker)
        expected_result = etf_tickers   
        self.assertEqual(expected_result, actual_result)
        
    def test_dividend(self):
        '''ensures that program accurately determines if ticker pays dividend'''
        dividend_tickers: list[str] = ["JEPQ","SCHD","VOO"]
        non_dividend_tickers: list[str] = ["TSLA","PLTR","GME"]
        all_tickers: list[str] = dividend_tickers + non_dividend_tickers
        actual_result = []
        for tick in all_tickers:
            test = Ticker(tick)
            if test.dividends():
                actual_result.append(test.ticker)
        expected_result = dividend_tickers   
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
  unittest.main()
