# udacity_emmamckinley
Udacity Data Science nanodegree
# Project 1: Write a Data science blog

For this project, you will pick a dataset and answer 3 questions using the data. My questions are:
1. Is there seasonality in price?
2. Does price vary by neighbourhood?
3. What price should I set my property at in order to be similar to the others?

### Data 

| Data        | Description           | Source           | 
| ------------- |-------------|-------------| 
| listings.csv     |Full descriptions and average review score| https://www.kaggle.com/airbnb/seattle | 
| calendar.csv     |Listing id and the price and availability for that day| https://www.kaggle.com/airbnb/seattle |  


### Notebooks


| Notebook        | Description           |
| ------------- |-------------|
| 0_listing_data_prep.ipynb  |This notebook uses listings.csv as an input and outputs listings_clean.csv which is a clean version for modelling and used in Q2 and Q3.| 
| 1_q1.ipynb    |This notebook uses calendar.csv as an input and outputs a graph to answer q1.| 
| 1_q2.ipynb   |This notebook uses listings_clean.csv as an input and outputs a graph to answer q2. Run 0_listing_data_prep.ipynb first.| 
| 1_q3.ipynb    |This notebook uses listings_clean.csv as an input and outputs a valur to answer q3. Run 0_listing_data_prep.ipynb first.| 

### Blog post

The answers to the questions are presented to a non-technical audience on a blog post, here:

https://medium.com/@emma.mckinley/airbnb-seattle-advanced-analytics-72804206934f


# Project 2: 

In this course, you've learned and built on your data engineering skills to expand your opportunities and potential as a data scientist. In this project, you'll apply these skills to analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages.

In the Project Workspace, you'll find a data set containing real messages that were sent during disaster events. You will be creating a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency.

Your project will include a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. This project will show off your software skills, including your ability to create basic data pipelines and write clean, organized code!

### How to run the Python scripts and web app

See README.md in project2 folder.

### Data 

| Data        | Description           | 
| ------------- |-------------|
| disaster_messages.csv     |Contains the disaster messages that features will be created from| 
| disaster_categories.csv     |Contains the target variables| 


### Files


| Notebook        | Folder           |Description           |
| ------------- |-------------| -------------|
| process_data.py  | data | ETL code| 
| train_classifier.py  | models|Build model code. See final model| 
| run.py |app | Backend code. Runs plotly to build graphs.| 
| go.html  |app/templates | Frontend html code. This has not been changed at the time of submitting the project.| 
| master.html    |app/templates  | Frontend html code. This has not been changed at the time of submitting the project.| 


### Model

The model was chosen as this gave the highest f1-score. f1-score is a balance between recall/precision but would need more information to decide whether this is the best metric to us. The f1-score is a weighted average of the f1-scores for all response levels. 
The following models were considered:

* Random Forest classifier using 2 transformers
* Random Forest classifier using 2 transformers with gridsearch
* Random Forest classifier using 3 transformers
* kn neighbours with 3 transformers
* kn neighbours with 3 transformers with gridsearch

The kn neighbours with 3 transformers with gridsearch was chosen as this was the best average f1-score across all 36 targets vars.
