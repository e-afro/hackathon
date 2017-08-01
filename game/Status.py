import Board
import Deck


class Status:

    def __init__(self):
        self.deck = Deck.Deck()
        self.board = Board.Board()

    def load(self, response):
        card_values = response["cardvalues"]
        rows = response["rows"]

        if card_values is not None:
            self.deck.build_all_cards(card_values)
        if rows is not None or not None in rows:
            self.board.build_rows(self.deck, rows)
