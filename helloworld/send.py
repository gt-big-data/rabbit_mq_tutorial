import pika
import sys

# First establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
# We're now connected to a broker on the local machine. If you wanted a to
# connect to a different broker simply pass in the address as the host parameter.

# create the queue to which the message will be delivered.
channel.queue_declare(queue='hello')


# a message can never be sent directly to the queue, it always needs to go
# through an exchange. Here we use the default exchange identified by the
# empty string. We also specify the queue name using the routing_key parameter.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello world!')

print(" [x] Sent 'Hello World!'")
connection.close()