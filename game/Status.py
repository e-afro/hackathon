import Board
import Deck
import Hand


class Status:

    def __init__(self):
        self.deck = Deck.Deck()
        self.board = Board.Board()
        self.hand = Hand.Hand()

    def load(self, response):
        card_values = response["cardvalues"]
        rows = response["rows"]
        cards = response["cards"]

        if card_values is not None:
            self.deck.build_all_cards(card_values)
        elif rows is not None or None not in rows:
            self.board.build_rows(self.deck, rows)
        elif cards is not None:
            self.hand.build_hand(cards)
