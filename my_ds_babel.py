import pandas as pd
import sqlite3

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    csv_content = df.to_csv(index=False)
    conn.close()
    return csv_content

from io import StringIO

def csv_to_sql(csv_content, database, table_name):
    conn = sqlite3.connect(database)
    df = pd.read_csv(StringIO(csv_content))
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


csv_data = sql_to_csv('all_fault_line.db', 'fault_lines')
print(csv_data)  


csv_content = open("fault_lines.csv").read()
csv_to_sql(csv_content, 'list_volcanos.db', 'volcanos')
