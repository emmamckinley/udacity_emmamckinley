# udacity_emmamckinley
Udacity Data Science nanodegree

1. [ Project 1 ](#p1)
2. [ Project 2 ](#p2)


<a name="p1"></a>
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


<a name="p2"></a>
# Project 2: Disaster response model and web app

Analyse disaster data from Figure Eight to build a model for an API that classifies disaster messages. Working with a data set containing real messages that were sent during disaster events and creating a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency.

The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. 

This project will utilise my software skills, including my ability to create basic data pipelines and write clean, organized code!

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


### Installations

The model has been tested on Python version 3.6 and requires the following packages:
*pandas, sqlalchemy, sys, pickle, nltk, sklearn, json, plotly, wordcloud, matplotlib, flask.*

### Model

Different models were tested based on f1-score. f1-score is a balance between recall/precision but would need more information to decide whether this is the best metric to us. The f1-score looked at is a weighted average of the f1-scores for all response levels. 
The following models were considered:

* Random Forest classifier using 2/3 transformer with gridsearch
* kn neighbours with 3 transformers

The kn neighbours with 3 transformers had the best average f1-score across all 36 targets vars however, the Random Forest model with gridsearch was submitted as a Gridsearch was required. 

### Classifications
The web app inlcudes the functionality to enter a disaster message and it will predict the categories using the model. Here is a screenshot of this functionality:

### Visualisations

1. The project came with the first chart, a graph of

2. I created a wordcloud to visualise some of the key words appearing across all the messages. This might even help the user word some of their messages in a way similar to others which may lead to the model making better predictions.

4. It's also useful to understand the distributions of categories in the data. Particularly if any have low volumes of 1,2 because the model may not accurately predict for these categories.

### Instructions
Run the following commands in the project's root directory to set up your database and model.

ETL pipeline (cleans data and stores in database)
**python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db**
ML pipeline (trains classifier and saves) 
**python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl**
Run the following command in the app's directory to run your web app. 
**python run.py**

To open the web app.
* Open another Terminal Window.
* Run the following: 
  **env|grep WORK**
  You'll see output that looks something like this:
<img src="https://user-images.githubusercontent.com/99752996/159735625-c2ff8aac-27d9-49a4-84a2-1c9dbc59d6d0.png" alt="webappaddress"/>

* In a new web browser window, enter the following: https://SPACEID-3001.SPACEDOMAIN

### Acknowledgements

I found a function online which plotted a word cloud using plotly, see here: <br>
https://github.com/PrashantSaikia/Wordcloud-in-Plotly/blob/master/plotly_wordcloud.py

I used a feature generator provided in this course called starting_verb. Thank-you to whoever created this.
