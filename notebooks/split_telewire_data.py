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
    >>> input_file = '../data/raw/telewire_analytics_cell_tower_data.csv'
    >>> output_loc = '../data/raw/'
    >>> split_data(input_file, output_loc)
    """

    # Unit tests
    assert input_filepath[-4:] == '.csv', "Input file has to be .csv!"               #Check that input file is .csv
    
    # read the csv file using pandas
    cell_tower_data = pd.read_csv(input_filepath, encoding = "windows-1254")
    
    # test size should be between 0 and 1
    # random_state is any integer number
    training_data, testing_data = train_test_split(cell_tower_data, test_size=0.3, random_state=11)
    
    # saving the train and test data in different files
    training_data.to_csv(output_folder+'train.csv')
    testing_data.to_csv(output_folder+'test.csv')

input_data_path = 'C:/Users/Harsh Patel/Desktop/Loyalist Term 4/AIP/TBC-AIP-2023-A7_Telewire-Analytics/data/raw/Telewire Analytics Cell_tower_data.csv'
output_data_path = 'C:/Users/Harsh Patel/Desktop/Loyalist Term 4/AIP/TBC-AIP-2023-A7_Telewire-Analytics/data/raw/'

# funtion call
split_telewire_data(input_data_path, output_data_path)