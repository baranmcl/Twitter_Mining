import tweepy
#make sure you have tweepy module installed

#enter these for the code to work. Don't share your key and secret publicly!
consumer_key =
consumer_secret =
access_token =
access_token_secret =

#OAuth goodness
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#prints most recent 10 tweets on your timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text