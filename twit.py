import tweepy
import time
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

# Follow back
def follow_back():
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        follower.follow()

# Like/Retweet
def main(search_string, numberOfTweets):
    for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
        try:
            tweet.favorite()
            # tweet.retweet()
            print('Done!')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
if __name__ == '__main__':
    # Likes the first 10 tweets that contain the word Christmas
    main('Christmas', 10)
