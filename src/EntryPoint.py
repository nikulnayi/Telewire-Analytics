import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from pathlib import Path
from sklearn.pipeline import Pipeline
import dill
from predict import predict
project_dir = Path(__file__).resolve().parents[1]
with open(project_dir.joinpath('notebooks/pipelines/PreprocessingPipeline2.0.pkl'), 'rb') as f:
    pipeline, categories = dill.load(f)
# Define the Streamlit app
def main():
    # Create a file uploader for CSV files
    data = pd.read_csv(project_dir.joinpath('data/raw/test.csv'),  encoding= 'unicode_escape')
    data = data.drop(["Unusual"], axis=1)
    prediction = predict(data)
    print(prediction)
# Run the app
if __name__ == '__main__':
    main()