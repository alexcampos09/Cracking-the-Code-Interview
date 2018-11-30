def compress(string):
    char = string[0]
    count = 1
    s = ''
    for l in string[1::]:
        if l == char:
            count += 1
        else:
            s += f'{char}{count}'
            char, count = l, 1
    s += f'{char}{count}'
    return s if len(s) < len(string) else string


import unittest

class Test(unittest.TestCase):
    def test_compression(self):
        self.assertEqual(compress('AAAABBBCCDDDEEEE'), 'A4B3C2D3E4')
        self.assertEqual(compress('ABCDE'), 'ABCDE')
        self.assertEqual(compress('AAAaaa'), 'A3a3')
        self.assertEqual(compress('AAAAbbB'), 'A4b2B1')
        self.assertEqual(compress('AAbbB'), 'AAbbB')

if __name__ == "__main__":
  unittest.main()
