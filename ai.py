import Player
import time

class Ai:

    def __init__(self, player):
        self.player = Player(player)
        self.infos = dict()

    def getInfo(self):
        time.sleep(1)
        self.infos = self.player.request_getstatus()

    def rightNumberOfPlayer(self):

        total = self.infos["numberOfPlayers"]
        listOfPlayer = self.infos["playersWaitingFor"] + self.infos["playersReady"]
        somme = len(listOfPlayer)

        return somme < total

    def startGame(self):
        self.player.join()

        self.getInfos()

        while self.rightNumberOfPlayer():
            self.getInfos()

        self.player.request_get_cards()

        while len(self.infos["finalRanking"]) == 0:
            #TODO


