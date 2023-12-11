# Welcome to My Ds Babel
<br>

<h3>Description</h3>
<p>Data is the heart of an information system. Converting data from a <code>format</code> to another or <code>migrating</code> them to another <code>database</code> is a critical skill.</p>
<p>It would be great if every information system could speak the same language.</p>
<img src="https://storage.googleapis.com/qwasar-public/track-ds/babel_picture.png" width="400">
Tower of Babel Your mission will be to help translate from one format to another.
<p>We will work with two popular formats: <code>SQL</code> and <code>CSV</code>.</p>
<h2>What is SQL?</h2>
<p>It stands for <code>Structured Query Language</code>.
It helps you perform queries in a database. The query will have the format of:</p>
<ul>
<li>SELECT (GET)</li>
<li>INSERT</li>
<li>UPDATE</li>
<li>DELETE</li>
</ul>
<p>It has a specific syntax:</p>
<pre class=" language-plain"><code class=" language-plain">SELECT * FROM table;
INSERT INTO table_name(id, name) VALUES(1, 'Pacific Ocean');
UPDATE ...
DELETE ...
</code></pre>
<h2>How to connect to an <code>SQLite</code> database?</h2>
<p>Good question. Google might have an answer. :-)</p>
<h2>What is CSV?</h2>
<p>It stands for <code>Comma Separated Values</code>
There are files with multiple lines and columns. Divider are <code>,</code> (comma) and new-line (<code>\n</code>)</p>
<pre class=" language-plain"><code class=" language-plain">id,name
1,Pacific Ocean
2,Atlantic Ocean
3,Indian Ocean
4,Arctic Ocean
5,Southern Ocean
</code></pre>
<p>Interesting fact: the Southern Ocean was recognized by the International Hydrographic Organization in 2000. It borders Antarctica in its entirety. <a href="https://en.wikipedia.org/wiki/Southern_Ocean" target="_blank">wiki link</a></p>
<p>Example in ruby:</p>
<pre class=" language-plain"><code class=" language-plain">require "sqlite3"
require 'csv'

db = SQLite3::Database.new "volcanos.db"

# Create a database
rows = db.execute &lt;&lt;-SQL
  create table volcanos (
    volcano_name varchar(100),
    latitude int,
    .... OTHER FIELDS
  );
SQL

csv = File.read('list_volcano.csv')

CSV.parse(csv, headers: true) do |row|
    db.execute "insert into volcanos values ( ?, ?, ?, ?, ?, ? )", row.fields
end

p db.execute( "select * from volcanos" )
</code></pre>
<p><strong>Part I</strong> <code>SQL</code><em>to</em><code>CSV</code>.
We will start with the <code>SQL</code> format to <code>CSV</code></p>
<p>Your function will receives a <code>connection</code> (an <code>sqlite3</code> object from import sqlite3 which will be already connected), <code>table_name</code>.
Your function will transform the content of <code>table_name</code> to <code>CSV</code> format and return it. (Columns separated by <code>comma</code> and rows separated by <code>\n</code>)</p>
<p><strong>Part II</strong> <code>CSV</code><em>to</em><code>SQL</code>
Your function will transform the content to <code>SQL</code> format by creating the <code>table_name</code> and adding each row.</p>
<p><strong>Part III</strong>
a) You will use your function to convert the <a href="https://storage.googleapis.com/qwasar-public/track-ds/list_volcano.csv" target="_blank">list of all volcanos</a> from CSV to SQL.</p>
<p>b) You will use your function to convert the <a href="https://storage.googleapis.com/qwasar-public/track-ds/all_fault_line.db" target="_blank">list of all fault lines</a> from SQL to CSV.
Data are inside the table named: <code>fault_lines</code>.</p>
<h2>Technical specifications</h2>
<p>Write two functions:</p>
<pre class=" language-plain"><code class=" language-plain">def sql_to_csv(database, table_name):
def csv_to_sql(csv_content, database, table_name):
</code></pre>
<p>1# sql_to_csv will receive two strings as parameters and return a string.
the database is a filename where sql_to_csv will fetch the information.
table_name is the table from the database file to fetch the information.
your return value will be a CSV formatted string:
"ColA,ColB,ColC\n1,2,3\n4,5,6\n"</p>
<p>2# csv_to_sql will receive three strings as parameters and return nothing.
csv_content is a StringIO following the CSV format.
the database is a filename where csv_to_sql will push the information.
table_name is the table from the database file to insert the data.</p>
<p>DoYourJob libraries are not authorized. We won't list all of them. If you are not doing the sql request by yourself then you are using a "doyourjob library". An example is: sqlalchemy</p>
<p>Example:</p>
<pre class=" language-plain"><code class=" language-plain">print(sql_to_csv('sourse_all_fault_line.db','fault_lines'))

csv_content = open("sourse_list_volcano.csv")
csv_to_sql(csv_content, 'list_volcanos.db','volcanos')
</code></pre>
<p><em>Tip</em>
Google: Python sqlite3
Google: Python CSV
Google: Python Class
Google: SQL Format SELECT
Google: create sqlite table
Google: SQL Format INSERT</p>

<p></p>

## Instalation
#### You have to install all libraries that shown in **`requirements.txt`** , otherwise project might working `wrogly` or `not work`

## Usage

After cloning and installing required libraries you have to write peace of code below at the end of `my_ds_babel.py` file:

```
  # If you want to convert your SQLite database to csv file write code below
  result = sql_to_scv('database_name.db', 'table_name')
  print(result)
```
***

```
  # If you want to convert csv file to SQLite database write the code below
  csv_content = open("csv_file_name.csv")
  csv_to_sql(csv_context, 'database_name.db', 'table_name')
```

After put this command in your terminal
```bash
  python my_ds_babel.py
```