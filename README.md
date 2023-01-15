# MAP670 - Data Stream Processing Project 

## Authors

EL SHAAR Abed EL Kader, KHALIFE Ahmed and KHOURY Karen

## Description

The project aims to collect tweets from Twitter API  in real-time and use a batch or online classification method to classify them for sentiment analysis.
Twitter introduced a new API (API V2/ Essential Access) which gives access to the stream Tweets right away without validation. Getting Started with the Twitter API | Docs | Twitter Developer Platform: https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level

## Getting Started


### Executing the project
> **Warning**
> Each script must be run in a different terminal window

- Clone the repository with: `git clone https://github.com/karenkhoury/MAP670---Data-Stream-Processing-Project`
- Install requirements with: `pip install -r requirements.txt`
- Start Zookeeper server in Apache Kafka with: `bin/zookeeper-server-start.sh config/zookeeper.properties`
- Start Kafka server with: `bin/kafka-server-start.sh config/server.properties`
- Run the `ingest-tweets.py` script to stream the tweets
- Run the `filter-tweets.py` script to filter the tweets into french and english tweets
- Run the `sentiment-tweets.py` script to label the tweets into positive and negative tweets
- Run the `preprocessing-tweets.py` script to preprocess the tweets for online modeling
- Run the `logreg-tweets.py` script to classify the tweets into positive and negative tweets using LogisticRegression classifier from river 
- Run the `naivebayes-tweets.py` script to classify the tweets into positive and negative tweets using GaussianNB classifier from river  
- Run the `rf-tweets.py` script to classify the tweets into positive and negative tweets using AdaptiveRandomForestClassifier classifier from river
- Run the `batchmodels-tweets.py` script to classify the tweets into positive and negative tweets using the LogisticRegression, GaussianNB and RandomForestClassifier classifiers from sklearn
- Run the `monitor-kafka.py` script to monitor all the Kafka topics
