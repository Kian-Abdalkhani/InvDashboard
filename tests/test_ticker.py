import unittest
from tickertypes.ticker import Ticker

class TestTicker(unittest.TestCase):
    schd = Ticker("SCHD")
        
    def test_manipulating_ticker(self):
        '''ensures that user doesn't have access to change ticker attribute in the Ticker class'''
        actual_result = None
        try:
            self.schd.ticker = None # type: ignore
        except:
            actual_result =  False
        else:
            actual_result =  True
        expected_result = False   
        self.assertEqual(expected_result, actual_result)
        
    def test_manipulating_priceData(self):
        '''ensures that user doesn't have access to change priceData attribute in the Ticker class'''
        actual_result = None
        try:
            self.schd.priceData = None # type: ignore
        except:
            actual_result =  False
        else:
            actual_result =  True
        expected_result = False   
        self.assertEqual(expected_result, actual_result)
    
    def test_manipulating_isEtf(self):
        '''ensures that user doesn't have access to change isEtf attribute in the Ticker class'''
        actual_result = None
        try:
            self.schd.isEtf = None # type: ignore
        except:
            actual_result =  False
        else:
            actual_result =  True
        expected_result = False   
        self.assertEqual(expected_result, actual_result)
        
    def test_manipulating_paysDividends(self):
        '''ensures that user doesn't have access to change paysDividends attribute in the Ticker class'''
        actual_result = None
        try:
            self.schd.paysDividends = None # type: ignore
        except:
            actual_result =  False
        else:
            actual_result =  True
        expected_result = False   
        self.assertEqual(expected_result, actual_result)      
        
    def test_df_generated(self):
        '''ensures that dataframe received from yfinance is accurate'''
        test_ticker = "SCHD"
        tick = Ticker(test_ticker)
        actual_result = str(tick.priceData.index[0])
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
            if test.isEtf:
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
            if test.paysDividends:
                actual_result.append(test.ticker)
        expected_result = dividend_tickers   
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
  unittest.main()
