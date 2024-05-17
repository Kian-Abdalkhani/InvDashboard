# import setup_path
import unittest
from stock import (DividendEtf,
                   Etf,
                   DividendStock,
                   Stock,
                   id_ticker)

    
class IdentifierTest(unittest.TestCase):

    def test_id_ticker(self):
        etf_no_div = id_ticker("UVXY")
        stock_no_div = id_ticker("GME")
        etf_div = id_ticker("SCHD")
        stock_div = id_ticker("BAC")
        
        self.assertEqual(True, isinstance(etf_no_div,Etf))
        self.assertEqual(True, isinstance(stock_no_div,Stock))
        self.assertEqual(True, isinstance(etf_div,DividendEtf))
        self.assertEqual(True, isinstance(stock_div,DividendStock))

class TestEtf(unittest.TestCase):
    tick = Etf("UVXY")

class TestDividendEtf(unittest.TestCase):
    tick = DividendEtf("SCHD")

class TestStock(unittest.TestCase):
    tick = Stock("GME")

class TestDividendStock(unittest.TestCase):
    tick = DividendStock("BAC")



if __name__ == '__main__':
  unittest.main()
