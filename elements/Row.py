class Row:

    def __init__(self, cards=list()):
        self.cards = cards

    def get_value(self):
        row_value = 0

        for card in self.cards:
            row_value += card.value

        return row_value

    def get_last_card(self):
        last_card = None
        for card in self.cards:
            if card is not None:
                last_card = card

        return last_card
