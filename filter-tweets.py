'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
import time
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
'''
In this script, we filter the tweets from the 'raw-tweets' topic into 'en-tweets' and 'fr-tweets' topics 
according to the tweets language.
'''
## consumer topic
topic_name = "raw-tweets"
## producer topics
en_tweets = "en-tweets"
fr_tweets = "fr-tweets"

## create producer and consumer objects
producer = KafkaProducer(bootstrap_servers="localhost:9092")
consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092")

## filter the tweets according to the language
for msg in consumer:
    msg = json.loads(msg.value.decode('utf-8'))
    if msg['lang'] == 'en':
        producer.send(en_tweets, json.dumps(msg).encode('utf-8'))
        print("Sending message {} to topic: {}".format(msg, en_tweets))
    elif msg['lang'] == 'fr':
        producer.send(fr_tweets, json.dumps(msg).encode('utf-8'))
        print("Sending message {} to topic: {}".format(msg, fr_tweets))
    time.sleep(1)