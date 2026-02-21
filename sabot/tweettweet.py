import tweepy

consumer_key = 'LKVQ52M06tLb4BhHhTi3HGGwE'
consumer_secret = 'AHVEpjM0C2v6bmljqTYs75C8BdY2kG9dxw5jSq5tuJAMh7E6Yw'
access_token = '1799820518456967168-IRk8JsY9kwtKK3RaKyVqZHcc0PiVA8'
access_token_secret = 'il931C6Q9mWEiRBQulyC7OrxIImVu2y9RCbO1htiHSRKE'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIsJ7wEAAAAACGyJDd%2B%2BkgWkPk%2B5eloOSCJvB%2Bg%3Dh3LVVYyY886B1B9gqow1m6d1M92ttFv005YFounoiWaP47F1Dy"

client = tweepy.Client(bearer_token=bearer_token)

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret, access_token, access_token_secret
# )

# api = tweepy.Client(auth)

public_tweets = client.get_home_timeline()
for tweet in public_tweets:
    print(tweet.text)
