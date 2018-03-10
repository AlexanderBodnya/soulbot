import pika


# import helpers.log_helper

# TODO: log it!
# function to quick queue set up
def start_queue(queue_name):
    channel = connect()
    set_queue(channel, queue_name)
    return channel


# set connection and return channel
def connect():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    print('Returning connection channel')
    return connection.channel()


def set_queue(channel, queue_name):
    print('Declare queue ',  queue_name)
    channel.queue_declare(queue=queue_name, durable=True)


def push_message(channel, queue_name, message):
    print('Pushing message to queue', queue_name)
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message,
                          # make message persistent
                          properties=pika.BasicProperties(delivery_mode=2, )
                          )
    channel.close()


