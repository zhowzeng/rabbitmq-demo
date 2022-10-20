import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# An exchange is a very simple thing. On one side it receives messages from producers and on the other side it pushes
# them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a
# particular queue? Should it be appended to many queues? Or should it get discarded.
channel.exchange_declare(exchange='logs', exchange_type='fanout')  # type: direct, topic, headers, fanout

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
