import flask
import json
import helpers.tlg_helper as tlg
import configs.config as conf
import helpers.rmq_helper as q_helper

app = flask.Flask(__name__)
bot = tlg.BotHelper(conf.TOKEN)

global channel
queue = 'bot_inbox'


@app.route('/soul_queue', methods=['POST'])
def push_message():
    print('GOT SOMETHING')
    message = flask.request.get_json()
    queue_handler.push_message(json.dumps(message))
    return 'OK'


if __name__ == '__main__':
    bot.deleteWebhook()
    result = bot.setWebhook('https://' + conf.URL + ':' + str(conf.PORT) + '/soul_queue', conf.CERT)
    print(result)
    print(bot.getWebhookInfo())
    queue_handler = q_helper.QueueHelper(conf.QUEUE_NAME)
    app.run(host='0.0.0.0', debug=False, ssl_context=(conf.CERT, conf.KEY), port=conf.PORT)
