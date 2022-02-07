import decimal
import random


from fild.sdk import fakeable, dates
from fild.sdk.field import Field
from fild.process import dictionary


class Bool(Field):
    def generate_value(self):
        return fakeable.FAKER.boolean()


class Int(Field):
    def __init__(self, name=None, required=True, allow_none=False,
                 min_val=None, max_val=None, default=None):
        self.save_kwargs(locals())
        self.min_val = min_val or 0
        self.max_val = max_val or 9999
        super().__init__(
            name=name, required=required, allow_none=allow_none,
            default=default
        )

    def generate_value(self):
        return fakeable.FAKER.pyint(
            min_value=self.min_val,
            max_value=self.max_val
        )


class Float(Field):
    def __init__(self, name=None, required=True, allow_none=False, i_len=None,
                 f_len=None, min_val=None, max_val=None, positive=None,
                 default=None):
        self.save_kwargs(locals())
        self.i_len = i_len
        self.f_len = f_len
        self.min_val = min_val
        self.max_val = max_val
        self.positive = positive
        super().__init__(
            name=name, required=required, allow_none=allow_none,
            default=default
        )

    def generate_value(self):
        return fakeable.FAKER.pyfloat(
            left_digits=self.i_len,
            right_digits=self.f_len,
            positive=bool(self.positive),
            min_value=self.min_val,
            max_value=self.max_val
        )


class Decimal(Float):
    def generate_value(self):
        return fakeable.FAKER.pydecimal(
            left_digits=self.i_len or 1,
            right_digits=self.f_len,
            positive=self.positive is None or self.positive,
            min_value=self.min_val,
            max_value=self.max_val
        )

    @staticmethod
    def from_value(value):
        if isinstance(value, (str, float)):
            value = decimal.Decimal(str(value))

        return Decimal().with_values(value)


class StringDecimal(Decimal):
    @property
    def value(self):
        if self._value in [None, '']:
            return self._value

        return f'{float(self._value):.{self.f_len or 2}f}'


class String(Field):
    def __init__(self, name=None, required=True, min_len=0,
                 max_len=None, allow_none=False, default=None, fake_as=None):
        self.save_kwargs(locals())
        self.min_len = min_len
        self.max_len = max_len
        self.fake_as = fake_as
        super().__init__(
            name=name, required=required, allow_none=allow_none,
            default=default
        )

    def generate_value(self):
        return fakeable.fake_string_attr(
            self.fake_as or self.name,
            min_len=self.min_len,
            max_len=self.max_len
        )


class Enum(Field):
    def __init__(self, name=None, required=True, allow_none=False,
                 default=None, exclude=None):
        self.save_kwargs(locals())
        self.exclude = exclude or ()
        super().__init__(
            name=name, required=required, allow_none=allow_none,
            default=default
        )

    @classmethod
    def _attr_values_as_list(cls):
        result = []

        for attr_name in dir(cls):
            if not attr_name.startswith('_'):
                attr_value = getattr(cls, attr_name)

                if (not callable(attr_value) and
                        not isinstance(attr_value, property)):
                    result.append(attr_value)

        return result

    @classmethod
    def to_list(cls, exclude=()):
        """
        :param exclude: list of values to be excluded from result; if
          not existent value passed, ValueError exception will be thrown
        :return: list of all fields of class A(Enum) and its parents
        """
        result = cls._attr_values_as_list()
        if type(exclude) not in (list, tuple):
            exclude = (exclude,)

        for item in exclude:
            result.remove(item)

        return result

    def generate_value(self):
        return random.choice(self.__class__.to_list(
            exclude=self.exclude
        ))


class Raw(String):
    def __init__(self, name=None, required=True, allow_none=False):
        self.save_kwargs(locals())
        self.overrided_values = False
        self._value = None
        super().__init__(
            name=name, required=required, allow_none=allow_none
        )

    def generate_value(self):
        return fakeable.FAKER.pydict(10, True, str)

    def with_values(self, values):
        if self.overrided_values and isinstance(self._value, dict):
            self._value = dictionary.merge_with_updates(self._value, values)
        else:
            self._value = values

        self.overrided_values = True

        return self


class Uuid(Field):
    @staticmethod
    def generate_value():
        return fakeable.FAKER.uuid4()


class DateTime(Field):
    @staticmethod
    def generate_value():
        return dates.generate_time()

    @property
    def value(self):
        return dates.to_format(self._value)
