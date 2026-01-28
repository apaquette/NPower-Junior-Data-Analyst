This module consists of the final project for course 7: Data Analysis with Python. Below I have summarized the overall process required to complete this project with relevant notes.

# Importing the Dataset
This task involves importing a data set from a file (typically csv, but could be excel or other structured format) into a dataframe. The syntax looks like the following: 

`df = pd.read_csv(file, header=None)`

The header clause is used to specify whether a header is included or not.

If no header is included, you should assign it using the columns attribute:

`df.columns = ['col1', 'col2'...]`

**It is very important that you use a single set of square brackets here.**

This is because two sets of square brackets will create a dataframe, which should not be the case for columns assignment.


# Data Wrangling

This task involves cleaning up the data for use later on in the pipeline. The first step is to replace certain values with another, ensuring consistency across the entire data frame.

`df.replace(value, target, inplace=True)`

A common usecase is replace `?` with `np.nan`, but other use case might be ensuring consistency in formatting between values (`New York City` vs 'NYC' vs 'NY' for example).

Another useful step in data wrangling is using the .info() method

`df.info()`

Which will provide a summary of all columns, values, and data types. This is helpful to identify any null values that need to be handled before moving forward as well as any data types that need to be changed.

- `.fillna(value)` can be used to replace all `nan` values with a targeted variable
- `.dropna` will remove all records which contain a `nan` value.
- `df['col1'...].astype('type')` will convert all values in the given columns to a targeted datatype.
- `np.round(df[['col1'...]], num)` will round values to the number of decimal points given by num.

# Exploratory Data Analysis (EDA)
This task involves using data visualization to understand the data better and identify possible correlations in the data that may help us better understand the relationship between the data as well as identify which variables are related to others for the purposes of training a model.

`sns.regplot()` is used to create a plot and find a line of best fit to see how well a linear model might fit the data. X and Y are used to test out different labels (Y) and how they relate to a value (X). This is restricted to visualizing LinearRegression models.

`sns.boxplot()` is used to visualize categorical features and likewise identify how they relate to a specific label.

`df.corr()` will show us a correlation matrix between all values in the dataset. Values will have a correlation of `1` to themselves. Values close to zero have weak or no relationship. Values close to 1 have strong positive relationships while values close to -1 have strong negative relationships. 

# Model Development
Now that we've imported our data, cleaned it, and explored it, we are ready to start developing our model. First we need to identify our target (Y) variable and our feature variable(s) (X). In single linear regression models, a single feature is used to identify our target variable

`X = df[['featurecol']]`
`Y = df[['targetcol']]`
`slg_model = LinearRegression().fit(X,Y)`
`slg_model.score(X,Y)`

The score is given as the **R^2** score which is the coefficient of determination of the model. It is a measure to determine how close the data is fitted to the regression line. A high score represents a more accurate model while a low score represents a less accurate model.

For a multi linear regression model, multiple features are used to identify the target variable (usually denoted by Z instead of X). There are two ways of assigning the Z value.

The first is by dropping our label value from the dataframe, which will assign all other columns to the Z variable

`Z = df.drop('label', axis=1)`

The second is by specifying which features to include in our dataframe:

`Z = df[['feature1', 'feature2', ...]]`

In either case, the goal is to store the columns you want to use to identify the Y value in Z.

The next step is to use our same LinearRegression model and use the Z variable containing multiple features to train the model.

`Z = df.drop('label', axis=1)`
`mlr_model = LinearRegression(Z, Y)`
`mlr_model.score(Z, Y)`

This process can be further improved by the use of a pipeline. A typical pipeline might include a StandardScaler, PolynomialFeatures, and LinearRegression. The goal of a pipeline is to streamline these processes into a single pipeline, and can include any number of components specific to your pipeline. Its construction is modular.

`StandarScaler`: Standardizes features by removing the mean and scaling to unit variance.
`PolynomialFeatures`: Generates a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the value specified.
`LinearRegression`: The algorithm used to train the model

Here's an example of how a model might be trained using a pipeline:

`Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]`

This line is the input used for the pipeline.

`pipe = Pipeline(Input)`
`pipe.fit(Z,Y)`

Just like with the model, the features and label are passed to a fit method, but each step of the pipeline we would normally have to handle manually is being performed by the pipeline to result in a trained model.

`pipe.score(Z,Y)`

Just like with our regression model, this will give us the R^2 value of the model.

# Model Refinement

To further refine our model, we want to split our data into training and testing subsets. The percentage of difference varies, but a common split is 70% for training, and 30% for testing, but any split will work.

`x_train, x_test, y_train, y_test = train_test_split(Z, Y, test_size=value, random_state=1)`
*setting the random state helps us ensure the output is consistent between runs.*

We can then use a Ridge regressor algorithm with a given hyperparameter alpha value to train the model.

`rm = Ridge(alpha=value)`
`rm.fit(x_train, y_train)`
`rm.score(x_test, y_test)`

The score is still using the R^2 value.