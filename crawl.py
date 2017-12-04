import tweepy
import os
import requests
from tqdm import tqdm


def print_timeline():
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    tweets = api.search("画像")
    for tweet in tqdm(tweets):
        if 'media' in tweet.entities:
            for media in tweet.entities['media']:
                media_url = media['media_url']
                filename = f"images/{media_url.split('/')[-1]}"
                with open(filename, 'wb') as fp:
                    img_data = requests.get(media_url).content
                    fp.write(img_data)


if __name__ == '__main__':
    print_timeline()
