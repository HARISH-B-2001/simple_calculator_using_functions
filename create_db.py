import sqlite3
from db_functions import add_content


sql_query =  """ 
            CREATE TABLE IF NOT EXISTS Data
            (
                content_name TEXT,
                content_qn TEXT
            );
            """

def execute_query(sql_query):
    with sqlite3.connect("Data.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result

if __name__ == '__main__':
    execute_query(sql_query)
