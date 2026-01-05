# Lists and Tuples
## Tuples
- ordered sequence written as comma-separated elements in parentheses
- tuples are immutable
`Ratings = (10,9,6,5,10)`
- elements can be accessed by index
- tuples can be added to each other
`tuple2 = tuple1 + ("hard rock", 10)`
### Slicing
`tuple2[0:3] will grab indices 0 to 2`
## Lists
- ordered sequence represented by square brackets
`L = ['Michael Jackson', 10.1, 1982]`
- lists are mutable
- can contain strings, floats, integers, other lists, and tuples
# Dictionaries
- set of key-value pairs
- key acts like an index
- key is used to lookup the value
# Sets
- type of collection
- are unordered
- only have unique elements
## Set operations
- myset.add(element) (duplicates won't be added)
- myset.remove(element)
- "Value" in myset (checks if element is in set)
- combine common elements into their own set
	- setC = setA & setB
- union of a set combines all elements into a new set
	- setA.union(setB)