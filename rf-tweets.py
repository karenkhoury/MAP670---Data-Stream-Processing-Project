'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
import json
from river import ensemble
from river import metrics

from kafka import KafkaConsumer
from kafka import KafkaProducer
'''
In this script, we predict the sentiment of the tweets from the 'processed-tweets' using the
AdaptiveRandomForestClassifier model from river.
'''
## consumer topic
topic_name = "processed-tweets"
## consumer and producer objects
consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092")
producer = KafkaProducer(bootstrap_servers="localhost:9092")

## AdaptiveRandomForestClassifier model
model = ensemble.AdaptiveRandomForestClassifier(n_models = 100, seed=8, leaf_prediction="mc")

## evaluation metrics
metric = metrics.ClassificationReport()+metrics.CohenKappa()+metrics.Precision()+metrics.F1()

for msg in consumer:
    ## load the msg 
    msg = json.loads(msg.value.decode('utf-8'))
    ## extract the features and the label
    x = msg["tfidf"]
    y = msg["sentiment"]
    
    ## predict the label
    y_pred = model.predict_one(x)
    ## update the model
    model.learn_one(x, y)

    ## update the metrics
    if y_pred is not None:
            metric.update(float(y), y_pred)

    print(metric)