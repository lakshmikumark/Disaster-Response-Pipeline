
import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):

    # load messages, categories datasets
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categaories_filepath)
    
    # merge the datasets
    df = pd.merge(messages,categories, on='id')
    
    return df


def clean_data(df):
    """ 
    input:
    a pandas dataframe before data clean
    
    output:
    a pandas dataframe after data clean
    """
    
    # create a dataframe of the individual category columns
    categories = df.categories.str.split(pat=';', expand=True)
    # select the first row of the categories dataframe
    row = categories.iloc[0,:]
    # use this row to extract a list of new column names for categories
    category_colnames = row.apply(lambda x:x[:-2])
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    # set each value to be the last character of the string and convert this to numeric
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(np.int)
    
    # drop the original categories column from `df` and concatenate with the new'categories' df
    df = df.drop('categories' , axis=1) 
    df = pd.concat([df, categories],axis=1)
    
    # drop duplicates
    df = df.drop_duplicates()
    
    return df

def save_data(df, database_filename):
    """ 
    input:
    a cleaned pandas dataframe
    
    output:
    save the dataframe into a sqllite database
    """
    
    # save the clean dataset into a sqlite database
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('df', engine, index=False , if_exists='replace')
    
def main():
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
