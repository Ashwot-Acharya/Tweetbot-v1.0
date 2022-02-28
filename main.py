from secrets import *
import tweepy, json, os , requests , random
myfile = "mytweets.txt"
Myuser_mentions = "user_mentions.txt"
URL ="https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw&format=txt"
respose =  requests.get(url= URL )
joke = respose.text + """
#programming #bot #myproject #funny #java #javascript #python"""


def make_tweet(what_to_tweet):
    my_tweets_from_app = open(myfile,"a")
    my_tweets_from_app.write(joke)
    my_tweets_from_app.close()
    
    try :
        client = tweepy.Client(B_token)
        client.access_token = A_TOKEN
        client.access_token_secret= A_TOKEN_SECRET
        client.consumer_key= C_KEY
        client.consumer_secret=C_SECRET
        client.create_tweet(text=what_to_tweet)   
    except Exception as E :
        print(E)
# def reply_tweets():
#     try:
#         client = tweepy.Client(B_token)
#         client.access_token = A_TOKEN
#         client.access_token_secret= A_TOKEN_SECRET
#         client.consumer_key= C_KEY
#         client.consumer_secret=C_SECRET
#         Mymentions = client.get_users_mentions(id="1255125948908912643")
#         add_to_file = open(Myuser_mentions,"a")
#         add_to_file.close()
#         open_reply= open(Myuser_mentions,"r")
  
#     except Exception as E :
#         print(E)
make_tweet(joke)
