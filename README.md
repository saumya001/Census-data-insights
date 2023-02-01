# Census-data-insights

This repository consists of income dataset from a Census. 

## Details
This repository contains a file called “Input_Dataset”. This dataset provides insights about the general population at the time the Census was conducted. The gathered information includes data on age, gender, country of origin, marital status, housing conditions, marriage, education, employment and some other fields. 

## Goal
The task is to persist this data for future use and derive some insights from it.

### Ingesting data into database
The dataset is cleaned and afterwards a database schema is created. Furthermore, a script is created which can upload the data from the Input_Dataset file to the SQLite database 'census.db'.

### Deriving insights
The code also derives interesting insights from the data provided.