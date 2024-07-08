import sqlite3

def create_db():
    conn = sqlite3.connect('CollecteDeDonneeProject.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE ifc_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            previous_close TEXT,
            open_price TEXT,
            bid TEXT,
            ask TEXT,
            days_range TEXT,
            week_52_range TEXT,
            volume TEXT,
            avg_volume TEXT,
            market_cap TEXT,
            beta TEXT,
            pe_ratio TEXT,
            eps TEXT,
            earnings_date TEXT,
            forward_dividend_yield TEXT,
            ex_dividend_date TEXT,
            target_est TEXT,
            date TEXT,
            time TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_db()


