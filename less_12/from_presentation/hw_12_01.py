#создать таблицу со студентами в БД

import sqlite3


def get_data_from_table(conn: sqlite3.Connection, table_name: str):
    curs = conn.cursor()
    curs.execute(f"""SELECT * FROM {table_name}""")
    return curs.fetchall()


def create_table(conn: sqlite3.Connection, table_name: str):
    curs = conn.cursor()
    curs.execute(
        f"""CREATE TABLE {table_name}(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        specialty TEXT
        );
        """
    )
    conn.commit()
    return curs.fetchall()


def insert_data_to_table(conn: sqlite3.Connection, table_name: str):
    curs = conn.cursor()
    curs.execute(
        f"""INSERT INTO {table_name} (name, age, specialty)
        VALUES 
        ('Yulia', 18, 'math'),
        ('Alex', 19, 'chemistry'),
        ('Nika', 17, 'math');
        """)
    conn.commit()
    return curs.fetchall()


def main():
    conn = sqlite3.connect('hwtable.sqlite')
    try:
        table_name = 'students'
        create_table(conn, table_name)

        insert_data_to_table(conn, table_name)

        assert len(get_data_from_table(conn, table_name)) > 0

    except:
        conn.rollback()
    finally:
        conn.close()


main()
