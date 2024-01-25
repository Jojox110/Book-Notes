from pathlib import Path
import pandas as pd
import numpy as np
import tarfile
import urllib.request
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.utils import shuffle

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)  # Download the data
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets") # Extract from the tar.gz
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data() # Load into a pd dataframe

##################
# Clean The Data #
##################

# imputer = SimpleImputer(strategy="median")
# housing_num = housing.select_dtypes(include=[np.number])
# imputer.fit(housing_num)
# X = imputer.transform(housing_num)
# housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing_num.index) # DataFrame(data, columns, index). Index is the row count

# print(len(X[0]))
# print(housing.describe())
# print(housing_tr.describe())
# print(housing_num.describe())
# print(housing_num.index)

############################################
# Handling Text and Categorical Attributes #
############################################

# housing_cat = housing[["ocean_proximity"]]
# housing_cat = shuffle(housing_cat)

# print(housing_cat.head(8))

# ordinal_encoder = OrdinalEncoder()
# housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
# print(housing_cat_encoded[:8])
# print(ordinal_encoder.categories_)

# cat_encoder = OneHotEncoder()
# housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
# print(len(housing_cat_1hot.toarray()))

######################################
# Feature Scaling and Transformation #
######################################

