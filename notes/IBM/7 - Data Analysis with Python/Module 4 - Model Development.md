# Linear Regression and Multiple Linear Regression
- linear regression: one independent variable
- multiple linear regression: multiple independent variables
## Simple linear regression (SLR)
- The predictor variable - x
- The target variable - y
- y = b_0 + b_1 x
- b_0: the intercept
- b_1: the slope
## Multiple Linear Regression (MLR)
- used to explain the relationship between
- one continuous target Y
- two or more features X
# Model Evaluation using Visualization
- Regression plot
- Residual plot
- distribution plot
# Polynomial Regression and Pipelines
- special case of genera linear regression model
- useful for describing curvilinear relationships
- Curvilinear relationship: squaring or setting high-order terms of predictor variables
## Polynomial Regression
- quadratic
- cubic
- higher order
## Pipelines
- many steps to getting a prediction
Normalization -> Polynomial transform -> Linear Regression
- pipelines perform series of transformations
# Kernel Density Estimation (KDE) Plots for Model Evaluation
- valuable for visualizing data distributions and estimating their probability density function (PDF)
- particularly useful in regression analysis
- KDE plots serve as a modern and effective method for assessing model performance
## Why Use KDE Plots?
- provide a smooth approximation of data distribution
- help compare true vs predicted distributions
- not sensitive to bin sizes
- can highlight deviations between observed and predicted values
# Measures for In-Sample Evaluation
- a way to numerically determine how good the model fits on dataset
- two important measures: Mean Squared Error (MSE), R-Squared
## R-squared
- coefficient of determination
- measure to determine how close the data is fitted to the regression line
- the percentage of variation of the target variable explained by the linear model
- comparing regression model to a simple model
# Prediction and Decision Making
- Do the predicted values make sense?
- Visualization
	- regression plot
	- residual plot
	- distribution plot
- Numerical measures for evaluation
	- Mean-squared error
	- R-Squared
- Comparing models
