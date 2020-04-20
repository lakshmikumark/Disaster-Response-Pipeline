# Disaster-Response-Pipeline
Classifying numerous messages during a disaster, so that the help would reach the needy quickly and accurately.

## The libraries used:
Pandas,
Numpy,
re,
nltk
sqlalchemy,
sklearn.model_selection,
sklearn.multioutput,
sklearn.ensemble,
sklearn.feature_extraction,
sklearn.base,
sklearn.pipeline,
sklearn.model_selection,
sklearn.metrics


## The motivation for the project

This project is to use ETL pipeline and ML pipeline and build a supervised learning model. This model categorizes the messages into 36 different categories.

This project is divided to 3 parts:
1. Create an ETL Pipeline - to extract, clean and load the data in a SQLite database.
2. Create a machine learning Pipeline - to train a NLP classifier.
3. Create a web application - to show the results in a web applications.

## The files in the repository


## Instructions

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Acknowledgements:
1. Udacity
2. www.stackoverflow.com
3. https://pandas.pydata.org/docs/
