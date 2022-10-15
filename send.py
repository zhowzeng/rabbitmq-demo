import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here.
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='',  # default
    routing_key='hello',  # queue name
    body='Hello World!',
)
print(" [x] Sent 'Hello World!'")

connection.close()
