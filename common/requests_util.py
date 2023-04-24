import requests
import json

class RequestsUtil:

    session = requests.session()

    def send_request(self, method, data, url, **kwargs):
        method = str(method).lower()
        data = json.dumps(data)

        rep = RequestsUtil.session.request(method, data=data, url=url, **kwargs)
        return rep