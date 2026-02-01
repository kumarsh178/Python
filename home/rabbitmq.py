import pika
import random
import json

def publish_message(message):
    params = pika.URLParameters('amqps://aejmfnqu:HccPmvPesq3IomDb5ow_jnxqyfjlifyG@beaver.rmq.cloudamqp.com/aejmfnqu')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")
    message = json.dumps(message)
    channel.basic_publish(
        exchange='',
        routing_key="my_queue",
        body=message
    )
    print(f"Message published")
    connection.close()

def publish_message_bylocal_rabbitmq(message):
    credentials  = pika.PlainCredentials('guest', 'guest')
    connection_params = pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/',
        credentials=credentials
    )
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue="test_queue")
    message = json.dumps(message)
    channel.basic_publish(
        exchange='',
        routing_key="test_queue",
        body=message
    )
    print(f"Message by local published")
    connection.close()