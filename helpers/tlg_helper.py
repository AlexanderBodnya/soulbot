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

    def setWebhook(self, wh_url, cert):
        payload = {
            'url': wh_url,
            'cert': open(cert, 'r')
        }
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


