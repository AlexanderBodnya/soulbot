#!/usr/bin/env python

import helpers.rmq_helper as q_helper
# TODO: log it!


def on_message(ch, method, properties, body):
    log.log_message(4, "Received %r" % body)


queue = 'bot_inbox'

if __name__ == '__main__':
    channel = q_helper.connect()
    q_helper.set_queue(channel, queue)
    # TODO: implement message acknowledgment
    channel.basic_consume(on_message,
                          queue=queue,
                          no_ack=True)

    channel.start_consuming()
