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
```
