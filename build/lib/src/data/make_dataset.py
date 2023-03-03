# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd
from sklearn.pipeline import Pipeline
from joblib import load


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)

    try:
        try:
            # Getting Data
            data = pd.read_csv(input_filepath,  encoding= 'unicode_escape')
            logger.info('Data Loaded Sucessfully')
        except ValueError: 
            logger.info('Loading Data Error:',ValueError)
        
        try:
        # Define the model pipeline
            pipeline = Pipeline([
                ('preprocessing', load('notebooks/pipelines/PreprocessingPipeline.pkl'))   
            ]) 
            logger.info('Data Processed Successfully')
        except ValueError: 
            logger.info('Transforming Data Error:',ValueError)

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

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
