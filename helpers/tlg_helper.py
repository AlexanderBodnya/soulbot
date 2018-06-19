import requests
import json


class BotHelper:
    # Here we are initializang instance of our bot. It does nothing except stores bot token
    def __init__(self, token):
        self.token = token

    # This is serialized api request. It is separated from api methods because DNRY(do not repeat yourself)
    def api_request(self, method_name, payload={}):
        url = 'https://api.telegram.org/bot' + self.token + '/' + method_name
        # Here we are separating setWebhook method from other methods.
        # setWebhook requires multipart/form-data,
        # requests lib requires to use special parameter files to use the format
        if method_name == 'setWebhook':
            req = requests.post(url, files=payload)
        else:
            req = requests.post(url, data=payload)
        # Here we are trying to handle possible exceptions. It needs to be redesigned, however it works at the moment
        try:
            resp = req.json()
            return 0, resp
        except ValueError:
            return 10
        else:
            return 1

    # This is API method to set webhook. It doesn't have required options, however if you want it to work
    # you need to specify url(this is url on which Telegram will send messages), and path to cert file,
    # in case you are using self-signed certificate
    def setWebhook(self, url=None, cert=None, max_connections=None, allowed_updates=None, **kwargs):
        payload = {
            'url': (None, url)
        }
        # We are checking if parameters are passed and adding them to request
        if cert is not None:
            payload['certificate'] = (cert, open(cert, 'rb'))
        if max_connections is not None:
            payload['max_connections'] = (None, max_connections)
        if allowed_updates is not None:
            payload['allowed_updates'] = (None, allowed_updates)
        payload.update(kwargs)

        result = self.api_request('setWebhook', payload)
        return result

    # This is API method which deletes webhook. It doesn't require any parameters.
    def deleteWebhook(self):
        result = self.api_request('deleteWebhook')
        return result

    # This is API method which returns information about bot. It doesn't require any parameters
    def getMe(self):
        result = self.api_request('getMe')
        return result

    # This is API method which returns information about webhook. It doesn't require any parameters
    def getWebhookInfo(self):
        result = self.api_request('getWebhookInfo')
        return result

    # This is API method to send messages. It requires chat_id and text of the message
    def sendMessage(self, chat_id, text):
        payload = {
            'chat_id': chat_id,
            'text': text
        }
        result = self.api_request('sendMessage', payload)
        return result


class Messaging(BotHelper):

    def __init__(self, token, message):
        super(Messaging, self).__init__(token)
        self._json_message = json.loads(message.decode('utf-8'))
        self._chat_id = self._json_message['message']['chat']['id']

    def command_execute(self, command):
        commands = {
            'start': self.start_message,
            'get_chat_id': self.return_chat_id,
            'get_name': self.return_name,
            'get_id': self.return_user_id
        }
        result = commands[command]()
        return result
    # Deprecated, moved to instance initialization
    # def get_chat_id(self):
    #     chat_id = self._json_message['message']['chat']['id']
    #     return chat_id

    def get_name(self):
        name = self._json_message['message']['from']['username']
        return name

    def get_user_id(self):
        id = self._json_message['message']['from']['id']
        return id

    def get_text(self):
        text = self._json_message['message']['text']
        return text

    def get_command(self):
        words = self.get_text().split()
        if words[0][0] == '/':
            return words[1:]
        else:
            return None

    def start_message(self):
        self.sendMessage(self._chat_id, 'welcome message')

    def return_chat_id(self):
        self.sendMessage(self._chat_id, self._chat_id)

    def return_name(self):
        self.sendMessage(self._chat_id, self.get_name)

    def return_user_id(self):
        self.sendMessage(self._chat_id, self.get_user_id)
