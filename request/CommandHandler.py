import Command
import Response


class RequesterHandler:

    def __init__(self):
        self.command = Command.Command()
        self.response = Response.Response()

    def execute(self, action, value):
        self.command.load_parameters(action, value)
        self.response.response = self.command.execute()

    def join(self, name):
        index = 0
        self.execute("join", name)

        if self.response.response is None:
            return self.join(name + str(index + 1))

        self.load_id()

        return name

    def load_id(self):
        key = "userID"
        value = self.response[key]
        self.command.load_parameters(key, value)

    def play_card(self, card):
        self.execute("playCard", card)

    def select_row(self, row):
        self.execute("selectRow", row)

    def get_cards(self):
        self.execute("getCards")