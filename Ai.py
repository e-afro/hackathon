import time

import Interface
import Player
from multiprocessing import Pool, Process, freeze_support


class Ai:

    def __init__(self, player):
        self.interface = Interface.Interface()
        self.player = Player.Player(player)
        self.infos = dict()
        self.cardvalues = list()

    def getCardValues(self):
        self.cardvalues = self.player.request_get_card_values()

    def getInfos(self):
        # time.sleep(1)
        self.infos = self.player.request_getstatus()
        # pool = Pool(processes=1)
        # pool.apply_async(self.interface.updateInterface, [self.infos["rows"], self.player.cards, self.infos["playersWaitingFor"]])
        # self.interface.updateInterface(self.infos["rows"], self.player.cards, self.infos["playersWaitingFor"])
        """process = Process(target=self.interface.updateInterface, args=[self.infos["rows"], self.player.cards, self.infos["playersWaitingFor"]])
        process.start()
        process.join()"""

    def rightNumberOfPlayer(self):

        total = self.infos["numberOfPlayers"]
        listOfPlayer = self.infos["playersWaitingFor"] + self.infos["playersReady"]
        somme = len(listOfPlayer)
        # print("somme = " + str(somme))
        # print("total = " + str(total))

        return somme < total

    def initGame(self):
        # self.interface.createInterface()
        # print "Interface is created"
        self.player.request_join()
        print self.player.player + " has joined"

        print "Starting to get Infos"
        self.getInfos()

        print "Waiting for player(s)"
        while self.rightNumberOfPlayer():
            self.getInfos()

        self.player.request_get_cards()
        self.cardvalues = self.player.request_get_card_values()

    def getLastCards(self):
        lastCards = list()
        for r in self.infos["rows"]:
            for i, e in enumerate(r):
                if e == 0:
                    lastCards.append(r[i-1])
                    break
        lastCards.sort()

        return lastCards

    def getRowValue(self, row):
        value = 0
        for c in row:
            value += self.cardvalues[c-1]

        return value

    def selectRow(self):
        self.getInfos()
        index = 0
        value = 0

        for i, r in enumerate(self.infos["rows"]):
            tmp = self.getRowValue(r)
            if tmp < value or value == 0:
                value = tmp
                index = i

        self.player.request_select_row(index)

    def playCard(self):
        self.getInfos()

        if self.player.cards == list():
            return 2
        elif self.infos["playersWaitingFor"] != list() and self.player.player not in self.infos["playersWaitingFor"]:
            return 3

        lastCards = self.getLastCards()
        for c in lastCards:
            tmp = list(self.player.cards)
            tmp.append(c)
            tmp.sort()
            index = tmp.index(c)

            if index < len(tmp)-1:
                self.player.request_play_card(tmp[index+1])
                return 0
        self.player.request_play_card(self.player.cards[0])
        return 1

    def displayGame(self):
        self.getInfos()
        rows = self.infos["rows"]
        print "State " + str(self.infos["state"])
        print "Waiting For : " + str(self.infos["playersWaitingFor"])
        print "Ready : " + str(self.infos["playersReady"]) + '\n'
        print "CARDS " + str(len(self.player.cards)) + ": " + str(self.player.cards)
        for i, r in enumerate(self.infos["rows"]):
            print "Row " + str(i) + ": " + str(r)
        """for key, value in self.infos.items():
            print str(key) + " : " + str(value)"""
        print '\n\n'

    def getNewCards(self):
        # if self.player.cards == list() and self.player.player in self.infos["playersWaitingFor"]:
        self.player.request_get_cards()
        print "Current ranking :" + str(self.infos["currentRanking"])

    def startGame(self):
        self.initGame()

        print "Initiate loop"
        while len(self.infos["finalRanking"]) == 0:
            self.displayGame()
            if self.infos["state"] == 1 or (self.infos["state"] == 2 and self.player.cards == list()):
                self.getNewCards()
                self.playCard()
                print str(self.infos) + '\n\n'
            elif self.infos["state"] == 2:
                self.playCard()
            elif self.infos["state"] == 3:
                self.selectRow()
            # print "SELECT ROW state : " + str(self.infos["state"])
            if self.player.failed > 50:
                break

        if self.infos["finalRanking"] == list():
            print "Ranks : " + str(self.infos["finalRanking"])
        else:
            print "Ranks : " + str(self.infos["currentRanking"])

if __name__ == "__main__":
    freeze_support()