import unittest
from src import Etf,Ticker

class TestEtf(unittest.TestCase):
    tick = Etf(Ticker("UVXY"))


if __name__ == '__main__':
  unittest.main()