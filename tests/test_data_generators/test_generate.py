import unittest

from tests.data import AllowedNone, ComposeOptional, Mix, Optional


class TestGenerate(unittest.TestCase):
    def test_generate_field_is_generated(self):
        entity = Optional()
        entity.OptInt.generate()
        self.assertTrue(entity.OptInt.generated)

    def test_generate_field_value(self):
        entity = Optional()
        entity.OptInt.generate()
        self.assertIsNotNone(entity.OptInt.value)

    def test_generate_field_not_affect_other_generated(self):
        entity = Optional()
        entity.OptInt.generate()
        self.assertFalse(entity.OptString.generated)

    def test_generated_field_not_affect_other_values(self):
        entity = Optional()
        entity.OptInt.generate()
        self.assertIsNone(entity.OptString.value)

    def test_generate_embedded_field_dictionary_is_generated(self):
        entity = ComposeOptional()
        entity.OptionalOpt.OptString.generate()
        self.assertTrue(entity.OptionalOpt.generated)

    def test_generate_embedded_field_dictionary_value(self):
        entity = ComposeOptional()
        entity.OptionalOpt.OptString.generate()
        self.assertNotEqual(entity.OptionalOpt.value, {})

    def test_generate_embedded_field_is_generated(self):
        entity = ComposeOptional()
        entity.OptionalOpt.OptString.generate()
        self.assertTrue(entity.OptionalOpt.OptString.generated)

    def test_generate_embedded_field_value(self):
        entity = ComposeOptional()
        entity.OptionalOpt.OptString.generate()
        self.assertIsNotNone(entity.OptionalOpt.OptString.value)

    def test_generate_embedded_field_not_affect_other_is_generated(self):
        entity = ComposeOptional()
        entity.OptionalOpt.OptString.generate()
        self.assertFalse(entity.OptionalOpt.OptInt.generated)

    def test_generate_embedded_field_not_affect_other_value(self):
        entity = ComposeOptional()
        entity.OptionalOpt.OptString.generate()
        self.assertIsNone(entity.OptionalOpt.OptInt.value)

    def test_generate_dictionary_is_generated(self):
        entity = Mix()
        entity.OptBase.generate()
        self.assertTrue(entity.OptBase.generated)

    def test_generated_dictionary_value(self):
        entity = Mix()
        entity.OptBase.generate()
        self.assertNotEqual(entity.OptBase.value, {})

    def test_generate_optional_dictionary_is_generated(self):
        entity = Mix()
        entity.OptOptional.generate()
        self.assertTrue(entity.OptOptional.generated)

    def test_generate_optional_dictionary_value(self):
        entity = Mix()
        entity.OptOptional.generate()
        self.assertEqual(entity.OptOptional.value, {})

    def test_generate_allow_none_value(self):
        entity = AllowedNone()
        entity.NoneString.generate()
        self.assertTrue(entity.NoneString.generated)


if __name__ == '__main__':
    unittest.main()
