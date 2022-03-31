



# Project 1: Write a Data science blog


For this project, you will pick a dataset and answer 3 questions using the data. My questions are:
1. Is there seasonality in price?
2. Does price vary by neighbourhood?
3. What price should I set my property at in order to be similar to the others?

Contents:

1. [ Data ](#p1)
2. [ Notebooks ](#p2)
3. [ Blog ](#p3)


<a name="p1"></a>
### Data 

| Data        | Description           | Source           | 
| ------------- |-------------|-------------| 
| listings.csv     |Full descriptions and average review score| https://www.kaggle.com/airbnb/seattle | 
| calendar.csv     |Listing id and the price and availability for that day| https://www.kaggle.com/airbnb/seattle |  

<a name="p2"></a>
### Notebooks


| Notebook        | Description           |
| ------------- |-------------|
| 0_listing_data_prep.ipynb  |This notebook uses listings.csv as an input and outputs listings_clean.csv which is a clean version for modelling and used in Q2 and Q3.| 
| 1_q1.ipynb    |This notebook uses calendar.csv as an input and outputs a graph to answer q1.| 
| 1_q2.ipynb   |This notebook uses listings_clean.csv as an input and outputs a graph to answer q2. Run 0_listing_data_prep.ipynb first.| 
| 1_q3.ipynb    |This notebook uses listings_clean.csv as an input and outputs a valur to answer q3. Run 0_listing_data_prep.ipynb first.| 

<a name="p3"></a>
### Blog post

The answers to the questions are presented to a non-technical audience on a blog post, here:

https://medium.com/@emma.mckinley/airbnb-seattle-advanced-analytics-72804206934f
