import unittest

from tests.data import Mix


class TestAllowNoneParam(unittest.TestCase):
    def test_dict_is_not_allowed_none(self):
        self.assertFalse(Mix.NotNoneAllowedNone.allow_none)

    def test_embedded_dict_is_allowed_none(self):
        self.assertTrue(Mix.NoneAllowedNone.allow_none)

    def test_embedded_in_dict_is_allowed_none(self):
        self.assertTrue(Mix.NoneAllowedNone.NoneString.allow_none)

    def test_array_none_is_allowed(self):
        self.assertTrue(Mix.NoneTypeArray.allow_none)

    def test_embedded_array_none_is_allowed(self):
        self.assertTrue(Mix.NoneTypeArray.field.NoneInt.allow_none)


if __name__ == '__main__':
    unittest.main()
