import unittest
from src import DividendStock,Ticker

class TestDividendStock(unittest.TestCase):
    tick = DividendStock(Ticker("BAC"))


if __name__ == '__main__':
  unittest.main()