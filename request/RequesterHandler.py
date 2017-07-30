import json

from request import Command


class RequesterHandler:

    def __init__(self):
        self.command = Command.Command()

    def join(self, name):
        index = 0
        self.command.load_parameters("join", name)

        response = self.command.execute()
        if response is None:
            return self.join(name + str(index + 1))

        self.load_id(response)

        return name

    def load_id(self, response):
        action, value = get_info(response, "userID")
        self.command.load_parameters(action, value)


def get_info(response, key):
    convert_response = json.load(response)

    return key, convert_response[key]
