import tweepy
#make sure you have tweepy installed

#enter these for the code to work
consumer_key =
consumer_secret =
access_token =
access_token_secret =

#OAuth goodness
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#print @RZA’s most recent 10 tweets
public_timeline = api.user_timeline(29663668)
for tweet in public_timeline:
    print tweet.text