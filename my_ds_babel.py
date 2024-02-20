import sqlite3
import pandas as pd


def sql_to_csv(database, table_name):
    con = sqlite3.connect(database)
    df = pd.read_sql(sql=f"SELECT * FROM {table_name}", con=con)
    df.to_csv(f'{table_name}.csv', index=False)
    con.close()


def csv_to_sql(csv_content, database, table_name):
    con = sqlite3.connect(database)
    df = pd.read_csv(csv_content)
    df.to_sql(f'{table_name}', con=con, if_exists='replace', index=False)
    con.close()


csv_to_sql('fault_lines.csv', 'list_volcanos.db', 'volcanos')
