#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split

def split_telewire_data(input_filepath, output_folder):
    """This function splits an input dataset into train
    and test sets, and saves these in the output_folder.

    Parameters
    ----------
    input_filepath : string
        Full path, incl. filename, for the input dataset.
        This must be a .csv file.
    output_folder : string
        Folder location to store split data files.

    Returns
    -------
    Null
    
    Examples
    --------
    >>> input_file = '../data/raw/data.csv'
    >>> output_loc = '../data/raw/'
    >>> split_data(input_file, output_loc)
    """

    # Unit tests
    assert input_filepath[-4:] == '.csv', "Input file has to be .csv!"               #Check that input file is .csv
    # read the csv file using pandas
    cell_tower_data = pd.read_csv(input_data_path, encoding = "windows-1254")
    
    # test size should be between 0 and 1
    # random_state is any integer number
    training_data, testing_data = train_test_split(cell_tower_data, test_size=0.3, random_state=11)
    
    # saving the train and test data in different files
    training_data.to_csv(output_folder+'train.csv')
    testing_data.to_csv(output_folder+'test.csv')


def get_train_data():
    train_data = pd.read_csv('../data/raw/train.csv',  encoding= 'unicode_escape')
    y_train = train_data["Unusual"]                      #defining the labels
    X_train = train_data.drop(["Unusual"], axis=1)

    return X_train,y_train

def get_test_data():
    test_data = pd.read_csv('../data/raw/test.csv',  encoding= 'unicode_escape')
    y_test = test_data["Unusual"]                      #defining the labels
    X_test = test_data.drop(["Unusual"], axis=1)
    return X_test,y_test


input_data_path ='../data/raw/data.csv'
output_data_path = '../data/raw/'

# funtion call
split_telewire_data(input_data_path, output_data_path)

