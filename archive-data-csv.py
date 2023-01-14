'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
import time
import json
from kafka import KafkaConsumer
from threading import Thread
import csv

'''
In this script, we store the data from the 'processed-tweets' topic into 
an 'archive.txt' file for batch modeling.
'''
## consumer topics
processed_tweets = "processed-tweets"

## create consumer objects
consumer = KafkaConsumer(processed_tweets, bootstrap_servers="localhost:9092")

## open file archive.csv in append mode 
file = open('archive.csv', 'a')    
writer = csv.writer(file, delimiter=';')
writer.writerow(["Tweet", 'Language','Sentiment'])

## store the data from the topics into the file
def write():
        for msg in consumer:
            #id=id+1
            msg = json.loads(msg.value.decode('utf-8'))
            print([msg['text'], msg['lang'], msg['sentiment']])
            writer.writerow([msg['text'], msg['lang'], msg['sentiment']])


write()
