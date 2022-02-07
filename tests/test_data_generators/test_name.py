import unittest

from tests.data import Mix


class TestName(unittest.TestCase):
    mix = Mix()
    mix_full = Mix(is_full=True)

    def test_generated_dict_name(self):
        self.assertEqual(self.mix_full.OptBase.name, Mix.OptBase.name)

    def test_generated_embedded_dict_name(self):
        self.assertEqual(self.mix.ReqOptional.OptInt.name,
                         Mix.ReqOptional.OptInt.name)

    def test_generated_array_name(self):
        self.assertEqual(self.mix.OptFullBaseArray.name,
                         Mix.OptFullBaseArray.name)

    def test_generated_embedded_array_dict_name(self):
        self.assertEqual(self.mix_full.OptBaseArray[0].StringField.name,
                         Mix.OptBaseArray.field.StringField.name)


if __name__ == '__main__':
    unittest.main()
