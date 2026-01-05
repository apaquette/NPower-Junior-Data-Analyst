- Comparison operators
	- == equals operation
	- > greater than operation
	- >= greater than or equal
	- < less than operation
	- <= less than or equal
	- != not equal operator
- Branching
	- if statements
		- only executes if statements is true
	- elif
		- check additional condition if preceeding condition is false
	- else
		- alternate code when if statement is false
- Logic operators
	- not (inverts boolean)
	- or (true if any boolean is true)
	- and (true if all booleans are true)
# Loops
## Range function
- range(N)
	- range(3) -> [0, 1, 2]
	- range(10,15) -> [10,11,12,13,14]
## For loops
`for i in range(0,5):`
- iterates from 0 to 4
`for square in squares:`
- iterates through each item in squares variables
`for i, square in enumerate(squares):`
- i is index, square is the element

## While loops
- continue while a condition is true
`while(condition):`
# Functions
- takes an input and produces an output
- def keyword defines a function
- functions allow you to reuse code
## Built-in functions
- `len()` returns the length of a sequence
- `sum()` returns the total of all elements
- `sorted()` returns a sorted list
- `.sort()` method to sort an existing list
## Making a function
`def add1(a):
	b=a+1
	return b`
# Exception Handling
`try:
	...
except:
	...
else:
	executes if no exceptions occur
finally:
	execute no matter what`

# Objects and Classes
- every object has
	- type
	- internal data representation
	- set of procedures
- methods
	- a class or type's methods are function that belong to that class
	- how you interact with the data in an object
- classes
	- objects are instances of classes
	- class define attributes and methods of its instances