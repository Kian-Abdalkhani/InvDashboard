import unittest
from src import Stock,Ticker

class TestStock(unittest.TestCase):
    tick = Stock(Ticker("GME"))


if __name__ == '__main__':
  unittest.main()