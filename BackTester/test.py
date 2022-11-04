import unittest
import sys, os
import backtester


sys.path.append('/BackTester/backtester')

class TestTrades(unittest.TestCase):

    def test_Trade_init(self):
        trades = backtester.Trades(amount=1, fee=1)
        self.assertEqual(trades.tradeNums, 0)


if __name__ == '__main__':
    unittest.main()