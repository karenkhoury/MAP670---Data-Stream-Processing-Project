'''
Team members : 
        Karen KHOURY
        Abed EL Kader AL SHAAR
        Ahmed KHALIFE
'''

from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads, dumps
from datetime import datetime

'''
In this script, we monitor all the Kafka topics and print the status of each Kafka topic
in the console in real-time for monitoring purposes.
'''

consumer = KafkaConsumer(
    'raw-tweets', 'en-tweets', 'fr-tweets', 'positive-tweets', 'negative-tweets',
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: loads(m.decode("utf8")),
)

for tweet in consumer: 
    print("Topic: {}, Partition_id: {}, offset_id: {}, timestamp: {}".format(tweet.topic, tweet.partition, tweet.offset, datetime.now() ))
