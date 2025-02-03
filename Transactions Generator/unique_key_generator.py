import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_random_code(len):
    """
    Returns a random number 
    Args:
        len (int) length of the number 
    """
    if len == 2:
        return np.random.randint(10, 99)
    elif len == 3:
        return np.random.randint(100, 999)
    elif len == 4:
        return np.random.randint(1000, 9999)
    elif len == 5:
        return np.random.randint(10000, 99999)
    elif len == 6:
        return np.random.randint(100000, 999999)
    
def generate_keys_for_column(column_name, key_length, df):
    """
    Pass in the column_name,length and data frame you want a unique code added for 
    Args:
        - column_name (string) of the column that needs a key
        - key_length (int) - number of digits of the generated key
        - df (pd.dataframe)
    Return:
        A pd.dataframe with the new ID name
    """

    IDs = {column_name: generate_random_code(key_length) for column_name in df[column_name].unique()}
    if " Name" in column_name:
        new_column_name = column_name.replace(" Name", "")
        new_column_name = f'{new_column_name}_ID'
    else:
        new_column_name = f'{column_name}_ID'
    df[new_column_name] = df[column_name].map(IDs)
    return df

def generate_transaction_ID(store, date, time):
    """
    Simple way to get a unique ID for each transaction by using store name and the date time object
    """
    formatted_date = date.strftime("%Y%m%d")
    formatted_time = time.strftime("%H%M%S")
    return store + "_" + formatted_date + "_" +formatted_time