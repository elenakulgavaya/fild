import unittest

from src.fild.sdk.array import Array
from tests.data import Base, ComposeBase, Mix, Optional, TypeOne


class TestGenerated(unittest.TestCase):
    def test_field_generated(self):
        self.assertTrue(TypeOne().generated)

    def test_embedded_field_generated(self):
        self.assertTrue(Base().IntField.generated)

    def test_optional_field_not_generated(self):
        self.assertFalse(Optional().OptString.generated)

    def test_optional_field_generated_in_full(self):
        self.assertTrue(Optional(is_full=True).OptString.generated)

    def test_dict_generated(self):
        self.assertTrue(ComposeBase().generated)

    def test_embedded_dict_generated(self):
        self.assertTrue(ComposeBase().FirstBase.generated)

    def test_embedded_optional_dict_not_generated(self):
        self.assertFalse(ComposeBase().OptBase.generated)

    def test_embedded_optional_dict_generated_in_full(self):
        self.assertTrue(ComposeBase(is_full=True).OptBase.generated)

    def test_array_generated(self):
        self.assertTrue(Array(Base).generated)

    def test_array_dict_generated(self):
        self.assertTrue(Array(Base)[0].generated)

    def test_array_embedded_field_generated(self):
        self.assertTrue(Array(Base)[0].StringField.generated)

    def test_array_optional_not_generated(self):
        self.assertFalse(Array(ComposeBase)[0].OptBase.generated)

    def test_array_optional_generated_in_full(self):
        self.assertTrue(
            Array(ComposeBase, is_full=True)[0].OptBase.generated
        )

    def test_optional_array_not_generated(self):
        self.assertFalse(Mix().OptFullBaseArray.generated)

    def test_optional_array_generated_in_full(self):
        self.assertTrue(Mix(is_full=True).OptFullBaseArray.generated)

    def test_optional_allownone_not_generated(self):
        self.assertFalse(Mix().NotNoneAllowedNone.OptNoneInt.generated)

    def test_optional_allownone_generated_in_full(self):
        self.assertTrue(
            Mix(is_full=True).NotNoneAllowedNone.OptNoneInt.generated
        )


if __name__ == '__main__':
    unittest.main()
