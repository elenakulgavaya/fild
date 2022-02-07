import unittest

from tests.data import Mix


class TestFullParam(unittest.TestCase):
    def test_array_is_full_false(self):
        self.assertFalse(Mix.OptBaseArray.field.is_full)

    def test_array_is_full_true(self):
        self.assertTrue(Mix.OptFullBaseArray.field.is_full)


if __name__ == '__main__':
    unittest.main()
