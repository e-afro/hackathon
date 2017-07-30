from request import Command


class StrategyD0:

    def __init__(self, bot=None):
        self.command = Command.Command()

    def play(self):
        return False

