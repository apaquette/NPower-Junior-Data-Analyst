# Refining your Results
## Using String Patterns and Ranges
- LIKE predicate can be used to search for pattern
	- example: `WHERE firstname LIKE 'R%'`
- using a range
	- `WHERE pages >= 290 AND <= 300`
	- becomes
	- `WHERE pages BETWEEN 290 AND 300`
- using a set of values
	- `WHERE country='AU' OR country='BR'`
	- becomes
	- `WHERE country IN('AU','BR')`
## Sorting Result Sets
- ORDER BY clause is used to order the set by a specified column
	- `ORDER BY columnname`
- use DESC to sort in descending order
	- `ORDER BY columnname DESC`
- can also indicate the column by number
	- `ORDER BY 2`
	- indicates to sort by the second column
## Grouping Result Sets
- GROUP BY groups results in subsets
- `GROUP BY <columnname>`
- HAVING clause is used with GROUP BY clause
- `GROUP BY <columnname> HAVING <condition>`
## Summary
- You can use the WHERE clause to refine query results
- The search condition of the WHERE clause uses a predicate to refine the search
- You can use the wildcard character (%) as a substitute for unknown characters in a pattern
- You can use BETWEEN ... AND ... to specify a range of numbers
- You can sort query results in ascending or descending order using ORDER BY
- You can group query results by using the GROUP BY clause
# Functions, Multiple Tables, and Sub-queries
## Built-in Database Functions
- most databases come with built-in SQL functions
- functions can significantly reduce amount of data needed to be retrieved
- can speed up data processing
- Aggregate functions
	- INPUT: Collection of values
	- Output: Single value
	- Examples: SUM, MIN, MAX, AVG
- Scalar and string functions
	- Perform operations on every input
	- ROUND, LENGTH, UCASE, LCASE
## Date and Time Built-in Functions
- most databases contain special datatypes for dates
	- DATE: `YYYYMMDD`
	- TIME: `HHMMSS`
	- TIMESTAMP: `YYYYXXDDHHMMSSZZZZZZ`
- Functions: YEAR, MONTH, DAY, DAYOFMONTH, DAYOFWEEK, DAYOFYEAR, WEEK, HOUR, MINUTE, SECOND
	- DAY: extract day portion of a date
- Date or time arithmetic
	- DATE_ADD
	- DATE_SUB: subtracts a specified time interval from a date
		- modifies a date
	- DATEDIFF: calculates the difference between two dates
		- provides numerical result in days between two dates
- Special Registers: CURRENT_DATE, CURRENT_TIME
## Sub-Queries and Nested Selects
- like regular queries, but placed in parentheses and nested inside another query
- `SELECT column1 FROM table WHERE column2 = (SELECT MAX(column2) FROM table)`
	- inside the WHERE clause of another query
## Working with Multiple Tables
- using subqueries, subquery filters result set of outer query
- subquery is used as input for outer query
- can also specify additional tables in the FROM clause
	- results in implicit join
## Summary
- When working with large datasets, you can save time by using built-in functions rather than retrieving the data into your application and executing functions on the data
- You can use sub-queries to form powerful queries than otherwise
- You can use a sub-select expression to evaluate built-in aggregate functions like average
- Derived tables or table expressions are sub-queries where the outer query uses the result of a sub-query as a data source