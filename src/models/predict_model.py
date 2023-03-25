import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.metrics import recall_score
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
import pickle
import argparse


def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, data):
    preds = model.predict(data)
    return preds

def main(args):
    # load pre-trained model
    model = load_model(args.model_path)
    
    # load new dataset
    new_data = pd.read_csv(args.data_path)
    
    # make predictions on new dataset
    preds = predict(model, new_data)
    
    # save predictions to file
    preds.to_csv(args.output_path, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, help='Path to pre-trained model')
    parser.add_argument('--data_path', type=str, help='Path to new dataset')
    parser.add_argument('--output_path', type=str, help='Path to output predictions')
    args = parser.parse_args()
    
    main(args)