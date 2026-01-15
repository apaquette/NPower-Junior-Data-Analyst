# Pre-processing Data in Python
- process of converting or mapping data from "raw" form into another format
- also known as data cleaning
# Dealing with Missing Values in Python
- missing values occur when no data value is stored for a variable
- could be represented as "?", "N/A", 0, or a blank cell
## How to deal with missing data
- check with the collection source
- drop the missing values (variable or data entry)
- replace the missing value (better, but less accurate)
	- replace value with average
	- replace by frequency
	- replace based on other functions
- leave it as missing
## How to drop missing values in Python
- use `df.dropna()`
- axis=0 for row
- axis=1 for columns
## How to replace missing values in Python
- use `df.replace(missing_value, new_value)`
# Data Formatting in Python
- data is usually collected from different places and stored in different formats
- bringing data into a common standard allows for meaningful comparison
- sometimes the wrong data type is assigned
- many data types in Pandas
	- Objets
	- Int64
	- Float64
- identify data types: `df.dtypes()`
- convert data types: `df.astype()`
# Data Normalization in Python
- not-normalized
	- categories are in different range
	- difficult to compare
	- higher range variables will have a bigger influence on the results
- normalized
	- similar value range
	- similar intrinsic influence on the model
- normalization approaches
	- simple feature scaling
		- xnew = xold/xmax
		- `df['feature']/df['feature].max()`
	- min-max
		- xnew = (xold-xmin)/(xmax-xmin)
		- `df['feature']-df['feature'].min() / df['feature'].max()-df['feature'].min()`
	- Z-score (standard score)
		- xnew = xold-mean/std
		- range between -3 to 3
		- `df['feature']-df['feature'].mean()/df['feature'].std()`
# Binning in Python
- grouping values into bins
- converts numeric into categorical variables
- can improve model accuracy
-  Visualizing binned data: Histograms
# Turning Categorical Variables into Quantitative Variables in Python
- most statistical models can't take in objects/strings as inputs
- Add dummy variables for each unique category
- assign 0 or 1 in each category (boolean)
- use `pd.get_dummies()` to convert categorical to dummy variables

| Car | Fuel   | gas | diesel |
| --- | ------ | --- | ------ |
| A   | gas    | 1   | 0      |
| B   | diesel | 0   | 1      |
| C   | gas    | 1   | 0      |
| D   | gas    | 1   | 0      |
