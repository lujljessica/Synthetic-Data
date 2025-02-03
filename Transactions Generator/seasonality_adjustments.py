import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def adjust_yearly_seasonality(transaction_date: datetime,
                              base_quantity: int,
                              store_weights: list):
    """
    ARGS: 
    transaction_date: a datetiime object - date the transaction is happening. 
    base_quantity: int -  current quantity of items
    store_weights: list - list of 2 items with minimum and maximum items in that store. 
                          Helps create randomness between stores
    Return 
    int -  quantity of items after adjustments
    
    Adjustments to quantity: 
    after the adjustments of the yearly seasonality - increase quantity in December and decrease in January 
    """
    
    if transaction_date.month == 12:
        _min  = store_weights[0] +  np.random.randint(1, 7)
        _max = ((store_weights[0] + store_weights[1]) + np.random.randint(1, 5))
        quantity = base_quantity + np.random.randint(_min, _max) 
        return  quantity    
    elif transaction_date.month == 1:
        _min =  store_weights[0] - store_weights[1]//2
        _max  =  store_weights[0]
        quantity = base_quantity + np.random.randint(_min, _max)
    return base_quantity + np.random.randint( - store_weights[0], store_weights[1])

def adjust_monthly_seasonality(transaction_date: datetime,
                              base_quantity: int,
                              store_weights: list):
    """
    ARGS: 
    transaction_date: a datetiime object - date the transaction is happening. 
    base_quantity: int -  current quantity of items
    store_weights: list - list of 2 items with minimum and maximum items in that store. 
                          Helps create randomness between stores
    Return 
    int -  quantity of items after adjustments
    
    Adjustments to quantity: 
    Increase sales in month end and middle of the month - ie during pay days
    """
    
    if transaction_date.day in [ 30,31]: # increase around pay days
        return base_quantity + np.random.randint(store_weights[0],store_weights[1]) + np.random.randint(1,store_weights[1])
    if transaction_date.day in [15, 16]: # increase around pay days - some people get paid bi-monthly
        return base_quantity + np.random.randint(0,store_weights[0] + 5)
    
    return base_quantity + np.random.randint(- 2 ,store_weights[1])

def adjust_weekly_seasonality(transaction_date: datetime,
                              base_quantity: int,
                              store_weights: list):
    """
    ARGS: 
    transaction_date: a datetiime object - date the transaction is happening. 
    base_quantity: int -  current quantity of items
    store_weights: list - list of 2 items with minimum and maximum items in that store. 
                          Helps create randomness between stores
    Return 
    int -  quantity of items after adjustments
    
    Adjustments to quantity: 
    Increase sales around weekend
    """
    if transaction_date.weekday() in [5, 6]:  # Saturday, Sunday
        return   base_quantity + np.random.randint(1, store_weights[0]+3)
    return base_quantity 

def add_trend_factor(base_quantity: float,
                     base_year: int,
                     current_year: int,
                     annual_growth_rate: float ):
    """
    Adds a trend factor to the base_number based on the current year.
    Args:
        base_quantity (float): The starting number.
        base_year (int): The reference year for the base_number -  the start year of our transactions
        current_year (int): current year
        annual_growth_rate (float): The growth rate per year
    Returns:
        float: The number of items adjusted by the trend factor.
    """
    years_elapsed = current_year - base_year
    trend_factor = (1 + annual_growth_rate) ** years_elapsed
    adjusted_number = int(base_quantity * trend_factor)
    
    return adjusted_number
