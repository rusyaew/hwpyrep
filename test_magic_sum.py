from unittest import TestCase
from main import magic_sum


class Test(TestCase):
    def test_magic_sum(self):
        expected = 12
        result = magic_sum(2, 4, 6)
        self.assertEqual(expected, result)
