import nltk
import pandas as pd 
import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

ace = pd.read_csv('Ace_KYD.csv')
ireaderinokun = pd.read_csv('ireaderinokun.csv')
markessien = pd.read_csv('markessien.csv')
mykeels = pd.read_csv('mykeels.csv')
OluwaYettie = pd.read_csv('OluwaYettie.csv')
risin_developer = pd.read_csv('risin_developer.csv')
robert_thas = pd.read_csv('robert_thas.csv')
unicodeveloper = pd.read_csv('unicodeveloper.csv')

tweets = pd.concat([ace,ireaderinokun,markessien,OluwaYettie,mykeels,risin_developer,robert_thas,unicodeveloper])

out = stopwords.words('english')
def text_process(text):

    no_punc = [c for c in text if c not in string.punctuation]
    no_punc = ''.join(no_punc)
    no_punc = no_punc.split()
    return [word for word in no_punc if word.lower() not in stopwords.words('english')]

tweets['tweet'].apply(text_process)

bow_transformer = CountVectorizer(analyzer=text_process).fit(tweets['tweet'])
messages_bow = bow_transformer.transform(tweets['tweet'])

tfidf_transformer = TfidfTransformer().fit(messages_bow)

messages_tfidf = tfidf_transformer.transform(messages_bow)

X_train,X_test,y_train,y_test = train_test_split(tweets['tweet'],tweets['name'],test_size=0.3,random_state=101)
pipeline = Pipeline([
    ('bow',CountVectorizer(analyzer=text_process)),
    ('tfidf',TfidfTransformer()),
    ('classifier',MultinomialNB())
    ])

pipeline.fit(X_train,y_train)

predictions = pipeline.predict(X_test)
# print(classification_report(y_test,predictions))
user_tweet = input("Drop the tweet here, let's find the person ")
print(pipeline.predict([user_tweet]))