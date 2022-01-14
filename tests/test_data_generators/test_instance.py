import unittest

from tests.data import Base, ComposeBase, Mix


class TestInstance(unittest.TestCase):
    base = Base()
    compose_base = ComposeBase()
    mix = Mix()
    mix_full = Mix(is_full=True)

    def test_generated_field(self):
        self.assertIsNot(id(self.base.StringField.value),
                         id(self.compose_base.FirstBase.StringField.value))

    def test_generated_embedded_field(self):
        self.assertIsNot(id(self.base.StringField.value),
                         id(self.compose_base.FirstBase.StringField.value))

    def test_generated_array(self):
        self.assertIsNot(self.mix.ReqBaseArray.value,
                         self.mix_full.ReqFullBaseArray.value)

    def test_array_contract(self):
        self.assertIsNot(id(self.mix.ReqTypeArray.field.value),
                         id(self.mix.ReqTypeArray[0].value))


if __name__ == '__main__':
    unittest.main()
