import unittest

from fild.tests.data import Mix


class TestFullParam(unittest.TestCase):
    mix = Mix()
    mix_full = Mix(is_full=True)

    def test_generated_array_is_full_false(self):
        self.assertFalse(self.mix_full.OptBaseArray[0].is_full)

    def test_generated_array_is_full_true(self):
        self.assertTrue(self.mix.ReqFullBaseArray[0].is_full)


if __name__ == '__main__':
    unittest.main()
