import time
from datetime import datetime, timedelta
from random import uniform


class Scheduler:
    def __init__(self, start_time: timedelta = None, end_time: timedelta = None, interval: int = None):
        if any(arg is not None for arg in (start_time, end_time, interval)) and not all(
                arg is not None for arg in (start_time, end_time, interval)):
            raise ValueError("You must provide either all three arguments or none.")

        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.scheduled_times = []
        self.consumed_scheduled_times = 0
        self.start_date = None

    def generate(self) -> None:
        self.__is_initialized()
        time_diff = self.end_time - self.start_time
        time_interval = time_diff / self.interval
        for i in range(self.interval):
            random_time = timedelta(seconds=int(uniform(0, time_interval.total_seconds())))
            scheduled_time = (time_interval * i) + random_time + self.start_time
            self.scheduled_times.append(scheduled_time)

    def write_txt(self, filepath) -> None:
        self.__is_initialized()
        output = f'{self.start_time};{self.end_time};{self.interval};' + ';'.join(map(str, self.scheduled_times))
        with open(filepath, "w") as file:
            file.write(output)

    def read_txt(self, filepath) -> None:
        with open(filepath, "r") as file:
            times = str(file.readline()).split(';')
        self.start_time = self.convert_to_timedelta(times[0])
        self.end_time = self.convert_to_timedelta(times[1])
        self.interval = int(times[2])
        for i, time in enumerate(times[3:]):
            self.scheduled_times.append(self.convert_to_timedelta(time))

    @staticmethod
    def convert_to_timedelta(str_time) -> timedelta:
        time_format = "%H:%M:%S"
        tmp_datetime = datetime.strptime(str_time, time_format)
        return timedelta(hours=tmp_datetime.hour, minutes=tmp_datetime.minute, seconds=tmp_datetime.second)

    def convert_to_datetime(self, timedelta: timedelta) -> datetime:
        return datetime(self.start_date.year, self.start_date.month, self.start_date.day) + timedelta

    def __is_initialized(self) -> None:
        if any(arg is None for arg in (self.start_time, self.end_time, self.interval)):
            raise ValueError("Class not initialize correctly")

    def __str__(self):
        return f"Start : {self.start_time}, End: {self.end_time}, interval: {self.interval}"

    def wait_next_scheduled_time(self) -> bool:
        if self.start_date is None:
            raise ValueError("start_date can't be empty")
        if not isinstance(self.start_date, datetime):
            raise ValueError("start_date is not a datetime")

        if self.consumed_scheduled_times == len(self.scheduled_times):
            return False

        now = datetime.now()
        diff_seconds = (self.convert_to_datetime(self.scheduled_times[self.consumed_scheduled_times]) - now).total_seconds()
        print(f"Wait {diff_seconds}")
        time.sleep(diff_seconds)
        self.consumed_scheduled_times += 1
        return True


if __name__ == '__main__':
    scheduler = Scheduler(timedelta(hours=10), timedelta(hours=16), 100)
    scheduler.generate()
    schedule_path = "../data/schedule.txt"
    scheduler.write_txt(schedule_path)
    scheduler.start_date = datetime.now() + timedelta(hours=12)

    new_scheduler = Scheduler()
    new_scheduler.read_txt(schedule_path)
    print(scheduler.scheduled_times)
    print(new_scheduler.scheduled_times)

    print(scheduler)
    print(new_scheduler)

    while scheduler.wait_next_scheduled_time():
        pass
