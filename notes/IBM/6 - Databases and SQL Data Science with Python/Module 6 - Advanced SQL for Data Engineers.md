# Views, Stored Procedures, and Transactions
## Views
- alternative way of representing data that exists in tables
- can include specified columns from multiple base tables
- once created, can be queried like a table
- data in the view can be modified and propagates to table
- views can
	- show a selection of data
	- combine two or more tables
	- simplify access to data
- `CREATE VIEW <viewname> (<columnalias>, ...) AS SELECT <column1>, ... FROM <tablename> WHERE <predicate>`
- `DROP VIEW` can be used to remove a view
## Stored Procedures
- a set of sql statements stored and executed on the database
	- write in many different languages
	- accept information as parameters
	- return results to the client
- benefits
	- reduction in network traffic
	- improvement in performance
	- reuse of code
	- increase in security
`CREATE PROCEDURE <procedureName> (<parameter1> data_type ...) AS`
`BEGIN`
`-- statements to be executed`
`END`
- can be called from
	- external applications
	- dynamic SQL statements
## ACID Transactions
- transaction is an indivisible unit of work
- consists of one or more SQL statements
- Either all happens or none
- ACID
	- Atomic: All changes must be performed successfully or not at all
	- Consistent: Data must be in a consistent state before and after
	- Isolated: No other process can change the data while the transaction is running
	- Durable: The changes made must persist
- `BEGIN` starts ACID transaction
- `COMIMT` all statements complete successfully and save the new database state
- `ROLLBACK` one or more statements fail, undo changes
- Can be called from other languages: Java, C, R, and Python
- Use `EXEC SQL` to execute SQL statements from code
## Summary
- Views are a dynamic mechanism for presenting data from one or more tables
- A transaction represents a complete unit of work, which can be one or more SQL statements
- An ACID transaction is one where all the SQL statements must complete successfully, or none at all
- A stored procedure is a set of SQL statements stored and executed on the database server, allowing to send one statement as an alternative to sending multiple
- You can write stored procedures in many different languages like SQL PL, PL/SQL, Java, and C
# Join Statements
## Overview
- join operator combines rows for two or more tables
- joins match primary key to foreign keys to join related records between tables
## Inner Join
- inner joins display matches only
- usually primary key that exists as a foreign key in another table
- `SELECT <columns> FROM <table1> INNER JOIN <table2> ON <table1>.key = <table2>.foreignkey` 
## Outer Join
- return rows from each table include those that don't have matches between table
- left outer join
	- all rows from first table, and only matching rows from second
- right outer join
	- all rows from the second table, and only matching rows from first
- full outer join
	- all rows from both tables are included
- `SELECT <columnname>, ... FROM <table1> LEFT/RIGHT/FULL JOIN <table2> ON <table1>.id = <table2>.id
## Summary
- A join combines rows from two or more tables based on a the relationship between foreign key and primary keys between the tables
- To combine data from three or more tables, add new joins to the SQL statement
- There are two types of joins: inner and outer; and three types of outer joins: left, right, and full
- The most common type of join is the inner join, which matches the results from two tables and only returns elements where corresponding elements in both tables are the same
- You can use an alias as shorthand for a table or column name