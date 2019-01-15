import tweepy 
import pandas as pd
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

consumer_key = "XXXXXXXXXX"
consumer_secret = "XXXXXXXX"
access_key = "XXXXXX"
access_secret = "XXXXXXXXX"

username = input('Which handle do you want tweets from? ')

# Function to extract tweets 
def get_tweets(): 
	
	# Authorization to consumer key and consumer secret 
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

	# Access to user's access key and access secret 
	auth.set_access_token(access_key, access_secret) 

	# Calling api 
	api = tweepy.API(auth) 

	statuses =[]

	for tweets in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended", exclude_replies = True).items(5000):
		if not tweets.full_text.startswith('RT @'):
			statuses.append(tweets.full_text)


	columns = list()
	columns = ['name', 'tweet']
	data = dict()
	data = {
		'name' : username,
		'tweet' : [item for item in statuses]
	}
	targetSetDF = pd.DataFrame(data, columns = columns)
	targetSetDF.to_csv(username+'.csv', sep = ',', encoding = 'utf-8')

# Driver code 
if __name__ == '__main__': 

	# Let's call our function to execute the code. 
	get_tweets() 
