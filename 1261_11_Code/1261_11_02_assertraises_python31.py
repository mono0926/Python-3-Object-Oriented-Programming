import unittest

def average(seq):
    return sum(seq) / len(seq)

class TestAverage(unittest.TestCase):
    def test_python30_zero(self):
        self.assertRaises(ZeroDivisionError,
                average,
                [])

    def test_python31_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

if __name__ == "__main__":
    unittest.main()
