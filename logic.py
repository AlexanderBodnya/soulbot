#!/usr/bin/env python

import helpers.rmq_helper as q_helper


# TODO: log it!


def on_message(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # log.log_message(4, "Received %r" % body)


queue = 'bot_inbox'

if __name__ == '__main__':
    queue_channel = q_helper.start_queue(queue)
    # TODO: implement message acknowledgment
    queue_channel.basic_consume(on_message,
                                queue=queue,
                                no_ack=True)

    queue_channel.start_consuming()
