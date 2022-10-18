import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(
    queue='task_queue',
    durable=True,  # To make sure that the queue will survive a RabbitMQ node restart, we need to declare it as durable
)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ),  # mark messages as persistent
)
print(" [x] Sent %r" % message)
connection.close()
