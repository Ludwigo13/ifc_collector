from objects.scheduler import Scheduler
from datetime import timedelta
import utils.converter as convert


if __name__ == '__main__':
    generate_dates = (
        "9-07-2024",
        "10-07-2024"
    )
    interval = 100

    for date in generate_dates:
        scheduler = Scheduler(timedelta(hours=9, minutes=30),
                              timedelta(hours=16), interval=interval,
                              start_date=convert.to_date(date))
        scheduler.generate()
        schedule_path = f"data/{date}.txt"
        scheduler.write_txt(schedule_path)
