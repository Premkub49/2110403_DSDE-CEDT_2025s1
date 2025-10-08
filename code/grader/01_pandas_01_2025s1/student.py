import pandas as pd
import json


def Q1(df):
    """
        1. For Q1, please return the shape of the data
    """
    # TODO: Paste your code here
    return df.shape


def Q2(df):
    '''
        2. For Q2, please return the max score of the data
    '''
    # TODO: Paste your code here
    return df['score'].max()


def Q3(df):
    '''
        3. For Q3, please return the total student that have score equal or more than 80 points
    '''
    # TODO: Paste your code here
    return len(df[df['score'] >= 80])


def Q4(df):
    '''
        4. Otherwise, just return “No Output”
    '''
    # TODO:  Paste your code here
    return "No Output"
