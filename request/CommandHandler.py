import json

from request import Command


class RequesterHandler:

    def __init__(self):
        self.command = Command.Command()
        self.response = None

    def join(self, name):
        index = 0
        self.command.load_parameters("join", name)

        self.response = self.command.execute()
        if self.response is None:
            return self.join(name + str(index + 1))

        self.load_id()

        return name

    def load_id(self):
        action, value = self.get_info("userID")
        self.command.load_parameters(action, value)

    def get_info(self, key):
        convert_response = json.load(self.response)

        return key, convert_response[key]
