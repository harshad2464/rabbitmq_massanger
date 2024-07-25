import random
import pika
import ssl
import time
import json

def client():
    content = {
    "status":str(random.randint(0, 6))
    }    
    message =json.dumps(content)

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.set_ciphers('ECDHE+AESGCM:!ECDSA')

    url = f"amqps://guest:guest@localhost/"

    parameters = pika.URLParameters(url)
    parameters.ssl_options = pika.SSLOptions(context=context)
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    channel = connection.channel()

    channel.basic_publish(exchange='', routing_key="random_values", body=message)

if __name__ == "__main__":
    while True:
        time.sleep(1)
        client()