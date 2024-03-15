# Import necessary libraries
import pandas as pd
import sqlite3 as sql

# Define functions to convert between SQL and CSV
def sql_to_csv(database, table_name):

    # Connect to the SQL database
    conn = sql.connect(database)

    # Fetch data from the specified table
    dataset=f"SELECT * FROM {table_name}"

    # Read SQL data into a pandas DataFrame
    data_frame = pd.read_sql(dataset, conn)

    # Display the DataFrame (optional)
    print(data_frame)

    # Convert DataFrame to CSV and save it
    data_frame = data_frame.to_csv('list_fault_lines.csv',index=False)

    # Indicate completion
    print('Proccess Completed :)')



def csv_to_sql(database, db, table_name):

    # Connect to the SQLite database
    conn = sql.connect(db)

    # Read CSV data into a pandas DataFrame
    df = pd.read_csv(database)

    # Convert DataFrame to SQL table and insert it into the database
    query = f"SELECT * FROM {table_name}"
    query = df.to_sql(query, conn,index=False)

    # Indicate completion
    print('Proccess Completed :)')



# Example usage:

#sql_to_csv('all_fault_line.db', 'fault_lines' )
#csv_to_sql('list_volcano.csv', 'list_volcano.db', 'Volcano Name')