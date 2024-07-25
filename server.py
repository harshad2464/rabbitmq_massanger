import pika
import json
import ssl
import time
from datetime import datetime
from pymongo import MongoClient

# CONNECTION_STRING = "mongodb+srv://patilharshad:VgEyLG5StaSiFHLG@cluster.mongodb.net/rabbitmq_messages"
CONNECTION_STRING = "mongodb://localhost:27017/rabbitmq_messages"  

client = MongoClient(CONNECTION_STRING)

db = client["rabbitmq_messages"]

def process_function(msg):
  data = {
     "status":json.loads(msg)['status'],
     "time":str(datetime.now().time())
  }
  print(data)
  db.message.insert_one(data)
  time.sleep(1)
  return None

def server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.set_ciphers('ECDHE+AESGCM:!ECDSA')

    url = f"amqps://guest:guest@localhost/"

    parameters = pika.URLParameters(url)
    parameters.ssl_options = pika.SSLOptions(context=context)
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    channel = connection.channel()

    channel.basic_consume("random_values",callback,auto_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    process_function(body)

if __name__ == "__main__":
  server()