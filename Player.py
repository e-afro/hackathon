import json
import urllib2


class Player:

    def __init__(self, player):
        self.player = player
        self.url = 'http://mapps4u.com:1976/'
        self.userID = ''
        self.cards = list()
        self.failed = 0

    def init_request(self, action):
        req = urllib2.Request(self.url + action)
        req.add_header('Content-Type', 'application/json')

        return req

    def request_join(self, name_index=0):
        if name_index > 0:
            self.player += str(name_index)
        data = {"username": self.player}
        req = self.init_request("join")

        try:
            response = urllib2.urlopen(req, json.dumps(data))

            dic = json.load(response)
            self.userID = str(dic["userID"])
        except urllib2.HTTPError as e:
            self.request_join(name_index+1)

    def request_getstatus(self):
        data = {"userID": self.userID}
        req = self.init_request("getStatus")
        req.add_data(json.dumps(data))

        response = urllib2.urlopen(req)

        # print response.read()
        game_dictionary = json.load(response)

        return game_dictionary["game"]

    def request_get_cards(self):
        data = {"userID": self.userID}
        req = self.init_request("getCards")

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)
        self.cards = dic["cards"]
        self.cards.sort()

    def request_play_card(self, card):
        bug = 1
        data = {"userID": self.userID, "card": card}
        try:
            req = self.init_request("playCard")
            urllib2.urlopen(req, json.dumps(data))
            self.cards.remove(card)
            bug = 0
            self.failed = 0
        except urllib2.HTTPError as e:
            if 0 != bug:
                self.cards.remove(card)
            # print "Failed to play card : " + str(card)
            self.failed += 1
            # print e
            None

    def request_get_card_values(self):
        data = {"userID": self.userID}
        req = self.init_request("getCardValues")

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)

        return dic["cardvalues"]

    def request_select_row(self, row):
        try:
            data = {"userID": self.userID, "row": row}
            req = self.init_request("selectRow")

            urllib2.urlopen(req, json.dumps(data))
            self.failed = 0
        except urllib2.HTTPError as e:
            print "Failed to select row : " + str(row)
            self.failed += 1
            None
