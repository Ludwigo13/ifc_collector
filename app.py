from objects.dto import IFC_DTO
from objects.collector_mod import Collector
from objects.scheduler import Scheduler
import sqlite3
import pandas as pd


def view_data():
    conn = sqlite3.connect('data\\CollecteDeDonneeProject.db')

    df = pd.read_sql_query('SELECT * FROM ifc_data', conn)

    print(df)

    conn.close()


if __name__ == '__main__':
    dates = (
        "9-07-2024",
        "10-07-2024"
    )

    for date in dates:
        schedule = Scheduler()
        schedule.read_txt(f"data\\{date}.txt")

        while schedule.wait_next_scheduled_time():
            collector = Collector('https://ca.finance.yahoo.com/quote/IFC.TO')
            data = collector.get_summary()

            dto = IFC_DTO.map_to_dto(data)
            dto.insert_into_db()
