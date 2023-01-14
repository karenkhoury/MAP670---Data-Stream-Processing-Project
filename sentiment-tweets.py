'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import time
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
'''
In this script, we add a 'sentiment' label to the tweets from 'en-tweets' and 'fr-tweets' topics
using the nltk library  .
'''
nltk.download('vader_lexicon')

def sentiment_analyzer_scores(sentence):
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score['compound']
## consumer topics
en_tweets = "en-tweets"
fr_tweets = "fr-tweets"

## create producer and consumer objects
producer = KafkaProducer(bootstrap_servers="localhost:9092")
consumer_eng = KafkaConsumer(en_tweets, bootstrap_servers="localhost:9092")
consumer_fr = KafkaConsumer(fr_tweets, bootstrap_servers="localhost:9092")

def english():

    for msg in consumer_eng:
        msg = json.loads(msg.value.decode('utf-8'))
        if sentiment_analyzer_scores(msg['text'])>=0.5:
            # Positive tweets
            msg['sentiment'] = 1
            producer.send("positive-tweets", json.dumps(msg).encode('utf-8'))
            producer.send("classified-tweets", json.dumps(msg).encode('utf-8'))
            print("Sending message {} to topic: {}".format(msg, "positive-tweets"))
        elif sentiment_analyzer_scores(msg['text'])<0.5:
            # Negative tweets
            msg['sentiment'] = 0
            producer.send("negative-tweets", json.dumps(msg).encode('utf-8'))
            producer.send("classified-tweets", json.dumps(msg).encode('utf-8'))
            print("Sending message {} to topic: {}".format(msg, "negative-tweets"))
  
        time.sleep(1)

def french():

    for msg in consumer_fr:
        msg = json.loads(msg.value.decode('utf-8'))
        if sentiment_analyzer_scores(msg['text'])>=0.5:
            # Positive tweets
            msg['sentiment'] = 1
            producer.send("positive-tweets", json.dumps(msg).encode('utf-8'))
            producer.send("classified-tweets", json.dumps(msg).encode('utf-8'))
            print("Sending message {} to topic: {}".format(msg, "positive-tweets"))
        elif sentiment_analyzer_scores(msg['text'])<0.5:
            # Negative tweets
            msg['sentiment'] = 0
            producer.send("negative-tweets", json.dumps(msg).encode('utf-8'))
            producer.send("classified-tweets", json.dumps(msg).encode('utf-8'))
            print("Sending message {} to topic: {}".format(msg, "negative-tweets"))
  
        time.sleep(1)

from threading import Thread
t1 = Thread(target=english)
t2 = Thread(target=french)
t1.start()
t2.start()
