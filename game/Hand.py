class Hand:

    def __init__(self, cards):
        self.cards = cards

    def play_card(self, card):
        self.cards.remove(card)
