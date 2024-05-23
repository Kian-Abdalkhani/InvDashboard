import unittest
from id_stock import id_ticker
from src import (DividendEtf,
                   Etf,
                   DividendStock,
                   Stock,)

    
class TestIDStock(unittest.TestCase):

    def test_id_ticker(self):
        etf_no_div = id_ticker("UVXY")
        stock_no_div = id_ticker("GME")
        etf_div = id_ticker("SCHD")
        stock_div = id_ticker("BAC")
        
        self.assertEqual(True, isinstance(etf_no_div,Etf))
        self.assertEqual(True, isinstance(stock_no_div,Stock))
        self.assertEqual(True, isinstance(etf_div,DividendEtf))
        self.assertEqual(True, isinstance(stock_div,DividendStock))



if __name__ == '__main__':
  unittest.main()
