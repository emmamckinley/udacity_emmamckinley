# Captone: Mail-order Customer data

This project was completed as part of my Data Science nanodegree from Udacity where I have chosen to analyse data provided Arvato Financial Services. The data contains attributes of customers from a mail-order service in Germany and attributes of the general population of Germany.

Contents:

1. [ Data ](#p1)
2. [ Notebooks ](#p2)
3. [ Requirements ](#p4)
4. [ Blog ](#p3)

<a name="p1"></a>
### Data 

The below data has been provided but not uploaded to github, as per the terms and conditions within the project. They can be found at the following location within the project workspace on udacity: ../../data/Term2/capstone/arvato_data/


| Data        | Description     | 
| ------------- |-------------|
| Udacity_AZDIAS_052018.csv     |Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns).| 
| Udacity_CUSTOMERS_052018.csv     | Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns).|  
| Udacity_MAILOUT_052018_TRAIN.csv     |Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns).|  
| Udacity_MAILOUT_052018_TEST.csv     |Demographics data for individuals who were targets of a marketing campaign; 42 833 persons (rows) x 366 (columns).|  
| DIAS Attributes - Values 2017.xlsx    |Data Dictionary containing the levels of the categorical columns|  
| DIAS Information Levels - Attributes 2017.xlsx    |Data Dictionary containing the columns names and the level of information e.g. Person, Household, Neighbourhood|  

Using the data dictionaries I also created the following files:

| Data        | Description     | 
| ------------- |-------------|
| fieldnames.csv    |List of Columns in DIAS Information Levels - Attributes 2017.xlsx | 
| valuenames.csv     |List of Columns in DIAS Attributes - Values 2017.xlsx |  
| labels.csv  | A tidy version of DIAS Attributes - Values 2017.xlsx that can be used to label the graphs. Only includes columns needed for visuals. |  
| unknown_values.csv    |One row per column in the data with an Unknown level coded as 0, 9 or -1. Will use this to set values to NULL.|  


<a name="p2"></a>
### Notebooks

| Notebook        | Description           | Inputs           | Outputs           |
| ------------- |-------------|-------------|-------------|
| 1_data_prep.ipynb * | Data prep | fieldnames.csv, valuenames.csv, unknown_values.csv, Udacity_AZDIAS_052018.csv, Udacity_CUSTOMERS_052018.csv. | customers_FR.csv, Germany_samp.csv, germany_FR.csv | 
| 2_unsupervised_learning.ipynb   |Unsupervised analysis for Customer Segmentation |customers_FR.csv, Germany_samp.csv, germany_FR.csv | none | 
| 3_supervised_learning.ipynb  | Builds a supervised model for target marketing |Udacity_MAILOUT_052018_TRAIN.csv, Udacity_MAILOUT_052018_TEST.csv | kaggle.csv | 

* exact results can not be replicated but since running I added a sort_values so the same results should be produced each time going forward.

<a name="p4"></a>
### Requirements 
The notebooks have been run in 2 separate environments.

1. 1_data_prep.ipynb.
Python version
3.6.3 | packaged by conda-forge | (default, Dec  9 2017, 04:28:46) 
[GCC 4.8.2 20140120 (Red Hat 4.8.2-15)]
Version info.
sys.version_info(major=3, minor=6, micro=3, releaselevel='final', serial=0)
numpy
1.12.1
pandas
0.23.3
matplotlib
2.1.0
scipy
1.2.1
itertools
- same as Python version

2. 2_unsupervised_learning.ipynb and 3_supervised_learning.ipynb.
I copied over the data to my work server as it is faster (Made a note to remove it after 2 weeks as per T&C)

<a name="p3"></a>
### Blog post

The project overview, results and acknowledgements are presented to a technical audience on a blog post, here:
https://medium.com/@emma.mckinley/airbnb-seattle-advanced-analytics-72804206934f


