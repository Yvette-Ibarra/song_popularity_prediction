# inmports
import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split

# Global Variables_______________________________________________________________

filename = 'song_data.csv'

# ________________________________________________________________________________


def fresh_data():
    '''
    This reads the zillow 2017 properties data from the Codeup db into a df.
    '''
    # Read in DataFrame from csv file.
    df = pd.read_csv(filename)
    return df

def acquire_data(new = False):
    '''
    Obtains the data from the csv file. 
    Next interation reads the data from the saved file
    Returns: pandas DataFrame
    '''

    # obtain cvs file
    if (os.path.isfile(filename) == False) or (new == True):
        df = fresh_data()
        #save as csv locally
        df.to_csv(filename,index=False)

    #cached data
    else:
        df = pd.read_csv(filename)
    
    return df

def data_prep(df):
    '''
    data_prep takes in dataframe and drops duplicates
    Returns cleaned dataframe
    '''
    df.drop_duplicates(inplace=True)
    
    return df

def split_data(df):
    '''
    split_data takes in data Frame and splits into  train , validate, test.
    The split is 20% test 80% train/validate. Then 30% of 80% validate and 70% of 80% train.
    Aproximately (train 56%, validate 24%, test 20%)
    Returns train, validate, and test 
    '''
    # split test data from train/validate
    train_and_validate, test = train_test_split(df, random_state=123, test_size=.2)

    # split train from validate
    train, validate = train_test_split(train_and_validate, random_state=123, test_size=.3)
                                   
    return train, validate, test
    
