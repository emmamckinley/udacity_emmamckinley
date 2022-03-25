import sys
import pandas as pd
import pickle
from sqlalchemy import create_engine
from sqlalchemy import inspect
    
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion

from sklearn.metrics import classification_report


def load_data(database_filepath):
    """ A function to load in the data created in the ETL stage """
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('msg_cat_clean', engine)
    X = df['message']
    y = df.iloc[:,4:]
    return X, y

class StartingVerbExtractor(BaseEstimator, TransformerMixin):
    """ A class to create extra NLP features. """
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

def tokenize(text):
    """ A function to create extra NLP features. """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """ A function which builds the model. It is a model with 3 transformers, Random forest, with Gridsearch. """
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ])),

            ('starting_verb', StartingVerbExtractor())
        ])),

        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    # print( pipeline.get_params().keys() )
    
    parameters = {
        'clf__estimator__min_samples_split': [2, 3, 4]
    }

    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv


def evaluate_model(model, X_test, Y_test):
    """ A function which evaluates the model giving a classification report for all the target fields. """
    y_pred = model.predict(X_test)
    for target in range(0,36):
        y_test_temp  = Y_test.iloc[:, target]
        y_pred_temp  = y_pred[:, target]
        print('classification report for target', Y_test.columns[target])
        print('')
        print(classification_report(y_test_temp,y_pred_temp))


def save_model(model, model_filepath):
    """ A function which saves the model to a pickle file. """
    with open(model_filepath, "wb") as f:
        pickle.dump(model, f)


def main():
    """ A function which runs all the steps to load data, split into train and test, build model, print evaluation        results and save the final model to a pickle file."""
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()