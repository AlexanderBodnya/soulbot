import flask
import helpers.tlg_helper as tlg

app = flask.Flask(__name__)
bot = tlg.BotHelper(TOKEN)


@app.route('/soul_queue', methods=['POST'])
def push_message():
    print('GOT SOMETHING')
    message = flask.request.get_json()
    print(message)
    return 'OK'


if __name__ == '__main__':
    bot.deleteWebhook()
    result = bot.setWebhook('https://URL:PORT/soul_queue', '/path/to/public/cert')
    print(result)
    print(bot.getWebhookInfo())
    app.run(host='0.0.0.0', debug=True, ssl_context=('/path/to/public/cert', '/path/to/private/key'), port=PORT)
