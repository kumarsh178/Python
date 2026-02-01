import pika
import pandas as pd
import json
import uuid

def generateExcel(message):
    message = json.loads(message)
    df = pd.DataFrame(message)
    df.to_excel(f"output_{uuid.uuid4()}.xlsx", index=False)

def callback(ch, method, properties, body):
    message = body.decode()
    generateExcel(message)
def callbackByLocal(ch, method, properties, body):
    message = body.decode()
    generateExcel(message)
# By param
"""
params = pika.URLParameters('amqps://aejmfnqu:HccPmvPesq3IomDb5ow_jnxqyfjlifyG@beaver.rmq.cloudamqp.com/aejmfnqu')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="my_queue")
channel.basic_consume(
    queue="my_queue",
    on_message_callback=callback,
    auto_ack=True
)
print("Consumer Started")
channel.start_consuming()
"""
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
channel.basic_consume(
    queue="test_queue",
    on_message_callback=callbackByLocal,
    auto_ack=True
)
print("Consumer Started")
channel.start_consuming()