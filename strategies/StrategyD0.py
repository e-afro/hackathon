from request import CommandHandler
from elements import Status


class StrategyD0:

    def __init__(self, bot):
        self.command_handler = CommandHandler.CommandHandler()
        bot.name = self.command_handler.join(bot.name)
        self.status = Status.Status()

    def play_card(self):
        None

    def select_row(self):
        None
