from elements import Card


class Deck:

    def __init__(self):
        self.cards = list()

    def build_all_cards(self, card_values):
        for value in range(1, 105):
            points = card_values[value]
            card = Card.Card(value, points)
            self.cards.append(card)
