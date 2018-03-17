#!/usr/bin/env python

import helpers.rmq_helper as q_helper
import configs.config as conf
import helpers.tlg_helper as tlg
import json


# TODO: log it!
bot = tlg.BotHelper(conf.TOKEN)


def on_message(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # log.log_message(4, "Received %r" % body)
    _json_message = json.loads(body.decode('utf-8'))
    text = _json_message['message']['text']
    chat_id = _json_message['message']['chat']['id']
    result = bot.sendMessage(chat_id, text)
    return result


queue = 'bot_inbox'

if __name__ == '__main__':
    queue_channel = q_helper.start_queue(queue)
    # TODO: implement message acknowledgment
    queue_channel.basic_consume(on_message,
                                queue=queue,
                                no_ack=True)
    queue_channel.start_consuming()
