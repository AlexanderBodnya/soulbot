import flask
import helpers.tlg_helper as tlg
import configs.config as conf

app = flask.Flask(__name__)
bot = tlg.BotHelper(conf.TOKEN)


@app.route('/soul_queue', methods=['POST'])
def push_message():
    print('GOT SOMETHING')
    message = flask.request.get_json()
    print(message)
    return 'OK'


if __name__ == '__main__':
    bot.deleteWebhook()
    result = bot.setWebhook('https://'+conf.URL+':'+conf.PORT+'/soul_queue', conf.CERT)
    print(result)
    print(bot.getWebhookInfo())
    app.run(host='0.0.0.0', debug=True, ssl_context=(conf.CERT, conf.KEY), port=conf.PORT)
