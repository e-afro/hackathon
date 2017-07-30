import JsonHandler
import Requester


class Command:

    def __init__(self):
        self.json_handler = JsonHandler.JsonHandler()
        self.requester = Requester.Requester()

    def load_parameters(self, action, value=None):
        self.requester.build_request(action)
        self.json_handler.load_data(action, value)

    def execute(self):
        json_data = self.json_handler.get_data()

        return self.requester.do_request(json_data)
