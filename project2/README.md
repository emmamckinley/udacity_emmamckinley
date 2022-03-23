# Disaster Response Pipeline Project



```diff
+ This file contains instructions to build the web app. 
- For full details on the project and file descriptions see README.md in the main repository directory.
```

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Now, open another Terminal Window.

    Run the following:
    env|grep WORK

    You'll see output that looks something like this:
![webappaddress](https://user-images.githubusercontent.com/99752996/159735625-c2ff8aac-27d9-49a4-84a2-1c9dbc59d6d0.png)


    In a new web browser window, type in the following:
    https://SPACEID-3001.SPACEDOMAIN
    In this example, that would be: "https://viewa7a4999b-3001.udacity-student-workspaces.com/" (Don't follow this link now, this is just an example.)

    You should be able to see the web app. The number 3001 represents the port where your web app will show up. Make sure that the 3001 is part of the web      address you type in.
