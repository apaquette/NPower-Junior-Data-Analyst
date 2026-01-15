# Importing Data Sets
## Python Packages for Data Science
- Scientific Computing Libraries
	- Pandas: Data structures & tools
	- NumPy: Arrays and matrices
	- SciPy: Integrals, solving differential equations, optimization
- Visualization Libraries
	- Matplotlib: plots & graphs, most popular
	- Seaborn: plots, heat maps, time series, violin plots
- Algorithmic Libraries
	- Scikit-learn: ML Regression, classification, and so on
	- Statsmodels: Explore data, estimate statistical models, and perform tests
## Importing and Exporting Data in Python
### Importing Data
- process of loading and reading data into Python from various sources
- Two important properties
	- Format (csv, json, xlsx)
	- File Path of dataset (Local path, or internet URL)
- use `df.head(n)` to show the first n rows of the dataframe
- use `df.tail(n)` to show the last n rows of the dataframe
- add headers using `df.columns = headers`
	- headers is a list of header values
- read data into a dataframe using
	- `df.read_csv(path)` for csv
	- `df.read_json()` for json
	- `df.read_excel()` for excel
	- `df.read_sql()` for sql
### Export data
- preserve progress anytime by saving modified dataset using
	- `df.to_csv(path)` for csv
	- `df.to_json()` for json
	- `df.to_excel()` for excel
	- `df.to_sql()` for sql

## Getting Started Analyzing Data in Python
- understand your data before beginning any analysis
- should check data types and data distribution
- locate potential issues with the data
- Why check data types?
	- potential info and type mismatch
	- comparability with python methods
- In pandas, we use `df.dtypes` to check datatypes
- `df.describe()` returns a statistical summary
	- `include="all"` shows summary of all columns
- `df.info()` gives a concise summary of the DataFrame
- 
### Data Types
| Pandas Type           | Native Python                                               | Description                      |
| --------------------- | ----------------------------------------------------------- | -------------------------------- |
| object                | string                                                      | numbers and strings              |
| int64                 | int                                                         | Numeric characters               |
| float64               | float                                                       | Numeric characters with decimals |
| datetime64, timedelta | N/A (but see datetime module  in Python's standard library) | time data                        |
