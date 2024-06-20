from objects.scheduler import Scheduler
from datetime import timedelta
import utils.converter as convert


if __name__ == '__main__':
    generate_dates = (
        "20-06-2024",
        "21-06-2024",
        "22-06-2024"
    )

    for date in generate_dates:
        scheduler = Scheduler(timedelta(hours=9, minutes=30), timedelta(hours=16), 100, convert.to_date(date))
        scheduler.generate()
        schedule_path = f"data/{date}.txt"
        scheduler.write_txt(schedule_path)
