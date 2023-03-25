import joblib
import pandas as pd
from preprocessing import preprocess
import pandas as pd
from pathlib import Path
import dill

# Load the predictive model from a pickle file
project_dir = Path(__file__).resolve().parents[1]

# Load the preprocessing pipeline from a pickle file
with open(project_dir.joinpath('models/ModelXGboost.pkl'), 'rb') as f:
    model = dill.load(f)

# Define a function to make predictions
def predict(df):
    # Preprocess the data using the preprocessing function
    preprocessed_df = preprocess(df)
    
    # Make predictions using the model
    predictions = model.predict(preprocessed_df)
    
    # Return the predictions as a Pandas dataframe
    return pd.DataFrame(predictions)