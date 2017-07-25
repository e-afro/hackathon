import json
import urllib2


class Player:

    def __init__(self, player):
        self.player = player
        self.url = 'http://localhost:1976/'
        self.userID = ''
        self.cards = list()
        self.cardvalues = list()

    def init_request(self, action):
        req = urllib2.Request(self.url + action)
        req.add_header('Content-Type', 'application/json')

        return req

    def request_join(self):
        data = {"username": self.player}
        req = self.init_request("join")

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)
        self.userID = dic["userID"]

    def request_getstatus(self):
        data = {"userID": self.userID}
        req = self.init_request("getStatus")

        response = urllib2.urlopen(req, json.dumps(data))

        #print response.read()
        return json.load(response)


    def request_get_cards(self):
        data = {"userID": self.userID}
        req = self.init_request("getCards")

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)
        self.cards = dic["cards"]

    def request_play_card(self, card):
        data = {"userID": self.userID, "card": card}
        req = self.init_request("playCard")

        response = urllib2.urlopen(req, json.dumps(data))

    def request_get_card_values(self):
        data = {"userID": self.userID}
        req = self.init_request("getCardValues")

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)
        self.cardvalues = dic["cardvalues"]

p = list()
p.append(Player("test6"))
p.append(Player("test7"))

for i in p:
    i.request_join()
    i.request_getstatus()

for i in p:
    i.request_get_cards()

for i in p:
    i.request_play_card(i.cards[1])

for i in p:
    i.request_getstatus()

for i in p:
    i.request_get_card_values()