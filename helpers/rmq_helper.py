import pika


# import helpers.log_helper

# TODO: log it!

# set connection and return channel
def connect():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    return connection.channel()


def set_queue(channel, queue_name):
    channel.queue_declare(queue=queue_name, durable=True)


def push_message(channel, message, queue_name):
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message,
                          # make message persistent
                          properties=pika.BasicProperties(delivery_mode=2, )
                          )
