import json


class Response:

    def __init__(self, response=None):
        self._response = response

    def _get_response(self):
        return dict(self._response)

    def _set_response(self, response):
        if response is not None:
            self._response = json.load(response)
        else:
            self.response = None

    response = property(_get_response, _set_response)

    def __getitem__(self, key):
        try:
            value = self.response[key]
        except KeyError:
            return None

        return value
