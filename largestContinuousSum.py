def largest_continuous_sum(l):
    sum_list = []
    sum = 0
    for i in l:
        if sum + i <= 0:
            sum_list.append(sum)
            sum = 0
        elif i < 0:
            sum_list.append(sum)
            sum += i
        else:
            sum += i
    sum_list.append(sum)
    return max(sum_list)


import unittest

class Test(unittest.TestCase):
    def test_largest_continuous_sum(self):
        self.assertEqual(largest_continuous_sum([7,8,9]), 24)
        self.assertEqual(largest_continuous_sum([-1,7,8,9,-10]), 24)
        self.assertEqual(largest_continuous_sum([2,3,-10,9,2]), 11)
        self.assertEqual(largest_continuous_sum([2,11,-10,9,2]), 14)
        self.assertEqual(largest_continuous_sum([12,-10,7,-8,4,6]), 12)

if __name__ == "__main__":
  unittest.main()
