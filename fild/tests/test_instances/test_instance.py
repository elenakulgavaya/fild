import unittest

from fild.tests.data import Base, ComposeBase, ComposeOptional, Mix, Optional


class TestInstance(unittest.TestCase):
    def test_field(self):
        self.assertNotEqual(id(Base.StringField), id(Optional.OptString))

    def test_required_dict(self):
        self.assertNotEqual(id(ComposeBase.FirstBase),
                            id(ComposeBase.SecondBase))

    def test_optional_dict(self):
        self.assertNotEqual(id(ComposeOptional.FirstOpt),
                            id(ComposeOptional.OptionalOpt))

    def test_embedded(self):
        self.assertNotEqual(id(Mix.ReqBase), id(ComposeBase.FirstBase))

    def test_field_array(self):
        self.assertNotEqual(id(Mix.OptTypeArray), id(Mix.OptBaseArray))

    def test_field_array_generator(self):
        self.assertNotEqual(id(Mix.OptTypeArray.field),
                            id(Mix.OptBaseArray.field))


if __name__ == '__main__':
    unittest.main()
