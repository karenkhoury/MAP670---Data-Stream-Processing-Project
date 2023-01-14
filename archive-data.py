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
In this script, we store the data from the 'positive-tweets' and 'negative-tweets' topics into 
an 'archive.txt' file for batch modeling.
'''
## consumer topics
classified_tweets = "classified-tweets"

## create consumer objects
consumer = KafkaConsumer(classified_tweets, bootstrap_servers="localhost:9092")

string_pos = []
string_neg = []

## open file archive.txt in append mode 
file = open('archive.txt', 'a')    

## store the data from the topics into the file
def write():
        for msg in consumer:
            #id=id+1
            msg = json.loads(msg.value.decode('utf-8'))
            print(str(msg['text'])+";"+ str(msg['sentiment'])+"\n")

            file.write(str(msg['text'])+";"+ str(msg['sentiment'])+"\n")


write()
