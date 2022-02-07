import unittest

from tests.data import Base, ComposeBase, Mix


class TestValue(unittest.TestCase):
    def test_field_no_value(self):
        self.assertIsNone(Base.StringField.value)

    def test_embedded_dict_no_value(self):
        self.assertIsNone(ComposeBase.FirstBase.value)

    def test_embedded_dict_field_no_value(self):
        self.assertIsNone(ComposeBase.FirstBase.IntField.value)

    def test_array_no_value(self):
        self.assertIsNone(Mix.ReqFullBaseArray.value)


if __name__ == '__main__':
    unittest.main()
