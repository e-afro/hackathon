from request import CommandHandler


class StrategyD0:

    def __init__(self, bot=None):
        self.command_handler = CommandHandler.CommandHandler()
        bot.name = self.command_handler.join(bot.name)

    def play(self):
        return False

