import unittest

from fild.tests.data import Base, ComposeBase, Mix


class TestGenerated(unittest.TestCase):
    def test_field_not_generated(self):
        self.assertFalse(Base.StringField.generated)

    def test_embedded_dict_not_generated(self):
        self.assertFalse(ComposeBase.FirstBase.generated)

    def test_embedded_dict_field_not_generated(self):
        self.assertFalse(ComposeBase.FirstBase.IntField.generated)

    def test_array_not_generated(self):
        self.assertFalse(Mix.ReqFullBaseArray.generated)


if __name__ == '__main__':
    unittest.main()
