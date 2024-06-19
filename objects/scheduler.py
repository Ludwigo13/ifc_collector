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

    def __is_initialized(self) -> None:
        if any(arg is None for arg in (self.start_time, self.end_time, self.interval)):
            raise ValueError("Class not initialize correctly")

    def __str__(self):
        return f"Start : {self.start_time}, End: {self.end_time}, interval: {self.interval}"


if __name__ == '__main__':
    scheduler = Scheduler(timedelta(hours=10), timedelta(hours=16), 100)
    scheduler.generate()
    schedule_path = "../data/schedule.txt"
    scheduler.write_txt(schedule_path)

    new_scheduler = Scheduler()
    new_scheduler.read_txt(schedule_path)
    print(scheduler.scheduled_times)
    print(new_scheduler.scheduled_times)

    print(scheduler)
    print(new_scheduler)
