# Census-data-insights

This repository consists of income dataset from a Census. 

## Details
This repository contains a file called “Input_Dataset”. This dataset provides insights about the general population at the time the Census was conducted. The gathered information includes data on age, gender, country of origin, marital status, housing conditions, marriage, education, employment and some other fields. 

## Goal
The task is to persist this data for future use and derive some insights from it.

### Ingesting data into database
The dataset is cleaned and afterwards a database schema is created. Furthermore, a script is created which can upload the data from the cleaned input.csv file to the SQLite database 'census.db'.

### Deriving insights
The code also derives interesting insights from the data provided in notebook data_insights.ipynb

### API Endpoint
There is a simple API endpoint in file api.py with which users can query the database for defined filter parameters from the dataset and receive a JSON response.

#### Requirements
Following are the required libraries:
- pandas
- numpy
- math
- sqlite3
- csv
- matplotlib
- seaborn

Please install flask and flask_cors in order to run api.py

- pip install flask
- pip install Flask-Cors
