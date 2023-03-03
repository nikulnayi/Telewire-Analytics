import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
# Define custom transformers
class NullEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X[X == '#Â¡VALOR!'] = np.nan
        return X
    
class TimeConversation(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
#         X['Time'] = pd.to_datetime(X['Time'], format='%H:%M').dt.time
#         print(X.info())
        return X
    
class ObjectToFloat(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X['maxUE_UL+DL'] = X['maxUE_UL+DL'].astype(float)
        return X
    
class OneHotEncoding(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        
        # Initialize the OneHotEncoder object
        one_hot_encoder = OneHotEncoder()

        # Fit and transform the categorical variable using OneHotEncoder
        one_hot_encoded = one_hot_encoder.fit_transform(X[['CellName']])

        # Convert the sparse matrix to a dense array and create a new dataframe
        one_hot_encoded_df = pd.DataFrame(one_hot_encoded.toarray(), columns=one_hot_encoder.get_feature_names_out(['CellName']))

        # Concatenate the one hot encoded dataframe with the original dataframe
        X = pd.concat([X, one_hot_encoded_df], axis=1)

        return X.drop(["CellName"], axis=1)

class Scaling(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Initialize the StandardScaler object
        scaler = StandardScaler()

        # Select only the float columns to scale
        float_cols = X.select_dtypes(include=['float']).columns.tolist()

        # Scale the float columns using StandardScaler and replace the original data with the scaled data
        X[float_cols] = scaler.fit_transform(X[float_cols])
        return X
    