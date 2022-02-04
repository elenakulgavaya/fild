import unittest

from fild.tests.data import Mix


class TestName(unittest.TestCase):
    def test_dict_name(self):
        self.assertEqual(Mix.ReqBase.name, 'req_base')

    def test_embedded_dict_name(self):
        self.assertEqual(Mix.ReqOptional.OptString.name, 'opt_string')

    def test_array_name(self):
        self.assertEqual(Mix.OptBaseArray.name, 'opt_base_array')

    def test_embedded_array_dict_name(self):
        self.assertEqual(Mix.OptBaseArray.field.StringField.name,
                         'string_field')


if __name__ == '__main__':
    unittest.main()
