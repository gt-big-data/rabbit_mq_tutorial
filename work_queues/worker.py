import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    # Tell RabbitMQ that a particular message had been received, processed and
    # that RabbitMQ is free to delete it.
    ch.basic_ack(delivery_tag = method.delivery_tag)

# This tells RabbitMQ not to give more than one message to a worker at a time.

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()