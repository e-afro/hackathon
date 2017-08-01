from elements import Row


class Board:

    def __init__(self):
        self.rows = list()

    def build_rows(self, deck, rows):
        for r in rows:
            row = Row.Row()
            for c in r:
                card = deck.get_card_by_value(c)
                row.cards.append(card)
            self.rows.append(row)
