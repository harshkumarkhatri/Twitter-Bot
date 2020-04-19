import tweepy
import time

auth=tweepy.OAuthHandler('fPsvbg9HM858Fdm9ta9foO975','qz2r1VxaVHbkgEXqmLsXJ9rXLUzwxtb5MLHDHuEYjbm0nm980I')

auth.set_access_token('753755517059817473-qxRJWMBXUefLPInsvlT4YXZvqnVflmt','qTJbC5PuAJV7uhlFYqNZJIzUphrrum9j7UwrTW6ZOowPN')

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()

# Printing our username
# print(user.screen_name)

# Printing my all followers
# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

search='python'
numTweets=500

for tweet in tweepy.Cursor(api.search,search).items(numTweets):
    try:
        print('Tweet Liked')
        # Liking a tweet with a specific search keyword in it
        tweet.favorite()
        print('done')
        # retweeting a tweet with a specific keyword in it
        tweet.retweet()
        print('Tweet retweeted')
        time.sleep(90)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break