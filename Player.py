import json
import urllib2


class Player:

    def __init__(self, player):
        self.player = player
        self.url = 'http://localhost:1976/'
        self.userID = ''

    def join(self):
        data = {"username": self.player}
        req = urllib2.Request(self.url+"join")
        req.add_header('Content-Type', 'application/json')

        response = urllib2.urlopen(req, json.dumps(data))

        dic = json.load(response)
        self.userID = dic["userID"]

    def getstatus(self):

        req = urllib2.Request(self.url+"getStatus")
        req.add_header('Content-Type', 'application/json')
        data = {"userID": self.userID}

        response = urllib2.urlopen(req, json.dumps(data))

        print response.read()


p = list()
p.append(Player("pascal"))
p.append(Player("david"))

for i in p:
    i.join()
    i.getstatus()

