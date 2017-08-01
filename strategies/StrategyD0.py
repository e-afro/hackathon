from game import Status


class StrategyD0:

    def __init__(self, bot):
        self.status = Status.Status()

    def get_last_cards(self):
        last_cards = list()
        for row in self.status.board.rows:
            card = row.get_last_card()
            last_cards.append(card)
        last_cards.sort()

        return last_cards

    def play_card(self):
        for c in self.get_last_cards():
            for card in self.status.hand.cards:
                if c < card:
                    return card

        return self.status.hand[0]

    def select_row(self):
        row_index = 0
        value = 0
        for i, row in enumerate(self.status.board.rows):
            if value > row.get_value():
                value = row.get_value()
                row_index = i

        return row_index
