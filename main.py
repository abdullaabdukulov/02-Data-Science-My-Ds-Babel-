import pandas as pd
import sqlite3 as sql


def sql_to_csv(database, table_name):
    conn = sql.connect(database)
    dataset=f"SELECT * FROM {table_name}"
    data_frame = pd.read_sql(dataset, conn)
    print(data_frame)
    data_frame = data_frame.to_csv('list_fault_lines.csv',index=False)
    print('Proccess Completed :)')



def csv_to_sql(database, db, table_name):
    conn = sql.connect(db)
    df = pd.read_csv(database)
    query = f"SELECT * FROM {table_name}"
    query = df.to_sql(query, conn,index=False)
    print('Proccess Completed :)')




#sql_to_csv('all_fault_line.db', 'fault_lines' )
#csv_to_sql('list_volcano.csv', 'list_volcano.db', 'Volcano Name')