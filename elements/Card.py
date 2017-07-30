class Card:

    def __init__(self, value, points):
        self.value = value
        self.points = points

    def __eq__(self, card):
        return self.value == card.value

