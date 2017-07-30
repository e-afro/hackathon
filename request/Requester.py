import urllib2


class Requester:

    def __init__(self):
        self.url = 'http://mapps4u.com:1976/'
        self.request = None

    def create_request(self, action):
        self.request = urllib2.Request(self.url + str(action))
        self.request.add_header('Content-Type', 'application/json')

    def do_request(self, data):
        try:
            return urllib2.urlopen(self.request, data)
        except urllib2.HTTPError:
            return None
