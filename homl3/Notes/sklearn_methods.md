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
from sklearn.impute import SimpleImputer

Uses the specified system to calculate the value that will be used to fill in missing values

## KNNImputer
Uses KNN

## IterativeImputer
Uses linear regression

# Encoders

.categories_

## OrdinalEncoder
from sklearn.preprocessing import OrdinalEncoder

Assigns each attribute an index. This can be problematic if the machine learning algorithms considers bigger distances between numbers

## OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

Assigns the current attribute the value 1 and everything else 0 in a np.array

# Scalers

## MinMaxScaler (Aka normalization)
from sklearn.preprocessing import MinMaxScaler

Scales down the data by substracting the min and dividing by the difference between the min and the max

## StandardScaler (Aka standardization)
from sklearn.preprocessing import StandardScaler

Scales down the data by substracting the mean then dividing by the standard deviation

# RBF

## rbf_kernel
from sklearn.metrics.pairwise import rbf_kernel

Calculates the distance between the current input and a fixed point using gaussian rbf in order to measure similarity

# Utility methods

## Shuffle
from sklearn.utils import shuffle

dataframe = shuffle(dataframe)