import pandas as pd
import numpy as np

def total_listings(df):
    #we could us len(df) or df.shape[0]
    return len(df)

def average_price(df):
    return round( df["price"].mean(), 2)

def median_price(df):
    return round( df["price"].median(), 2)

def average_reviews(df):
    return round( df["number_of_reviews"].mean(), 2)

def occupancy_rate(df):
    return round((df["estimated_occupancy_l365d"].mean() / 365) * 100, 2)

def revenue_potential(df):
    return round(df["estimated_revenue_l365d"].mean(), 2)