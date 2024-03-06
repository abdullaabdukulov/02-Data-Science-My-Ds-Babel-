# Description

Part I SQLtoCSV. We will start with the SQL format to CSV

Your function will receives a connection (an sqlite3 object from import sqlite3 which will be already connected), table_name. Your function will transform the content of table_name to CSV format and return it. (Columns separated by comma and rows separated by \n)

Part II CSVtoSQL Your function will transform the content to SQL format by creating the table_name and adding each row.

Part III a) You will use your function to convert the list of all volcanos from CSV to SQL.

b) You will use your function to convert the list of all fault lines from SQL to CSV. Data are inside the table named: fault_lines.

# Task

1# sql_to_csv will receive two strings as parameters and return a string. the database is a filename where sql_to_csv will fetch the information. table_name is the table from the database file to fetch the information. your return value will be a CSV formatted string: "ColA,ColB,ColC\n1,2,3\n4,5,6\n"

2# csv_to_sql will receive three strings as parameters and return nothing. csv_content is a StringIO following the CSV format. the database is a filename where csv_to_sql will push the information. table_name is the table from the database file to insert the data.

DoYourJob libraries are not authorized. We won't list all of them. If you are not doing the sql request by yourself then you are using a "doyourjob library". An example is: sqlalchemy

# Installation
pip install numpy
pip install pandas
pip install python-dateutil
pip install pytz
pip install six
pip install tzdata

# Usages
Open CMD or Terminal
python my_ds_babel.py