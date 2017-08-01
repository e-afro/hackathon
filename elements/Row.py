class Row:

    def __init__(self, cards=list()):
        self.cards = cards

    def get_value(self):
        row_value = 0

        for card in self.cards:
            row_value += card.value

        return row_value
