from elements import Card


class Deck:

    def __init__(self):
        self.cards = list()

    def build_all_cards(self, card_values):
        for value in range(1, 105):
            points = card_values[value]
            card = Card.Card(value, points)
            self.cards.append(card)

    def get_card_by_value(self, value):
        for card in self.cards:
            if card.value == value:
                return card

        return None

    def remove_card_by_value(self, value):
        if value == 0:
            return None

        for card in self.cards:
            if card.value == value:
                self.cards.remove(card)
                return card

        return None
