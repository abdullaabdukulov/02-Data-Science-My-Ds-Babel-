import sqlite3
import pandas as pd 

def csv_to_sql(csv_context, database, table_name):
    connection = sqlite3.connect(database)
    dataframe = pd.read_csv(csv_context)
    dataframe.to_sql(name=table_name, con=connection, index=False)
    connection.close()

def sql_to_csv(database, table_name):
    connection = sqlite3.connect(database)
    select = f"SELECT * FROM {table_name};"
    request = pd.read_sql_query(select, connection)
    request.to_csv("list_fault_lines.csv", index=False)
    with open("list_fault_lines.csv", "r") as file:
        all_results = file.read()
    return all_results[:-1]
