# import libraries
import pandas as pd
from sqlalchemy import create_engine
import sys


def load_data(messages_filepath, categories_filepath):
    """
    Load in messages and categories data from filepaths provided.
    """

    # load messages dataset
    messages = pd.read_csv(messages_filepath)

    # load categories dataset
    categories = pd.read_csv(categories_filepath)
    
    # merge datasets
    df = messages.merge(categories, on='id', how='outer')
    
    return df


def clean_data(df):
    """
    Clean the data by creating target columns.
    """
    ## Split 'categories' into separate category columns.

    # create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(';', expand=True)

    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing

    category_colnames = row.apply(lambda x: x[0:-2]).tolist()

    # rename the columns of `categories`
    categories.columns = category_colnames

    #Convert category values to just numbers 0 or 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str.slice(-1)

        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
        
        # Make binary
        categories[column] = categories[column].apply(lambda x: 1 if x >= 1 else 0)

    # drop the original categories column from `df`
    df = df.drop(columns='categories')

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,categories], axis=1)

    # drop duplicates
    df = df.drop_duplicates()
    
    return df

def save_data(df, database_filepath):
    """
    Save the data into an sqlite db
    """
    # Save the clean dataset into an sqlite database
    engine = create_engine('sqlite:///'+database_filepath)
    df.to_sql('msg_cat_clean', engine, index=False, if_exists='replace')  


def main():
    """
    ETL function. Runs the Extract, Transform and Load steps.
    """
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()