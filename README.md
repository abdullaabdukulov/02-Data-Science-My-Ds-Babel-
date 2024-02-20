# Welcome to My_DS_Babel Project


## Task
The task of this project is to convert data between SQLite and CSV formats using Python.


## Description
This project provides functions for converting data between SQLite and CSV formats. It includes two main functions:

    sql_to_csv: Converts data from a SQLite database table to a CSV file.
    csv_to_sql: Converts data from a CSV file to a SQLite database table.


## Installation
Requirements

    Python 3.x
    pandas
    sqlite3

You can install the required dependencies using the following command:

```pip install pandas```


## Usage
Converting from SQLite to CSV

    Import the sql_to_csv function:

from sample_module import sql_to_csv

    Use the function with your database and table names:

csv_content = sql_to_csv('sample_database.db', 'sample_table')
print(csv_content)

Converting from CSV to SQLite

    Import the csv_to_sql function:

from sample_module import csv_to_sql

    Use the function with your CSV file, database, and table names:

csv_content = open("sample_csv_file.csv")
csv_to_sql(csv_content, 'sample_database.db', 'sample_table')

