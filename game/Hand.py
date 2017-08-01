class Hand:

    def __init__(self, cards=list()):
        self.cards = cards

    def build_hand(self, deck, cards):
        self.cards = list()
        for c in cards:
            card = deck.get_card_by_value(c)
            self.cards.append(card)
