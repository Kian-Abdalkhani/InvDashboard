import unittest
from src.stock import Stock

class TestStock(unittest.TestCase):
    AVG_YEARLY_TRADING_DAYS = 252
    VOLATILITY_INDEXES = {"S&P":"^VIX","NASDAQ":"^VXN","DOW":"^VXD","RUS":"^RVX"}
    STOCK_INDEXES = {"S&P":"^GSPC","NASDAQ":"^IXIC","DOW":"^DJI","RUS":"^RUT"}

    tickers = {"Invalid":"EQ>Z", #invalid tickers 
                "ETF":"SCHD", #ETFs
                "Dividend":"MSFT", #Dividend tickers
                "Non-Dividend": "TSLA", #Tickers that don't pay dividends
                "Index":"SPX" #stock indexes
                }
    valid_tickers = {"ETF":Stock("SCHD"), #ETFs
                     "Dividend":Stock("MSFT"), #Dividend tickers
                     "Non-Dividend": Stock("TSLA"), #Tickers that don't pay dividends
                     "Index":Stock("SPX") #stock indexes
                }

    def setUp(self):
        # Initialize objects or variables used in your tests here.
        # This method runs before each test case.
        #symbols to run tests on
        pass

    def tearDown(self):
        # Clean up any resources used in your tests here.
        # This method runs after each test case.
        pass

    def test_function_name(self):
        """
        This docstring describes what your test case is verifying.

        Args:
        self: The test case object.
        """
        # Arrange (Set up the test data and conditions)
        # Act (Call the function or method you're testing)
        # Assert (Verify the expected outcome using assertions)

        # # Example: Test if a function adds numbers correctly
        # expected_result = 10
        # actual_result = your_function(5, 5)
        # self.assertEqual(expected_result, actual_result)
        pass

    #test all the different types of tickers and return only the invalid ones
    def test__valid_ticker(self):
        actual_result = ""
        for value in self.tickers.values():
                try:
                    Stock(value)
                except:
                    actual_result = value
                    break
                
        expected_result = self.tickers["Invalid"]
        self.assertEqual(expected_result,actual_result)

    #test all of the valid tickers to see if it accurately tells ETF or not
    def test__etf_check(self):
        self.assertEqual(True,self.valid_tickers["ETF"].isETF)
        self.assertEqual(False,self.valid_tickers["Dividend"].isETF)
        self.assertEqual(False,self.valid_tickers["Non-Dividend"].isETF)
        self.assertEqual(True,self.valid_tickers["Index"].isETF)

    def test__generate_price_frame(self):
        pass

    def test__generate_div_frame(self):
        pass

    def test__cagr(self):
        pass

    def test__comparison_metrics(self):
        pass

    def test__str__(self):
        pass

if __name__ == '__main__':
  unittest.main()
