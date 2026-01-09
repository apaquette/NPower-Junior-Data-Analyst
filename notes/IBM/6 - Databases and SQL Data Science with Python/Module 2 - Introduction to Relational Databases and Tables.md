# Relational Database Concepts
- Relational Model
	- most used data model
	- allows for data independence
	- data is stored in tables
	- ER: entity-relationship
	- ERD: entity-relationship diagram
- ER Model
	- used as a tool to design relational databases
- Mapping Entity diagrams to tables
	- entities becomes tables
	- attributes translate to columns
- Primary Keys and Foreign Keys
	- Primary Keys uniquely identify each row/entity
	- Foreign keys are primary keys defined in other tables, creating a link
# Types of SQL statements (DDL vs DML)
- DDL: Data Definition Language
	- Define, change, or drop data
	- Common statements: CREATE, ALTER, TRUNCATE, DROP
- DML: Data Manipulation Language
	- used to ready and modify data
	- CRUD operations (Create, Read, Update, Delete)
	- Common statements: INSERT, SELECT, UPDATE, DELETE
# CREATE TABLE Statement
- Syntax: `CREATE TABLE <tablename> (<columnName> <datatype> <optional parameters>, ...)`
# ALTER, DROP, and TRUNCATE Tables
- ALTER
	- add or remove columns
	- modify data types of columns
	- add or remove keys
	- add or remove constraints
	- syntax: 
		- `ALTER TABLE <tablename> ADD COLUMN <columnname> <datatype> ...`
		- `ALTER TABLE <tablename> MOIDFY <columnname> <datatype>`
		- `ALTER TABLE <tablename> DROP COLUMN <columnname>`
- DROP TABLE
	- used to delete tables
	- drops data in the table as well
	- syntax: `DROP TABLE <tablename>`
- TRUNCATE
	- removes the data in the table without deleting it
	- syntax: `TRUNCATE TABLE <tablename> IMMEDIATE`
	- this is quicker than using the DELETE statement
# Understanding Relational Model Constraints
Maintaining data integrity is essential to ensure accuracy, consistency, and reliability. Three key relational model constraints are:
- Entity Integrity
- Referential Integrity
- Domain Integrity
These constraints enforce rules on how data is stored and related within tables.
## Entity Integrity
This constraint ensures every table has a **primary key**. A primary key uniquely identifies each row in a table. A primary key column:
- must not contain NULL values
- must be **unique across all rows**
This constraint guarantees each record in a table is **distinct and identifiable**. 
## Referential integrity constraint
This constraint ensures a **foreign key** in one table always refers to a valid **primary key** in another. This maintains **consistent and meaningful relationships** between tables.

It enforces the logical link between related data in different tables, preventing the existence of invalid references.
## Domain integrity constraint
This constraint ensures all values stores in a column fall in a defined domain. This includes rules about:
- Data type
- Format
- Allowed values
- Nullability
It helps ensure the data in a column is **valid, logical, and consistent** with its intended use.
# SQL Scripts - Uses and Applications
## SQL Scripts
- a series of commands or a program that will be executed on an SQL server
- useful for making complex database changes
- can be used to create, modify, or delete objects
## Applications of SQL Scripts
- Create tables
- Drop tables
- Insert data
- Update data
- Delete data
- Create views
- Create stored procedures
- Create triggers
# Summary
- a database is a repository of data that provides functionality for adding ,modifying, and querying data
- SQL is a language used to query or retrieve data from a relational database
- The Relational Model is the most used data model due to its data independence
- The primary key uniquely identifies each row, preventing data duplication and providing a way of defining relationships between tables
- SQL statements fall into two categories: Data Definition Language (DDL) statements and Data Manipulation Language (DML) statements