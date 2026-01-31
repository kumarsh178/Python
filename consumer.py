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