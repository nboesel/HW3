# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy

# Unique code from Twitter
import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "2155414722-RU2WHLoT0IhljfeOzVWeeAak2yIot5S54RvPnLe"
access_token_secret = "RWftU91xIZBR2ZmbzTbWuZ6OMOcwvtxCTCJI00VCBeazM"
consumer_key = "NL5BZbHPXrkUU5bAUhU2MijrX"
consumer_secret = "iUUZVzhzt8UqXjw5mkuLNZ6nzf0ymlvEFkZBsuNfNAML8H4V0x"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('GSW')

s = 0
p = 0
c = 0
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	s = s + analysis.subjectivity 
	p = p + analysis.polarity
	c = c +1

print("Average subjectivity is" + str(s/c))
print("Average polarity is" + str(p/c))
