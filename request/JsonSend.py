class JsonSend:

    def __init__(self):
        self._auth_data = dict()
        self._action_data = dict()
        self.data = dict()

    def _get_auth_data(self):
        return dict(self._auth_data)

    def _set_auth_data(self, auth_data):
        self._auth_data = auth_data
        self.data = auth_data

    def _get_action_data(self):
        return dict(self._action_data)

    def _set_action_data(self, action_data):
        self._action_data = action_data
        self.data = sum_dictionary(self._auth_data, self._action_data)

    connection_data = property(_get_action_data, _set_action_data)
    action_data = property(_get_action_data, _set_action_data)


def sum_dictionary(dict1, dict2):
    dict_sum = dict()
    for key, value in dict2.items() + dict1.items():
        dict_sum[key] = value

    return dict_sum
