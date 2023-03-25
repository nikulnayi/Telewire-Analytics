import pandas as pd
import preprocessing
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from pathlib import Path
from sklearn.pipeline import Pipeline
import dill
project_dir = Path(__file__).resolve().parents[1]
# Define a function to preprocess the data
def preprocess(df):
    # Load the preprocessing pipeline from a pickle file
    with open(project_dir.joinpath('notebooks/pipelines/PreprocessingPipeline2.0.pkl'), 'rb') as f:
        pipeline, categories = dill.load(f)
    # Apply the preprocessing pipeline to the dataframe
    try:
        df = pipeline.transform(df)
        # preprocessed_df = pd.DataFrame(pipeline.transform(df))
    except ValueError:
        print(ValueError)
    # Return the preprocessed dataframe
    return df