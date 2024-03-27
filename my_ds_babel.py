# Import neccesary libraries
import sqlite3
import pandas as pd

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)

    # Write your SQL query
    query = f"SELECT * FROM {table_name}"

    # Use pandas to read the SQL data into a DataFrame
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Save the DataFrame to a CSV file
    # Replace 'output_file.csv' with your desired output file name
    new_csv = df.to_csv(index=False)
    return new_csv

def csv_to_sql(csv_file_path, database_path, table_name):
    # Read CSV content into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)

    # Write the DataFrame to the SQLite database
    df.to_sql(table_name, conn, index=False, if_exists='replace')

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()



# # Example usage:
# csv_content_fault_lines = sql_to_csv('all_fault_line.db', 'fault_lines')
# print(csv_content_fault_lines)


csv_content_volcanos = open("list_volcano.csv").read()
csv_to_sql(csv_content_volcanos, 'list_volcanos.db', 'volcanos')

with open('list_volcano.csv', 'r') as csv_file:
    csv_to_sql(csv_file, 'list_volcanos.db', 'volcanos')