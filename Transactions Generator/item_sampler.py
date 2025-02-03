import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


def get_sampled_item(items_df, weights_dict):    
    """
    Samples a random item from items_df based on category weights.
    
    Args:
        items_df (pd.DataFrame): DataFrame containing items with a 'Category' column.
        weights_dict (dict): Dictionary of category weights.
        
    Returns:
        pd.Series: A random row from the filtered DataFrame.
    """
    category_weights = []
    total_weight = sum(weights_dict.values())
    if total_weight == 0:
        raise ValueError("The total of weights cannot be zero.")
        
    category_weights = {key: value / total_weight for key, value in weights_dict.items()}
    
    categories = list(category_weights.keys())
    probabilities = list(category_weights.values())
    chosen_category = np.random.choice(categories, p=probabilities)
    
    filtered_df = items_df[items_df['Category'] == chosen_category]
    
    if filtered_df.empty:
        raise ValueError(f"No items found in the chosen category: {chosen_category}")
    
    sampled_item = filtered_df.sample(n=1).iloc[0]
    return sampled_item
