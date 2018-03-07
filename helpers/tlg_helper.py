import requests


class BotHelper:

    def __init__(self, token):
        self.token = token

    def api_request(self, method_name, payload={}):
        url = 'https://api.telegram.org/bot' + self.token + '/' + method_name
        req = requests.post(url, data=payload)
        try:
            resp = req.json()
            return 0, resp
        except ValueError:
            return 10
        else:
            return 1

    def setWebhook(self, url=None, cert=None, max_connections=None, allowed_updates=None, **kwargs):
        payload = {}

        if url is not None:
            payload['url'] = url
        if cert is not None:
            payload['certificate'] = open(cert, 'rb')
        if max_connections is not None:
            payload['max_connections'] = max_connections
        if allowed_updates is not None:
            payload['allowed_updates'] = allowed_updates
        payload.update(kwargs)


        print(payload)
        result = self.api_request('setWebhook', payload)
        return result

    def deleteWebhook(self):
        result = self.api_request('deleteWebhook')
        return result

    def getMe(self):
        result = self.api_request('getMe')
        return result

    def getWebhookInfo(self):
        result = self.api_request('getWebhookInfo')
        return result