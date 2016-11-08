# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

from TwitterAPI import TwitterAPI

access_token = "2155414722-RU2WHLoT0IhljfeOzVWeeAak2yIot5S54RvPnLe"
access_token_secret = "RWftU91xIZBR2ZmbzTbWuZ6OMOcwvtxCTCJI00VCBeazM"
consumer_key = "NL5BZbHPXrkUU5bAUhU2MijrX"
consumer_secret = "iUUZVzhzt8UqXjw5mkuLNZ6nzf0ymlvEFkZBsuNfNAML8H4V0x"

API = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
file = open('michigan.jpg', 'rb')
data = file.read()
tweet = API.request('statuses/update_with_media', {'status':'#UMSI206 #Project3'}, {'media[]':data})
print (tweet.status_code)

