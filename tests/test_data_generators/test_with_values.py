import unittest

from tests.data import Base, Mix, Optional


class TestWithValues(unittest.TestCase):
    def test_required_fields_with_values(self):
        new_value = 'my_new_value'
        entity = Base().with_values({Base.StringField.name: new_value})
        self.assertEqual(entity.StringField.value, new_value)

    def test_optional_field_with_values_generated(self):
        entity = Optional().with_values(
            {Optional.OptString.name: 'test_value'})
        self.assertTrue(entity.OptString.generated)

    def test_optional_field_with_values_new_value(self):
        new_value = 'optional_string'
        entity = Optional().with_values({Optional.OptString.name: new_value})
        self.assertEqual(entity.OptString.value, new_value)

    def test_embedded_dict_with_values_dict_generated(self):
        entity = Mix().with_values({
            Mix.OptBase.name: {Base.StringField.name: 'test_string'},
        })
        self.assertTrue(entity.OptBase.generated)

    def test_embedded_dict_with_values_field_generated(self):
        entity = Mix().with_values({
            Mix.OptBase.name: {Base.StringField.name: 'test_val'},
        })
        self.assertTrue(entity.OptBase.StringField.generated)

    def test_embedded_dict_with_values_field_not_affect_other_generated(self):
        entity = Mix().with_values({
            Mix.OptBase.name: {Base.StringField.name: 'value'},
        })
        self.assertFalse(entity.OptBase.IntField.generated)

    def test_embedded_dict_with_values_new_value(self):
        new_value = 'embedded_dict_string'
        entity = Mix().with_values({
            Mix.OptBase.name: {
                Base.StringField.name: new_value,
            },
        })
        self.assertEqual(entity.OptBase.StringField.value, new_value)

    def test_embedded_dict_with_values_new_dictionary_value(self):
        new_value = 'new_dict_string'
        entity = Mix().with_values({
            Mix.OptBase.name: {
                Base.StringField.name: new_value,
            },
        })
        self.assertEqual(
            entity.OptBase.value, {Base.StringField.name: new_value}
        )

    def test_array_of_fields_with_values_is_generated(self):
        entity = Mix().with_values({
            Mix.OptTypeArray.name: ['random_str1', 'random_str2'],
        })
        self.assertTrue(entity.OptTypeArray.generated)

    def test_array_of_fields_with_values_value(self):
        new_values = ['str1', 'str2', 'str3']
        entity = Mix().with_values({Mix.OptTypeArray.name: new_values})
        self.assertEqual(entity.OptTypeArray.value, new_values)

    def test_array_of_fields_with_values_override_value(self):
        new_values = ['r_str1', 'r_str2', 'r_str3']
        entity = Mix().with_values({Mix.ReqTypeArray.name: new_values})
        self.assertEqual(entity.ReqTypeArray.value, new_values)

    def test_array_of_dicts_with_values_is_generated(self):
        entity = Mix().with_values({Mix.OptBaseArray.name: [
            {Base.StringField.name: 'randoms_name1'},
            {Base.StringField.name: 'randoms_name2'},
        ]})
        self.assertTrue(entity.OptBaseArray.generated)

    def test_array_of_dicts_with_value_is_generated(self):
        entity = Mix().with_values({Mix.OptBaseArray.name: [
            {Base.StringField.name: 'name1', Base.IntField.name: 1},
            {Base.StringField.name: 'name2', Base.IntField.name: 2},
        ]})
        self.assertEqual(entity.OptBaseArray.value, [
            {"string_field": 'name1', "int_field": 1},
            {"string_field": 'name2', "int_field": 2}
        ])


if __name__ == '__main__':
    unittest.main()
