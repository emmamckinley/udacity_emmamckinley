
# Imports:
import json
import plotly
import sys
import pickle

# Required for data
import pandas as pd
from sqlalchemy import create_engine

# Required for model
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'stopwords'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import classification_report
from sklearn.externals import joblib

# Required for graphs
from plotly.graph_objs import Bar
from plotly.graph_objs import Scatter
from plotly.graph_objs import Layout
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# For web app
from flask import Flask
from flask import render_template, request, jsonify


# start Flask
app = Flask(__name__)

# A class required within model
class StartingVerbExtractor(BaseEstimator, TransformerMixin):
    """
    A NLP function which creates new features.
    """

    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return True
        return False

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)

# A function required in model
def tokenize(text):
    """
    A NLP function which creates new features.
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

def tokenize_stop(text):
    """ A function to create extra NLP features. Tokenize and remove stop words """
    #tokenize
    tokens = word_tokenize(text)
    # Remove stop words
    words = [w for w in tokens if w not in stopwords.words("english")]
    
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in words:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# set-up word cloud that works in Plotly
# Reference: https://github.com/PrashantSaikia/Wordcloud-in-Plotly/blob/master/plotly_wordcloud.py
def plotly_wordcloud(text):
    """
    A function to plot a wordcloud with plotly.
    """
    wc = WordCloud(stopwords = set(STOPWORDS),
                   max_words = 200,
                   max_font_size = 100)
    wc.generate(text)
    
    word_list=[]
    freq_list=[]
    fontsize_list=[]
    position_list=[]
    orientation_list=[]
    color_list=[]

    for (word, freq), fontsize, position, orientation, color in wc.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)
        
    # get the positions
    x=[]
    y=[]
    for i in position_list:
        x.append(i[0])
        y.append(i[1])
            
    # get the relative occurence frequencies
    new_freq_list = []
    for i in freq_list:
        new_freq_list.append(i*100)
    new_freq_list
    
    trace = Scatter(x=x, 
                       y=y, 
                       textfont = dict(size=new_freq_list,
                                       color=color_list),
                       hoverinfo='text',
                       hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)],
                       mode='text',  
                       text=word_list
                      )
    
    return trace

# Set-up data for graph 3
def create_bars(cat_list, counts_list, name): 
    """
    A function which creates bars on a graph
    """
    trace = Bar(
    x=cat_list,
    y=counts_list,
    name=name 
    )
    return trace

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('msg_cat_clean', engine)

# Restructure table for graph 3
# Put value_counts of all the target columns into a dataframe (stacked vertically)

# Set-up table with the target columns (minus first) and a table containing only the first
y = df.iloc[:,5:]
y_0 = df.iloc[:,4:5]
column_name_0 = y_0.columns[0]

# initiate table with 1st category
# put value counts of the first category into a df
value_counts = y_0[column_name_0].value_counts(dropna=False, sort=True)
df_val_counts = pd.DataFrame(value_counts)
all_vc = df_val_counts.reset_index()
all_vc.columns = ['unique_values', 'counts'] # change column names
all_vc['category'] = column_name_0

# Loop round all other categories and append value counts 
for c in y.columns:
    
    value_counts = y[c].value_counts(dropna=False, sort=True)
    df_val_counts = pd.DataFrame(value_counts)
    df_value_counts_reset = df_val_counts.reset_index()
    df_value_counts_reset.columns = ['unique_values', 'counts'] # change column names
    df_value_counts_reset['category'] = c
    all_vc = pd.concat([all_vc, df_value_counts_reset])
    
# Get a list of categories from the value_counts table    
cat_list = all_vc['category'].unique().tolist()

# For each value in the unique_values (in this case 0,1,2) and for each category find the counts and put this into counts_list
# counts_list will contain all the counts for a particuar unique_values
# Run the function create_bars to turn create a trace (A bar on the chart)
# The final output of this stage is trace_list which will be plugged into the graphs section later

trace_list = []
counts_list= []
for i in range(0, all_vc['unique_values'].max() + 1): 
    counts_list = []
    for c in cat_list:
        values_i = all_vc[(all_vc['unique_values'] == i) & (all_vc['category'] == c)]
        val = values_i['counts'].sum() # using sum to convert to values. This doesn't sum anything as 1 value is returned.
        counts_list.append(val)
    
    trace = create_bars(cat_list, counts_list, i)
    trace_list.append(trace)

# load model
model = joblib.load("../models/classifier.pkl")

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
 
    # Read in all the text from all messages into a single string for the word cloud
    text = " ".join(review for review in df.message)
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        }
       
        ,
                {
            'data': [
                plotly_wordcloud(text)
            ],

            'layout': Layout({
                        'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'title': 'Words in all Messages'}
                            )
        }
        
        ,
        
        {
            'data': trace_list,

            'layout': Layout(
    barmode= 'stack',
    title='Target values',
    xaxis=dict(title='Category'),
    yaxis=dict(title='Count')
    )
        }
        
       
    ]
       
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    """
    renders html
    """
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    """
    pushs web app live
    """
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()