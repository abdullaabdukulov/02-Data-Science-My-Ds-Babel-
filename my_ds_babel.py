import sqlite3 as sql
import csv
import pandas as pd


def sql_to_csv(database, table_name):
    """Converting from slqite databese top csv file"""
    con = sql.connect(database)
    cur = con.cursor()
    df = pd.read_sql(f"SELECT * FROM {table_name}", con)
    return df.to_csv(index=False)


def csv_to_sql(csv_context, database, table_name):
    """Converting from csv file to sqlite database"""
    con = sql.connect(database)
    df = pd.read_csv(csv_context)
    return df.to_sql(name=table_name, con=con, index=False)


print(sql_to_csv('all_fault_line.db', 'fault_lines'))

# csv_content = open("list_volcano.csv")
# abj.csv_to_sql(csv_content=csv_content, database='volcanos.db', table_name='volcanosy')
