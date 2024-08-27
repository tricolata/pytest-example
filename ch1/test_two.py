import unittest

class TestSum2(unittest.TestCase):
    def test_occurance(self):
        self.assertIn(1, [1,2,3], "1 should be in container")

    def test_greater(self):
        self.assertGreaterEqual(7, 5)

    def test_str(self):
        self.assertNotIn('s', 'helloworld')

if __name__ == '__main__':
    unittest.main()