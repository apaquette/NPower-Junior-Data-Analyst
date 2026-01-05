# Reading Files with Open
- open(filepath, mode)
- with statement
	- automatically closes the file out of scope
Modes
- r - reading
- w - writing
- a - appending
## Writing files with open
- create a new text file with open() and write mode
- if the file is in the directory, it will be overwritten
- .write() will write text into the file
- append mode will add content at the end of the file

## File modes
| Mode | Description                                                                                                         |
| ---- | ------------------------------------------------------------------------------------------------------------------- |
| r    | Read                                                                                                                |
| w    | Write                                                                                                               |
| a    | Append                                                                                                              |
| x    | Exclusive creation (creates a new file but raises an error if it exists)                                            |
| rb   | Read binary mode                                                                                                    |
| wb   | Write binary mode                                                                                                   |
| ab   | Append binary mode                                                                                                  |
| xb   | Exclusive binary creation mode                                                                                      |
| rt   | Read text mode (Default for text files)                                                                             |
| wt   | Write text mode                                                                                                     |
| at   | Append text mode                                                                                                    |
| r+   | Read and write mode. Opens file for both reading and writing                                                        |
| w+   | Write and read mode. Creates a new file for reading and writing. Overwrites the file if it exists                   |
| a+   | Append and read mode. Opens for both appending and reading. Creates the file if it doesn't exist                    |
| x+   | Exclusive creation and read/write mode. Creates a new file for reading and writing but raises an error if it exists |
# Pandas
- popular open-source data manipulation and analysis library
- provides flexible tools for working with structured data
- designed to handle various formats
**Data Structures**: Pandas offers two primary data strictures
1. DataFrame: 2D, size-mutable tabular data stricture with rows and columns
2. Series: one-dimensional labelled array; a single column or row of data
**Import and export**: Easy to read data from various sources (CSV, Excel, SQL databases)
**Data Merging and joining**: Can combine multiple DataFrames using methods like merge and join
**Efficient Indexing**: Pandas provides efficient indexing and selection methods
**Custom Data Structures**: Can create custom data structures and manipulate data in ways that suit your specific needs

## Series Attributes and Methods
**values**: Returns the series data as a NumPy array
**index**: Returns the index of the Series
**shape**: returns a tuple representing the dimensions of the Series
**size**: returns the number of elements
**mean(), sum(), min(), max()**: Calculates summary statistics
**unique(), nunique()**: Get unique values or the number of unique values
**sort_values(), sort_index()**: Sort the series by values or index labels
**isnull(), notnull()**: Check for missing or non-missing values
**apply()**: Apply a custom function to each element

## What is a DataFrame?
- 2D labelled data structure with columns and different data types
- like a table where columns represent variables, and rows represent data points
- suitable for a wide range of data (CSV, spreadsheets, SQL databases)

DataFrame Attributes and Methods
**shape**: Returns the dimensions (number of rows and columns) of the DataFrame.
**info()**: Provides a summary of the DataFrame, including data types and non-null counts.
**describe()**: Generates summary statistics for numerical columns.
**head(), tail()**: Displays the first or last n rows of the DataFrame.
**mean(), sum(), min(), max()**: Calculate summary statistics for columns.
**sort_values()**: Sort the DataFrame by one or more columns.
**groupby()**: Group data based on specific columns for aggregation.
**fillna(), drop(), rename()**: Handle missing values, drop columns, or rename columns.
**apply()**: Apply a function to each element, row, or column of the DataFrame.

# Numpy in Python
- a library for scientific computing
- NumPy is the basis for Pandas
## NumPy Array
- similar to a list
- usually fixed in size
- each element is of the same type
- the data is accessible via an index
- NumPy makes it easier to do operations performed in data science
- typically computationally faster and require less memory than Python
- this is important when you have lots of data
## Matrix Mathematics
### 1D Arrays : Vectors
- 1D array is often termed as a fector
- vector can be classified as a row or column vector
![[Pasted image 20260105131509.png]]
- vectors can be added, subtracted, or multiplied if they have the same shape
![[Pasted image 20260105131558.png]]
![[Pasted image 20260105131607.png]]
- resulting array has the same size as the original two vectors
- we can add, subtract, or multiply a constant to any vectors
![[Pasted image 20260105131658.png]]
![[Pasted image 20260105131702.png]]
### 2D Arrays : Matrices
- typically rectangular arrays with data stores in rows
- all operations for 1D arrays are applicable to 2D arrays
- dot product
![[Pasted image 20260105131841.png]]
- reverse example
![[Pasted image 20260105131909.png]]
## Two Dimensional Numpy
- Numpy arrays can be created with more than one dimension
- 2D Numpy arrays can be visualized as a rectangular array with rows and columns
- ndim attribute provides the number of nested lists (or axes)
- elements can be accessed via index
	- first index is for the list
	- second index is for an element in that list

## Beginner's Guide to NumPy
- short for Numerical Python
- library for numerical and scientific computing
- provides support for large, multi-dimensional arrays and matrices
- has a collection of high-level mathematical functions
- serves as the foundation for many data science and machine learning libraries
### Key aspects
- Efficient data structures
- Multi-dimensional arrays
- Element-wise operations
- Random number generation
- Integration with other libraries
- Performance optimization
### Operation with NumPy
| Operation               | Description                                   | Example                                           |
| ----------------------- | --------------------------------------------- | ------------------------------------------------- |
| Array Creation          | Creating a NumPy array                        | `arr = np.array([1,2,3])`                         |
| Element-Wise Arithmetic | Element-wise addition, subtraction, and so on | `result = arr1 + arr2`                            |
| Scala Arithmetic        | Scalar addition, subtraction, and so on       | `result = arr * 2`                                |
| Element-Wise Functions  | Applying functions to each element            | `result = np.sqrt(arr)`                           |
| Sum and Mean            | Calculating the sum and mean of an array.     | `total = np.sum(arr)`<br>`average = np.mean(arr)` |
| Maximum and Minimum     | Finding the max and min values                | `max = np.max(arr)`<br>`min = np.min(arr)`        |
| Reshaping               | Changing the shape of the array               | `reshaped = arr.reshape(2,3`                      |
| Transposing             | Transposing a multi-dimensional array         | `transposed = arr.T`                              |
| Matrix Multiplication   | Perform matrix multiplication                 | `result = np.dot(matrix1, matrix 2`               |
# Summary
- Python uses the open() function to read and write files, providing access to the content. It also allows overwriting.
- Pandas is a powerful Python library for data manipulation and analysis. It provides data structures and functions to work with structured data.
- NumPy is a Python library for numerical and matrix operations, offering multidimensional array objects and mathematical functions to work with data efficiently
- A one-dimensional NumPy array is a linear sequence of elements, like a traditional list, but optimized for computations and array operations.
- A two-dimensional NumPy array is a grid-like structure suitable for representing data as a matrix or a table for numerical computations.
