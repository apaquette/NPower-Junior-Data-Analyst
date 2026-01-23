# Model Evaluation and Refinement
- In-sample evaluation tells us how well our model will fit the data used to train it
- It doesn't tell us how well the model can be used to predict new data
- Solution: training data, or out-of-sample evaluation set
- split dataset into
	- training set (70%)
	- testing set (30%)
- testing set is used to evaluate the model
### Function training_test_split()
- split data into random train and test subsets
`from sklean.model_selection import train_test_split`
`x_train, x_test, y_train, y_test = train_test_split(x_data, test_size=0.3, random_state=0)`
- **x_data**: features
- **y_data**: dataset target
- **x_train, y_train**: parts of data as training set
- **test_size**: percentage of data for testing (30% here)
- **random_state**: number generator used for random sampling
## Generalization performance
- a measure of how well our data does at predicting unseen data
- error obtained using testing data is an approximation of this
## Cross validation
- common out-of-sample evaluation metrics
- more effective use of data, each observation is used for both training and testing
### Function cross_val_score()
`from sklearn.model_selection import cross_val_score`
`scores = cross_val_score(lr,x_data,y_data, cv=3)`
- lr: model used for cross validation (linear-regression here)
- x_data: predictor data
- y_data: target data
- cv: number of partitions (3 here)
`np.mean(scores)`
- calculate the average score
### Function cross_val_predict()
- returns the prediction that was obtained for each element
- Has similar interface as cross_val_score()
`from sklearn.model_selection impot cross_val_predict`
`yhat=cross_val_predict(lr2e,xdata,ydata, cv)`
- same input parameters as cross_val_score()
- output is a prediction instead of score
# Overfitting, Underfitting and Model Selection
- underfitting: the model is too simple to fit the data
- overfitting: the model is too flexible and fits the noise rather than the function
![[Pasted image 20260123161005.png]]
- select the order that minimizes the test error
# Ridge Regression
- used to prevent overfitting
`from sklearn.linear_model import Ridge`
`RidgeModel=Ridge(alpha=0.1)`
`RidgeModel.fit(X,y)`
`Yha=RidgeModel.predict(X)`
- increment alpha value and calculate R-squared
- select alpha value that maximizes the R-squared
# Grid Search
- allows to scan multiple free parameters
- hyperparameters
	- alpha in Ridge recession is a hyperparameter
	- Scikit-learn has a means of automatically iteration over hyperparameters
- different hyperparameters are used to train multiple models
- model that performs the best is selected