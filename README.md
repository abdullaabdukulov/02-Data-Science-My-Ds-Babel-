# Description

Data is the heart of an information system. Converting data from a format to another or migrating them to another database is a critical skill.

It would be great if every information system could speak the same language.

Tower of Babel Your mission will be to help translate from one format to another.
We will work with two popular formats: SQL and CSV.

# Task

Part I SQLtoCSV. We will start with the SQL format to CSV

Your function will receives a connection (an sqlite3 object from import sqlite3 which will be already connected), table_name. Your function will transform the content of table_name to CSV format and return it. (Columns separated by comma and rows separated by \n)

Part II CSVtoSQL Your function will transform the content to SQL format by creating the table_name and adding each row.

Part III a) You will use your function to convert the list of all volcanos from CSV to SQL.

b) You will use your function to convert the list of all fault lines from SQL to CSV. Data are inside the table named: fault_lines.

# Install
pip install pandas
pip install sqlite3

# Usage

jupyter-notebook --no-browser