from strategies import StrategyD0
from elements import State


class Bot:

    DEFAULT_STRATEGY = StrategyD0.StrategyD0

    def __init__(self, strategy=None):
        self.name = ''
        self.state = State.State()
        self.strategy = strategy(self) if strategy else self.build_strategy()

    def build_strategy(self):
        return self.DEFAULT_STRATEGY(self)

    def play(self):
        None
