import unittest

from fild.tests.data import Mix


class TestRequiredParam(unittest.TestCase):
    mix = Mix()
    mix_full = Mix(is_full=True)

    def test_generated_dict_is_required(self):
        self.assertIs(self.mix_full.ReqOptional.required,
                      Mix.ReqOptional.required)

    def test_generated_embedded_dict_is_required(self):
        self.assertIs(Mix.OptOptional.OptString.required,
                      self.mix.OptOptional.OptString.required)

    def test_generated_embedded_optional_dict_is_required(self):
        self.assertIs(Mix.OptBase.IntField.required,
                      self.mix_full.OptBase.IntField.required)

    def test_generated_array_is_required(self):
        self.assertIs(Mix.OptFullBaseArray.required,
                      self.mix_full.OptFullBaseArray.required)

    def test_generated_embedded_array_dict_is_required(self):
        self.assertIs(Mix.OptBaseArray.field.StringField.required,
                      self.mix_full.OptBaseArray[0].StringField.required)


if __name__ == '__main__':
    unittest.main()
