import Player
import Ai
import interface


def play():
    player = Player.Player("playername")
    ai = Ai.Ai(player)
    ui = interface.Interface()

    ui.createInterface()

play()

