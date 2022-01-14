import random

from sdk.field import Field


class Array(Field):
    def __init__(self, field, name=None, required=True, allow_none=False,
                 is_full=False, is_optional=False, min_len=1, max_len=1):
        if not hasattr(self, '_kwargs'):
            self.save_kwargs(locals())

        self.is_full = is_full
        self._field = field
        self.min_len = min_len
        self.max_len = max_len
        super(Array, self).__init__(name, required, allow_none)

    @property
    def field(self):
        if not isinstance(
                self._field, Field) and issubclass(self._field, Field):
            self._field = self._field()

        return self._field

    @property
    def value(self):
        if self._value is None:
            return None

        return [field.value for field in self._value]

    @property
    def full_value(self):
        if self._value is None:
            return []

        return [field.full_value for field in self._value]

    def generate_value(self):
        pass

    def _generate(self, is_full=False, with_data=True, required=True,
                  use_default=None):
        # TODO duplicated entities, duplicated empty dicts
        if with_data and (is_full or required):
            self._value = [self.field(is_full=is_full) for _ in range(
                random.randint(self.min_len, self.max_len)
            )]

    def generate(self, is_full=False):
        self._generate(is_full=is_full)

    def __len__(self):
        return len(self._value)

    def __getitem__(self, item):
        return self._value[item]  # Return Field to provide attribute access

    def __setitem__(self, key, value):
        self._value[key] = value

    def __iter__(self):
        return iter(self._value)

    def append(self, value):
        self._value.append(value)

    def with_values(self, values):
        if isinstance(values, list):
            _values = []

            for value in values:
                if not isinstance(value, self.field.__class__):
                    value = self.field(is_full=False).with_values(value)
                _values.append(value)
            self._value = _values

            return self
        else:
            return super(Array, self).with_values(values)
