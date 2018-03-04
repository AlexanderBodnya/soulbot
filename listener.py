#!/usr/bin/env python

from flask import Flask, request
import telegram
import helpers.rmq_helper as q_helper
import config

app = Flask(__name__)

# create and configure bot object
bot = telegram.Bot(token=config.bot_token)

global channel
# TODO: move queue name to config
queue = 'bot_inbox'


def set_webhook(bot):

    bot.set_webhook(url=config.webhook_url_base + config.webhook_url_path, certificate=open(config.webhook_ssl_cert, 'r'))


@app.route('/soul_queue')
def push_message():
    # TODO: implement correct connection closing
    # TODO: parse real telegram message and push to queue
    message = 'lorem ipsum'
    q_helper.push_message(channel, message, queue)


if __name__ == '__main__':
    set_webhook(bot)
    channel = q_helper.connect()
    q_helper.set_queue(channel, queue)

    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)






