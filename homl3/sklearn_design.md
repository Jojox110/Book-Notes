# Page 71
<br>

# Consistency
Scikit-learn aims to make their objects share a consistent and simple interface

## Estimators
Estimators are objects that can estimate a value based off a dataset (Ex: SimpleImputer). The estimation itself is performed by the fit() method. 

## Transformers
Transformers are objects that can transform a dataset using an estimator on missing values. \
There are methods, such as fit_transform() that do everything in one go and are usually more optimized than doing them seperately

## Predictors
Predictors are types of estimators that are capable of making a prediction based off a dataset using some techniques such as Linear Regression. \
This will usually be performed by the predict() method

# Inspection
These objects have methods that allow us to inspect them, such as .strategy and .statistics_

# Nonproliferation of classes
Datasets are represented as np arrays or scipi sparse matrices. Hyperparameters are just regular Python string or numbers

# Composition
All of this is designed with re-usability in mind

# Sensible defaults
Scikit-learn provides reasonable default values for most parameters, making it easy to quickly create a baseline working system

# fit, predict and fit_predict
The fit() method is used to train a model on the dataset, and the predict() method is used to make a prediction on new data using a trained model

The fit_predict() method is used in unsupervised learning to train the model and predict data in a single step. This is often used for clustering tasks.