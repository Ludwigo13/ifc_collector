from datetime import datetime, timedelta


def to_timedelta(str_time) -> timedelta:
    time_format = "%H:%M:%S"
    tmp_datetime = datetime.strptime(str_time, time_format)
    return timedelta(hours=tmp_datetime.hour, minutes=tmp_datetime.minute, seconds=tmp_datetime.second)


def add_timedelta_to_datetime(start_date: datetime, time: timedelta) -> datetime:
    return datetime(start_date.year, start_date.month, start_date.day) + time

def to_date(str_date) -> datetime:
    date_format = "%d-%m-%Y"
    return datetime.strptime(str_date, date_format)

def to_datetime(str_date) -> datetime:
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    return datetime.strptime(str_date, date_format)
