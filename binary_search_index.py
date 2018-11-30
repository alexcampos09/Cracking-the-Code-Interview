def binary_search(array, value):
    index = int(len(array)/2) -1
    end = int(len(array)) - 1
    while array[index] != value:
        if index == end:
            return None
        elif array[index] > value:
            end = index
            index = int(index/2)
        elif array[index] < value:
            index = int((index+1 + end)/2)
    return index

import unittest
class Test(unittest.TestCase):
    def test_binary_search(self):
        array = [-2893,-342,-23,-1,0,1,2,3,4,5,6,7,8,9,10,30,100,10023]
        self.assertEqual(binary_search(array, 1), 5)
        self.assertEqual(binary_search(array, 2), 6)
        self.assertEqual(binary_search(array, 3), 7)
        self.assertEqual(binary_search(array, 4), 8)
        self.assertEqual(binary_search(array, 5), 9)
        self.assertEqual(binary_search(array, 6), 10)
        self.assertEqual(binary_search(array, -2893), 0)
        self.assertEqual(binary_search(array, -1), 3)
        self.assertEqual(binary_search(array, 0), 4)
        self.assertEqual(binary_search(array, 10023), 17)
        self.assertEqual(binary_search(array, -2), None)
        self.assertEqual(binary_search(array, 101), None)
        self.assertEqual(binary_search(array, 100000), None)

if __name__ == "__main__":
  unittest.main()
