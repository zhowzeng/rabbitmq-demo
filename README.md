# rabbitmq-demo

Follow this [tutorial](https://www.rabbitmq.com/getstarted.html).

## rabbitmq server

```bash
# pull image
docker pull rabbitmq
# run server (standard port: 5672)
docker run -d --hostname my-rabbit --name some-rabbit --net host rabbitmq
```

## pika installation

Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.

See [introduction to pika](https://pika.readthedocs.io/en/stable/intro.html).

```bash
# virtual environment
python3 -m venv .venv
source .venv/bin/activate
# install
pip install pika --upgrade
```

## commands

```bash
# see what queues RabbitMQ has and how many messages are in them
rabbitmqctl list_queues

# It's a common mistake to miss the basic_ack. It's an easy error, but the consequences are serious. Messages will be
# redelivered when your client quits (which may look like random redelivery), but RabbitMQ will eat more and more
# memory as it won't be able to release any unacked messages.
rabbitmqctl list_queues name messages_ready messages_unacknowledged

# In this list there will be some amq.* exchanges and the default (unnamed) exchange. These are created by default.
rabbitmqctl list_exchanges

# list bindings
rabbitmqctl list_bindings
```
