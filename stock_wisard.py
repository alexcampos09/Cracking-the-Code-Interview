def stock_wisard(stocks):
    buy, sell = 0, 1
    final_buy, final_sell = 0, 1
    for i in range(2, len(stocks)):
        if stocks[i] < stocks[buy]:
            buy, sell = i, i
        elif stocks[sell] < stocks[i]:
            sell = i
        if stocks[sell] - stocks[buy] > stocks[final_sell] - stocks[final_buy]:
            final_buy, final_sell = buy, sell
    return [final_buy, final_sell]


import unittest

class Test(unittest.TestCase):
    def test_stock_wisard(self):
        self.assertEqual(stock_wisard([6,13,2,10,3,5]), [2,3])
        self.assertEqual(stock_wisard([6,13,100,2,10,3,5]), [0,2])
        self.assertEqual(stock_wisard([2,8,12]), [0,2])
        self.assertEqual(stock_wisard([1,20,5]), [0,1])

if __name__ == "__main__":
  unittest.main()
