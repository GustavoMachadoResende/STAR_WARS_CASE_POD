import unittest


class TestRepository(unittest.TestCase):

    def test_soma(self):
        result = 4 + 4
        expected = 8
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()