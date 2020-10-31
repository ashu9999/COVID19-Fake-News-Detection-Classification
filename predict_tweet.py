import private
import re
import tweepy
import pandas as pd
import numpy as np
import pickle
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

auth = tweepy.OAuthHandler(private.CONSUMER_KEY, private.CONSUMER_SECRET)
auth.set_access_token(private.OAUTH_TOKEN, private.OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

vec = pickle.load(open("vector.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))
 

#tweet_id = "http://twitter.com/anyuser/status/1280224654406430720"

def predict(tweet_id):
    
    if( tweet_id.split("/")[0] == 'http:' or tweet_id.split("/")[0] == 'https:'):
        tweet_id = int(tweet_id.split("/")[-1])

    tweet = api.get_status(tweet_id)
    tweet_text  = tweet.text
    # print(tweet_text)

    tweet_text = re.sub('[^a-zA-Z]', ' ', tweet_text)
    tweet_text = tweet_text.lower()
    tweet_text = tweet_text.split()
    lem = WordNetLemmatizer()    
    tweet_text = [lem.lemmatize(word) for word in tweet_text if not word in stopwords.words('english')]
    tweet_text = ' '.join(tweet_text)

    # print(tweet_text)


    tweet_vector = vec.transform([tweet_text]).toarray()
    # print(tweet_vector)

    result = model.predict(np.array(tweet_vector))

    if(result=='FAKE'):
        return 2
    else:        
        return 1










