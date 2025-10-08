import pandas as pd
import json

"""
    ASSIGNMENT 1 (STUDENT VERSION):
    Using pandas to explore youtube trending data from (videos.csv and category_id.json) and answer the questions.
"""


def Q1():
    """
        1. How many rows are there in the videos.csv after removing duplications?
        - To access 'videos.csv', use the path '/data/videos.csv'.
    """
    # TODO: Paste your code here
    df = pd.read_csv('/data/videos.csv')
    df_no_dup = df.drop_duplicates()
    return len(df_no_dup)


def Q2(vdo_df):
    '''
        2. How many VDO that have "dislikes" more than "likes"? Make sure that you count only unique title!
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    # TODO: Paste your code here
    df_dis_more_like = vdo_df.loc[vdo_df['dislikes'] > vdo_df['likes'], "title"].unique()
    return len(df_dis_more_like)


def Q3(vdo_df):
    '''
        3. How many VDO that are trending on 22 Jan 2018 with comments more than 10,000 comments?
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - The trending date of vdo_df is represented as 'YY.DD.MM'. For example, January 22, 2018, is represented as '18.22.01'.
    '''
    # TODO: Paste your code here
    return len(vdo_df[(vdo_df['comment_count'] > 10000) & (vdo_df['trending_date'].str.contains('18.22.01'))])


def Q4(vdo_df):
    '''
        4. Which trending date that has the minimum average number of comments per VDO?
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    # TODO:  Paste your code here
    df_group_publish = vdo_df.groupby(by=['trending_date'])
    df_date_min_avg = df_group_publish['comment_count'].mean().idxmin()
    return df_date_min_avg


def Q5(vdo_df):
    '''
        5. Compare "Sports" and "Comedy", how many days that there are more total daily views of VDO in "Sports" category than in "Comedy" category?
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - You must load the additional data from 'category_id.json' into memory before executing any operations.
            - To access 'category_id.json', use the path '/data/category_id.json'.
    '''
    # TODO:  Paste your code here
    import json
    from pandas import json_normalize
    with open("/data/category_id.json") as file:
        json_data = json.load(file)
    df_category_id = json_normalize(json_data, record_path=['items'])
    sports_id = int(df_category_id.loc[(df_category_id["snippet.title"] == "Sports") & (df_category_id["snippet.assignable"]), "id"].iloc[0])
    comedy_id = int(df_category_id.loc[(df_category_id["snippet.title"] == "Comedy") & (df_category_id["snippet.assignable"]), "id"].iloc[0])
    df_sports = vdo_df[vdo_df['category_id'] == sports_id]
    df_comedy = vdo_df[vdo_df['category_id'] == comedy_id]
    df_sports_sum = df_sports.groupby(by=['trending_date'], as_index=False)['views'].sum()
    df_comedy_sum = df_comedy.groupby(by=['trending_date'], as_index=False)['views'].sum()
    df_sports_comp_comedy = pd.merge(df_sports_sum, df_comedy_sum, on='trending_date', how='outer')
    df_sports_comp_comedy = df_sports_comp_comedy[((df_sports_comp_comedy['trending_date'].notna()) & ((df_sports_comp_comedy['views_y'].isna()) | (df_sports_comp_comedy['views_x'] > df_sports_comp_comedy['views_y'])))]
    return len(df_sports_comp_comedy)
