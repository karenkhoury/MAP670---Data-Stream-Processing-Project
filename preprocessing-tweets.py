'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
import time
import json
import re
import nltk
from kafka import KafkaConsumer
from kafka import KafkaProducer
from river import feature_extraction
from nltk.corpus import stopwords   
from nltk.stem import PorterStemmer

'''
In this script, we preprocess the tweets from 'classified-tweets' topic and write 
them into 'processed-tweets' topic.
'''
tfidf = feature_extraction.TFIDF()
producer = KafkaProducer(bootstrap_servers="localhost:9092")

## consumer topic
classified_tweets = "classified-tweets"
## producer topic
topic_name = "processed-tweets"

## consumer and producer objects
consumer = KafkaConsumer(classified_tweets, bootstrap_servers="localhost:9092")
producer = KafkaProducer(bootstrap_servers="localhost:9092")

## download stopwords
nltk.download('stopwords')
stop_words_en = set(stopwords.words('english'))
stop_words_fr = set(stopwords.words('french'))

## create stemmer object
ps = PorterStemmer()

for msg in consumer:
    msg = json.loads(msg.value.decode('utf-8'))
  
    p=msg['text']
    # Remove URLs       
    msg['text'] = re.sub(r"http\S+", "", msg['text'])

    # Remove mentions
    msg['text'] = re.sub(r"@\S+", "", msg['text'])

    # Remove hashtags
    msg['text'] = re.sub(r"#\S+", "", msg['text'])

    # Remove RT and FAV         
    msg['text'] = re.sub(r"RT|FAV", "", msg['text'])

    # Remove punctuations
    msg['text'] = re.sub(r"[^\w\s]", "", msg['text'])

    # Remove numbers
    msg['text'] = re.sub(r"\d+", "", msg['text'])

    # Remove whitespaces
    msg['text'] = re.sub(r"\s+", " ", msg['text'])

    # Remove emojis
    msg['text'] = re.sub(r"[^\x00-\x7F]+", "", msg['text'])
    
    # Convert to lowercase
    msg['text'] = msg['text'].lower()

    # Remove stopwords
    if msg['lang'] == 'en':
        msg['text'] = ' '.join([word for word in msg['text'].split() if word not in stop_words_en])
    elif msg['lang'] == 'fr':
        msg['text'] = ' '.join([word for word in msg['text'].split() if word not in stop_words_fr])
    
    # Remove short words
    msg['text'] = ' '.join([word for word in msg['text'].split() if len(word) > 2])

    # Remove words with numbers
    msg['text'] = ' '.join([word for word in msg['text'].split() if not any(c.isdigit() for c in word)])

    # Remove words with special characters
    msg['text'] = ' '.join([word for word in msg['text'].split() if not any(c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+" for c in word)])

    # Represent the tweet as a bag of words
    msg['text'] = msg['text'].split()

    # Stemming
    msg['text'] = [ps.stem(word) for word in msg['text']]
    msg['text'] = ' '.join(msg['text'])
    c=msg['text']
    
    # Learn the vocabulary
    tfidf = tfidf.learn_one(msg['text'])
    msg['tfidf'] = (tfidf.transform_one(msg['text']))
    
    # Send the tweet to the topic
    producer.send(topic_name, json.dumps(msg).encode('utf-8'))
    
    time.sleep(1)

