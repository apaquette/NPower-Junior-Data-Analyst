# Introduction to databases
- SQL: Structured Query Language
	- used to query data in relational databases
- Data: facts, pictures
- Database: a repository of data
	- provides functionality for adding, modifying, and querying data
- Relational Database
	- organized in tabular form
	- columns contain item properties
	- table is a collection of related things
	- Relationships exist between tables
- DBMS: Database Management System
- RDBMS: Relational Database Management System
	- set of software tools that controls the data
	- Examples: MySQL, Oracle Database, IBM Db2

# SELECT Statement
- Data Manipulation Language (DML): statement used to read and modify data
- Select statement: query
- Result from the query: Result set/table
- `Select * from <tablename>`
- Can retrieve just the columns you want
- `SELECT <col1>,<col2>,<...> FROM <tablename>`
- WHERE clause
	- restricts the result set
	- always required a predicate: true/false/unknown
	- `select * from <tablename> WHERE <predicate>`
# COUNT, DISTINCT, LIMIT
- builtin functions
- COUNT
	- retrieves the number of rows
	- `SELECT COUNT(*) FROM <tablename>`
- DISTINCT
	- removes duplicate values from the result set
	- `SELECT DISTINCT <colname> FROM <tablename>`
- LIMIT
	- restricts the number of rows retrieved
	- `SELECT * FROM <tablename> LIMIT <amount>`
# INSERT Statement
- inserts data into a table
- DML statement
- `INSERT INTO <tablename> (<columnName>) VALUES (<value>)`
- multiple rows can be inserted at once
# UPDATE and DELETE Statements
- data in a table can be altered
- DML statement
- `UPDATE <tablename> SET <columnname>=<value> WHERE <condition>`
- DELETE statement is used for removing
- `DELETE FROM <tablename> WHERE <condition>`
# Summary
- Data Manipulation Language (DML) statements read and modify data
- The search condition of the WHERE clause uses a predicate to refine the search
- COUNT, DISTINCT, and LIMIT are expressions used with SELECT statements
- The INSERT, UPDATE, and DELETE are DML statements for populating and changing tables