# Project 2: Disaster response model and web app

Analyse disaster data from Figure Eight to build a model for an API that classifies disaster messages. Working with a data set containing real messages that were sent during disaster events and creating a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency. The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data.
This project will utilise my software skills, including my ability to create basic data pipelines and write clean, organized code!

Contents:
1. [ Data ](#p1)
2. [ Notebooks ](#p2)
3. [ Notebooks ](#p3)
4. [ Classifications ](#p4)
5. [ Visualisations ](#p5)
6. [ Instructions ](#p6)
7. [ Acknowledgements ](#p7)
8. [ Extra tips ](#p8)

<a name="p1"></a>
### Data 

| Data        | Description           | 
| ------------- |-------------|
| disaster_messages.csv     |Contains the disaster messages that features will be created from| 
| disaster_categories.csv     |Contains the target variables| 

<a name="p2"></a>
### Files


| Notebook        | Folder           |Description           |
| ------------- |-------------| -------------|
| process_data.py  | data | ETL code| 
| train_classifier.py  | models|Build model code. See final model| 
| run.py |app | Backend code. Runs plotly to build graphs.| 
| go.html  |app/templates | Frontend html code. This has not been changed at the time of submitting the project.| 
| master.html    |app/templates  | Frontend html code. This has not been changed at the time of submitting the project.| 

<a name="p3"></a>
### Installations

The model has been tested on Python version 3.6 and requires the following packages:
*pandas, sqlalchemy, sys, pickle, nltk, sklearn, json, plotly, wordcloud, matplotlib, flask.*

<a name="p4"></a>
### Classifications
The web app inlcudes the functionality to enter a disaster message and it will predict the categories using the model. This uses a Random Forest classifier optimised using GridSearchCV(). Here is a screenshot of this functionality:
![image](https://user-images.githubusercontent.com/99752996/161022077-9bfd0909-3834-43e0-879e-dbd8de3ba3b7.png)

<a name="p5"></a>
### Visualisations

1. The project came with the first chart:
![image](https://user-images.githubusercontent.com/99752996/161022197-fd0488dd-9928-491d-ae7a-e5d7c902cac8.png)

2. I created a wordcloud to visualise some of the key words appearing across all the messages. This might even help the user word some of their messages in a way similar to others which may lead to the model making better predictions. <br>
![image](https://user-images.githubusercontent.com/99752996/161022286-a84558a0-1b82-481e-9bc5-b92827f9c8ca.png)

3. It's also useful to understand the distributions of categories in the data. Particularly if any have low volumes of 1,2 because the model may not accurately predict for these categories.
![image](https://user-images.githubusercontent.com/99752996/161022377-282f82b9-d9d0-4f22-b72b-a898be3780d7.png)

<a name="p6"></a>
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

<a name="p7"></a>
### Acknowledgements

I found a function online which plotted a word cloud using plotly, see here: <br>
https://github.com/PrashantSaikia/Wordcloud-in-Plotly/blob/master/plotly_wordcloud.py

I used a feature generator provided in this course called starting_verb. Thank-you to whoever created this.


<a name="p8"></a>
### Extra tips

* You can further look into deploying application on Heroku.

* You can also use following message format for providing more structured message.
 Bugfix: bugfix message
 Update: update message
 Correction: correction message
 Added: files added or whatever
 
 * Initialize verbose=3 in GridSearchCV() class to get extra messages
