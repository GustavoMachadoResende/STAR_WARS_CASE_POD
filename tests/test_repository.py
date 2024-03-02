import unittest
from api.src.repository import soma


class TestRepository(unittest.TestCase):

    def test_soma(self):
        result = soma(5, 3)
        expected = 8
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()