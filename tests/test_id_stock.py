import unittest
from id_stock import id_ticker
from tickertypes.etf import Etf
from tickertypes.dividendetf import DividendEtf
from tickertypes.dividendstock import DividendStock
from tickertypes.stock import Stock

etfs_no_div = ["UVXY","SCO","TSLZ"]
stocks_no_div = ["GME","TSLA","AMC"]
etfs_div = ["SCHD","VOO","QQQ"]
stocks_div = ["MSFT","BAC","O"]

class TestIDStock(unittest.TestCase):

  def test_etfs_no_div(self):
      """Tests if ETFs without dividends are correctly classified as Etf."""
      for ticker in etfs_no_div:
          self.assertIsInstance(id_ticker(ticker), Etf, f"{ticker} should be an Etf")

  def test_etfs_div(self):
      """Tests if ETFs with dividends are correctly classified as DividendEtf."""
      for ticker in etfs_div:
          self.assertIsInstance(id_ticker(ticker), DividendEtf, f"{ticker} should be a DividendEtf")

  def test_stocks_no_div(self):
      """Tests if stocks without dividends are correctly classified as Stock."""
      for ticker in stocks_no_div:
          self.assertIsInstance(id_ticker(ticker), Stock, f"{ticker} should be a Stock")

  def test_stocks_div(self):
      """Tests if stocks with dividends are correctly classified as DividendStock."""
      for ticker in stocks_div:
          self.assertIsInstance(id_ticker(ticker), DividendStock, f"{ticker} should be a DividendStock")




if __name__ == '__main__':
  unittest.main()
