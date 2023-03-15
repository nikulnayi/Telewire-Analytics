# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from joblib import load
import dill
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    project_dir = Path(__file__).resolve().parents[2]
    try:
        try:
            # Getting Data
            data = pd.read_csv(input_filepath,  encoding= 'unicode_escape')
            logger.info('Data Loaded Sucessfully')
        except ValueError: 
            logger.info('Loading Data Error:',ValueError)
        
        try:
        # Define the model pipeline
            with open(project_dir.joinpath('notebooks/pipelines/PreprocessingPipeline2.0.pkl'), 'rb') as f:
                pipeline = dill.load(f)
            logger.info('Processing Pipeline Loaded')
        except ValueError: 
            logger.info('TError in loading processing pipeline :',ValueError)

        try:
            pd.DataFrame(pipeline.fit_transform(data)).to_csv(output_filepath, index=False)
            logger.info('Saved Processed Data at..',output_filepath)
        except ValueError: 
            logger.info('Saving CSV Error',ValueError)
    except ValueError:
        logger.info('Operation Failed',ValueError)
    


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    load_dotenv(find_dotenv())

    main()
