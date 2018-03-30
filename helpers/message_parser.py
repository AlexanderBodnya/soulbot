import json


class MessageParser:
    def __init__(self, message):
        self._json_message = json.loads(message.decode('utf-8'))

    def get_chat_id(self):
        chat_id = self._json_message['message']['chat']['id']
        return chat_id

    def get_text(self):
        text = self._json_message['message']['text']
        return text

    def get_command(self):
        words = self.get_text().spilt()
        if words[0] == '/start':
            return 'start'
        else:
            return 0

