import time
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
    collector = Collector('https://ca.finance.yahoo.com/quote/IFC.TO')
    data = collector.get_summary()
    print(data)

    dto = IFC_DTO.map_to_dto(data)
    dto.insert_into_db()

    view_data()
