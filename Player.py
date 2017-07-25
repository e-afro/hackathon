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

        print response.read()

    def request_get_cards(self):
        data = {"userID": self.userID}
        req = self.init_request("getCards")

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)
        self.cards = dic["cards"]

        print self.cards

p = list()
p.append(Player("test4"))
p.append(Player("test5"))

for i in p:
    i.request_join()
    i.request_getstatus()

for i in p:
    i.request_get_cards()