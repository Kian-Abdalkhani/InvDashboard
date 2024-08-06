import unittest
from tickertypes.dividend_mixin import DividendMixin

class TestDividendMixin(unittest.TestCase):
    
    test = DividendMixin("SCHD")
    
    def test_dividend_data(self):
        '''test if dividend data table is accurate'''
        self.assertEqual(self.test.divFrequency,4,f"{self.test.ticker} pays dividends quarterly")
        
    def test_dividend_yield(self):
        "test to ensure dividend yield is greater than 0 and a float"
        self.assertGreaterEqual(self.test.dividend_yield,0.0)
        self.assertEqual(type(self.test.dividend_yield),float,f"{self.test.dividend_yield} should be a float")
        self.assertIsInstance(self.test.dividend_yield,float)
    

if __name__ == '__main__':
  unittest.main()