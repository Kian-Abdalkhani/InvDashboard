import unittest
from analysis import calculate_cagr
from id_stock import id_ticker

class TestAnalysis(unittest.TestCase):

    def test_cagr(self):
        
        tick = id_ticker("SCHD")
        test = calculate_cagr(tick.dividendData["Year Dividend Payment"],3)
        
        self.assertIsInstance(test,float,"calculate_cagr function should always return a float")
        self.assertGreaterEqual(test,0,f"{tick.ticker} should always return dividend growth >0")
    




if __name__ == '__main__':
  unittest.main()
