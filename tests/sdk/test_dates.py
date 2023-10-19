import datetime

from fild.sdk import dates


def test_get_current_time_utc():
    current_time = datetime.datetime.utcnow()
    got_time = dates.get_current_time_utc()
    assert got_time - current_time < datetime.timedelta(seconds=3)


def test_generate_date():
    got_date = dates.generate_date()
    assert isinstance(got_date, datetime.date)


def test_to_timestamp():
    current_time = datetime.datetime.utcnow()
    got_ts = dates.to_timestamp(current_time)
    assert isinstance(got_ts, int)


def test_str_to_date():
    got_date = dates.str_to_date('2021-04-21', dates.Pattern.DATE)
    assert isinstance(got_date, datetime.datetime)


def test_to_timezone():
    current_time = datetime.datetime.utcnow()
    got_datetime = dates.to_timezone(current_time, 'US/Eastern')
    assert got_datetime.tzinfo.zone == 'US/Eastern'
