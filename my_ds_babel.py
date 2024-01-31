import sqlite3 as sql
import csv
import pandas as pd


def sql_to_csv(database, table_name):
    con = sql.connect(database)
    df = pd.read_sql(f"SELECT * FROM {table_name}", con)
    csv_filename = f"{table_name}.csv"
    df.to_csv(csv_filename, index=False)
    return csv_filename


def csv_to_sql(csv_filename, database, table_name):
    con = sql.connect(database)
    cur = con.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
    df = pd.read_csv(csv_filename)
    df.to_sql(name=table_name, con=con, index=False)


# Part III a) Converting the list of all volcanos from CSV to SQL
csv_content_volcanos = open("list_volcano.csv")
csv_filename = csv_to_sql(csv_content_volcanos, 'all_fault_line.db', 'volcanos')

# Part III b) Converting the list of all fault lines from SQL to CSV
csv_result = sql_to_csv('all_fault_line.db', 'fault_lines')
print(csv_result)
