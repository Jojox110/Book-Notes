# Dataframe methods

## df.info()
This method prints each column with their non-null amount of data and their datatype

## df.describe()
This methods prints out statistical data for each column (count, mean, max, min, std, 25%, 50%, 75%)

## df[column].value_counts()
This method prints out how many of each value is present in the dataframe

## df.head()
This method prints out the first five rows of each column

## df.hist() and plt.show()
Note: this uses import matploblib.pyplot as plt, pandas uses matploblib.pyplot

df.hist(bins=#, figsize(width, height))\
The bins attribute tells pandas to make a graph with # amount of consistent x intervals

## df.iloc
iloc can take in a variety of parameters that allow it to select rows in the dataframe

## df.reset_index()
This method adds an index row into the dataframe