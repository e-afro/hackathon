from strategies import StrategyD0
from game import State
from request import CommandHandler


class Bot:

    DEFAULT_STRATEGY = StrategyD0.StrategyD0

    def __init__(self, name='bot', strategy=None):
        self.command_handler = CommandHandler.CommandHandler()
        self.name = self.command_handler.join(name)
        self.state = State.State()
        self.strategy = strategy(self) if strategy else self.build_strategy()

    def build_strategy(self):
        return self.DEFAULT_STRATEGY(self)

    def load(self, response):
        self.command_handler.get_status()
        self.state.load(self.name, response)
        self.strategy.status.load(response)

        self.load_cards()

    def load_cards(self):
        self.command_handler.get_cards()
        self.strategy.status.load(self.command_handler.response)

    def load_card_values(self):
        self.command_handler.get_card_values()
        self.strategy.status.load(self.command_handler.response)

    def play(self):
        if self.state.can_get_card_values():
            self.load_card_values()
        self.load(self.command_handler.response)

        if self.state.can_play_card():
            card = self.strategy.play_card()
            self.command_handler.play_card(card)

        if self.state.can_select_row():
            row = self.strategy.select_row()
            self.command_handler.select_row(row)

