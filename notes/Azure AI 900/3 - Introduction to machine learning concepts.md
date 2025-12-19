# Introduction
- Machine learning is the intersection of two disciplines: data science and software engineering
- Its goal is to use data to create predictive models
- This goal requires collaboration between data scientists and software developers

# Machine learning models
- a software application that encapsulates a function to calculate an output value based on input values
- the process of defining that function is known as training
- predicting new values is known as inferencing
![[Pasted image 20251216152057.png]]
1. training data consists of past observation
2. an algorithm is applied to the data to determine a relationship between the label and generalize that relationship as a calculation
3. The result of the algorithm is a model that encapsulates the calculation derived by the algorithm as a function
4. The trained model can be used for inferencing

# Types of machine learning model

![[Pasted image 20251216152324.png]]

## Supervised machine learning
- general term for machine learning algorithms where the t raining data includes both feature values and known label values
- used to train models by determining a relationship between features and labels in past observations
### Regression
- form of supervised ML where the label predicted by the model is a numeric value
### Classification
- form of supervised ML where the label represents a categorization
#### Binary
- the label determines whether the observed item is or isn't an instance of a specific class
- the model predicts one of two mutually exclusive outcomes
#### Multiclass
- extends binary classification to predict a label that represents one of multiple possible classes
- involves a known set of classes
- used to predict mutually exclusive labels

## Unsupervised machine learning
- involves training models using data that consists only of features
- there are no known labels
- determines relationships between the features of the observations in the training data

### Clustering
- most common form of unsupervised learning
- identifies similarities between observations based on their features
- similar to mulitclass classification, but you don't know the classes
- the classes are purely determined by the similarity of features

# Regression
- trained to predict numeric label values based on training data
- training data includes both features and known labels
- process for training involves multiple iterations where you use an appropriate algorithm
- the algorithm trains, evaluates, and refines the model
![[Pasted image 20251216152945.png]]
1. Split the training data (randomly) to create a dataset for training and a dataset for validation
2. Use an algorithm to fit the training data to a model (linear regression for example)
3. Use the validation data to test the model
4. Compare the known actual labels in the validation dataset to the labels the model predicted
- after each iteration, you can repeat the process with different algorithms and parameters until an acceptable evaluation metric is achieved

## Regression evaluation metrics
- you can calculate some common metrics used to evaluate regression models

### Mean Absolute Error (MAE)
- how many predictions are wrong

### Mean Squared Error (MSE)
- takes all discrepancies between predicted and actual labels
- this metric amplifies larger errors by squaring individual errors and calculating the mean

### Root Mean Squared Error (RMSE)
- helps take the magnitude of errors into account
- resulting metric no longer represents the quantity measured by the label

### Coefficient of determination (R^2)

## Iterative Training
- 

# Binary classification
- a supervised machine learning technique
- calculate probability values for class assignment
- used to train models to predict one of two possible labels (true or false)

### Binary classification evaluation metrics
- matrix of the number of correct and incorrect predictions for each possible class label
![[Pasted image 20251216153635.png]]
- known as a confusion matrix
	- True negatives (TN)
	- False positives (FP)
	- False negatives (FN)
	- True positives (TP)
- true predictions are show in a diagonal line from top-left to bottom-right
- colour-intensity is used to indicate the number of predictions in each cell

### Accuracy
- the proportion of predictions the model got right
- (TN + TP) / (TN + FN + FP + TP)

### Recall
- a metric that measures the proportion of positive cases that the model identified correctly
- TP / (TP+ FN)

### Precision
- similar to recall, but measures the proportion of predicted positive cases where the true label is actually positive
- TP / (TP + FP)

### F1-score
- overall metric that combines recall and precision
- (2 x Precision x Recall) / (Precision + Recall)

### Area Under the Curve (AUC)
- FP / (FP+TN)

# Multiclass classification
- a  type of supervised learning
- used to predict which of multiple possible classes an observations belongs
- follows the iterative train, validate, and evaluate process 

## Training a multiclass classification model
- need to use an algorithm to fit the training data to a function
- this function calculates a probability value for each possible class
### One-vs-Rest (OvR) algorithms
- train a binary classification function for each class
- each calculates the probability that the observation is an example of the target class
- Each function calculates the probability of the observation being a specific class compared to any other class
### Multinominal algorithms
- output is a vector that contains the probability distribution for all possible classes
## Evaluating a multiclass classification model
- by calculating binary classification metrics for each individual class
- can alternatively calculate aggregate metrics that take all classes into account

# Clustering
- a form of unsupervised machine learning where observations are grouped into clusters based on similarities
- it doesn't make use of previously known labels to train the model
- the label is the cluster to which the observation is assigned
## Training a clustering model
- multiple algorithms can be used for clustering
- most common is K-Means clustering
	1. Feature values are vectorized to define n-dimensional coordinates (n is the number of features)
	2. You decide how many clusters you want to use to group (called the k value)
	3. Each data point is assigned to its nearest centroid
	4. Each centroid is moved to the center of the data points assigned to it based on the mean distance between the points
	5. After the centroid is moved, the data points may be closer to a different centroid, so the data points are reassigned to clusters based on the new closest centroid
	6. centroid movement and cluster reallocation steps are repeated until the clusters become stable

## Evaluating a clustering model
- evaluation of a clustering model is based on how well the resulting clusters are separated from each other
- Metrics to use:
	- Average distance to cluster center
	- Average distance to other center
	- Maximum distance to cluster center
	- Silhouette

# Deep learning
- advanced form of machine learning that emulates how the brain learns
- key is the creation of artificial neural networks that simulate neurons using mathematical functions
- Artificial neural networks are made up of layers of neurons
- models produced are often referred as deep neural networks (DNN)
- can be used for many kinds of ML problems, including regression and classification
- involves fitting training data to a function that can predict a label based on the value of one or more features
- each layer encapsulates functions that operate on x and the weight (w) values associated
- algorithm involves iteratively feeding the feature values (x) in the training data through layers to calculate the output (y)
- it modifies the weights to reduce loss
- the final model includes the final weight values resulting in the most accurate predictions

## How does a neural network learn?
- weights in a neural network are central to how it calculates predicted values
- during raining, the model learns the weights that result in the most accurate precision
![[Pasted image 20251218114739.png]]
1. The training and validation datasets are defined
2. The neurons in each layer apply their weights and feed the data through the network
3. The output layer produce a vector containing the calculated value for (y)
4. A function loss is used to compare the predicted y values to the known y values and aggregate the difference (known as loss)
5. An optimization function can use differential calculus to evaluate the influence of each weight in the network and determine how they could be adjusted to reduce the amount of loss. The techniques can vary, but usually involves a gradient descent approach.
6. The changes to weights are backpropagated into to the layers in the network replacing previous values
7. The process is repeated over multiple iterations until the loss is minimized and the model predicts acceptably accurately