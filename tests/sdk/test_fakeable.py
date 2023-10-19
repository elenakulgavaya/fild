from fild.sdk import fakeable

from fild.sdk.fakeable import (
    Fakeable, fake_string_attr, generate_float, generate_string,
)


def test_generate_string_fixed_size():
    value = generate_string(size=28)
    assert len(value) == 28


def test_fake_attribute():
    value = fake_string_attr(Fakeable.CompanyEmail)
    assert '@' in value


def test_max_len_in_fake_attrs():
    value = fake_string_attr(Fakeable.Uuid, max_len=10)
    assert len(value) == 10


def test_generate_float_i_len():
    value = generate_float(i_len=3)
    assert len(str(value).split('.')[0]) <= 3


def test_generate_float_f_len():
    value = generate_float(f_len=5)
    assert len(str(value).split('.')[1]) <= 5


def test_generate_float_fixed_f_len(monkeypatch):
    monkeypatch.setattr(
        fakeable.random,
        'randint',
        lambda x, y: 1 if y < 10 else 10
    )
    value = generate_float(fixed_f_len=True, f_len=2, i_len=0,
                           integer_allowed=False)
    assert len(str(value).split('.')[1]) == 2

