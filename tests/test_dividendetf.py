import unittest
from src import DividendEtf,Ticker

class TestDividendEtf(unittest.TestCase):
    tick = DividendEtf(Ticker("SCHD"))

if __name__ == '__main__':
  unittest.main()