'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
## API KEY: "gnE6FdGoUlgw2xsQF18iN9CYz"
## API SECRET KEY:  "OxXslfK55sTVFNNAeU3xtUXDeX0fx8tONI7U0w6P1xxZ3JuEF8"
## Bearer_Token: "AAAAAAAAAAAAAAAAAAAAAHZ4kgEAAAAAI7WD%2F0TnflpHdfjBG%2F1HFEO8Vdc%3D6tnhzQbhbvWCu2SjaFjjBkwp94aeGyRGpytRNud7fBAY7IraOA"
## access_token: "330898964-Ep8tcWUxwUgO0V8VnVfBgvDWimYLCgN8GLqSQCEE"
## access_token_secret: "t0FEfRuQL61lzNAL8Ma81LZGIzHxckUXbiWCZ2mbnHyNe"
import tweepy
import json
import time
from kafka import KafkaProducer
'''
In this script, we filter the tweets from the 'raw-tweets' topic into 'en-tweets' and 'fr-tweets' topics 
according to the tweets language.
'''
producer = KafkaProducer(bootstrap_servers="localhost:9092")
topic_name = "raw-tweets"

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAHZ4kgEAAAAAI7WD%2F0TnflpHdfjBG%2F1HFEO8Vdc%3D6tnhzQbhbvWCu2SjaFjjBkwp94aeGyRGpytRNud7fBAY7IraOA")
## search for tweets
query = 'messi'
x = {"text": '', "created_at": '', "lang": '', "possibly_sensitive": '' }

# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=[ 'created_at', 'lang', 'possibly_sensitive', 'context_annotations'], max_results=20).flatten(limit=1000):
    x['text']=tweet['text']
    x['lang']=tweet['lang']
    x['possibly_sensitive']=(tweet['possibly_sensitive'])
    x['created_at']=str(tweet['created_at'])
    x['context_annotations']=(tweet['context_annotations'])
    msgs = json.dumps(x)    
    producer.send(topic_name, msgs.encode('utf-8')) 
    print("Sending message {} to topic: {}".format(msgs, topic_name))
    time.sleep(1)
