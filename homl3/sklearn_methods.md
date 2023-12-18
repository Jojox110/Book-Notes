# Test-train split methods

## train_test_split
from sklearn.model_selection import train_test_split

Creates datasets for train and test using random

## StratifiedShuffleSplit
from sklearn.model_selection import StratifiedShuffleSplit

Creates splits of data for train and test using while keeping the stratum mostly evenly distributed

## .split()
Method built in for shuffle split methods

Generated indices to split data into training and test sets

# Imputer methods (Estimators)

## SimpleImputer
Uses the specified system to calculate the value that will be used to fill in missing values

## KNNImputer
Uses KNN

## IterativeImputer
Uses linear regression
