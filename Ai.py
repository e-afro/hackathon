import Player
import time

class Ai:

    def __init__(self, player):
        self.player = Player.Player(player)
        self.infos = dict()
        self.cardvalues = list()

    def getCardValues(self):
        self.cardvalues = self.player.request_get_card_values()

    def getInfo(self):
        time.sleep(1)
        self.infos = self.player.request_getstatus()

    def rightNumberOfPlayer(self):

        total = self.infos["numberOfPlayers"]
        listOfPlayer = self.infos["playersWaitingFor"] + self.infos["playersReady"]
        somme = len(listOfPlayer)

        return somme < total

    def initGame(self):
        self.player.join()

        self.getInfos()

        while self.rightNumberOfPlayer():
            self.getInfos()

        self.player.request_get_cards()

    def startGame(self):
        self.initGame()

        while len(self.infos["finalRanking"]) == 0:
            None
            #TODO


