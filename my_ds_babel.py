import sqlite3 as sql
import csv
import pandas as pd



def sql_to_csv(database, table_name):
    """Converting from slqite databese top csv file"""
    con = sql.connect(database)
    cur = con.cursor()
    df = pd.read_sql(f"SELECT * FROM {table_name}", con)
    return df[1:].to_csv(index=False)


def csv_to_sql(csv_context, database, table_name):
    """Converting from csv file to sqlite database"""
    con = sql.connect(database)
    df = pd.read_csv(csv_context)
    return df.to_sql(name=table_name, con=con, index=False)

print(sql_to_csv('all_fault_line.db','fault_lines'))




































# class MyDsBabel:
#         def sql_to_csv(self, database, table_name):
#             con = sql.connect(database)
#             cur = con.cursor()
#             cur.execute(f"SELECT * FROM {table_name}")
#             rows = cur.fetchall()
#
#             result = ""
#
#             for i in cur.description:
#                 result += f'{i[0]},'
#             result += '\n'
#
#             for row in rows:
#                 for i in row:
#                     result += f"{i},"
#                 result += '\n'
#
#             return result
#
#         def csv_to_sql(csv_content, database, table_name):
#             con = sql.connect(database)
#             cur = con.cursor()
#
#             print(csv_content.readlines())
#
#
# abj = MyDsBabel()
# # print(abj.sql_to_csv('all_fault_line.db','fault_lines'))
#
# csv_content = open("list_volcano.csv")
# abj.csv_to_sql(csv_content=csv_content, database='volcanos.db', table_name='volcanosy')
