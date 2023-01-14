'''
Team members : 
        Karen KHOURY
        Abed EL Kader EL SHAAR
        Ahmed KHALIFE
'''
from river import linear_model
import json
from river import optim
from river import metrics
from river import linear_model
from sklearn import model_selection
from kafka import KafkaConsumer
from kafka import KafkaProducer
'''
In this script, we predict the sentiment of the tweets from the 'processed-tweets' using the
LogisticRegression model from river.
'''
## consumer topic
topic_name = "processed-tweets"
## consumer and producer objects
consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092")
producer = KafkaProducer(bootstrap_servers="localhost:9092")

## Logistic Regression model
model = linear_model.LogisticRegression(optimizer=optim.SGD(.1))
## evaluation metrics
metric = metrics.ClassificationReport()+metrics.CohenKappa()+metrics.Precision()+metrics.F1()

for msg in consumer:
    ## load the msg as a json object
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