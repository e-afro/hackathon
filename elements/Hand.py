class Hand:

    def __init__(self, cards):
        self.cards = cards

    def play(self, card):
        self.cards.remove(card)
