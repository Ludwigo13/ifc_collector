from objects.dto import IFC_DTO
from utils.collector_mod import Collector
import sqlite3
import pandas as pd

def view_data():
    conn = sqlite3.connect('CollecteDeDonneeProject.db')

    df = pd.read_sql_query('SELECT * FROM ifc_data', conn)

    print(df)

    conn.close()

if __name__ == '__main__':
    collector = Collector('https://ca.finance.yahoo.com/quote/IFC.TO')
    data = collector.get_summary()

    dto = IFC_DTO.map_to_dto(data)
    dto.insert_into_db()

    view_data()
    #print(f'Data inserted: {dto.to_tuple()}')


