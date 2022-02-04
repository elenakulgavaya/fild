import unittest

from fild.tests.data import Mix


class TestRequiredParam(unittest.TestCase):
    def test_dict_is_required(self):
        self.assertTrue(Mix.ReqOptional.required)

    def test_embedded_dict_is_not_required(self):
        self.assertFalse(Mix.OptOptional.OptString.required)

    def test_embedded_optional_dict_is_required(self):
        self.assertTrue(Mix.OptBase.IntField.required)

    def test_array_is_not_required(self):
        self.assertFalse(Mix.OptFullBaseArray.required)

    def test_embedded_array_dict_is_required(self):
        self.assertTrue(Mix.OptBaseArray.field.StringField.required)


if __name__ == '__main__':
    unittest.main()
