import unittest

from fild.sdk.array import Array
from fild.tests.data import AllowedNone, Mix, Optional


class TestValue(unittest.TestCase):
    def test_required_value(self):
        self.assertIsNotNone(Mix().ReqBase.value)

    def test_required_embedded_field_value(self):
        self.assertIsNotNone(Mix().ReqBase.StringField.value)

    def test_optional_no_value(self):
        self.assertIsNone(Mix().OptBase.value)

    def test_optional_embedded_field_no_value(self):
        self.assertIsNone(Mix().OptBase.IntField.value)

    def test_optional_value_in_full(self):
        self.assertIsNotNone(Mix(is_full=True).OptBase.value)

    def test_optional_embedded_field_in_full(self):
        self.assertIsNotNone(Mix(is_full=True).OptBase.IntField.value)

    def test_array_value(self):
        self.assertIsNotNone(Mix().ReqTypeArray.value)

    def test_optional_array_no_value(self):
        self.assertIsNone(Mix().OptBaseArray.value)

    def test_optional_array_in_full(self):
        self.assertIsNotNone(Mix(is_full=True).OptBaseArray.value)

    def test_optional_field_in_array_no_value(self):
        self.assertIsNone(Array(Optional)[0].OptString.value)

    def test_optional_field_in_array_value_in_full(self):
        self.assertIsNotNone(
            Array(Optional, is_full=True)[0].OptString.value
        )

    def test_required_dict_with_optional_fields(self):
        self.assertEqual(Mix().ReqOptional.value, {})

    def test_allownone_value_in_dict(self):
        self.assertEqual(AllowedNone().value, {
            AllowedNone.NoneString.name: None,
            AllowedNone.NoneInt.name: None,
        })

if __name__ == '__main__':
    unittest.main()
