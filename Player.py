import json
import urllib2


class Player:

    def __init__(self, player):
        self.player = player
        self.url = 'http://localhost:1976/'
        self.userID = ''
        self.cards = list()

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

        # print response.read()
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

        urllib2.urlopen(req, json.dumps(data))

    def request_get_card_values(self):
        data = {"userID": self.userID}
        req = self.init_request("getCardValues")

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)

        return dic["cardvalues"]

    def request_select_row(self, row):
        data = {"userID": self.userID, "row": row}
        req = self.init_request("selectRow")

        response = urllib2.urlopen(req, json.dumps(data))

        print response.read()
