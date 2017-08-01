class State:

    def __init__(self):
        self.state = 0
        self.waiting_for = True
        self.is_ready = False

    def load(self, name, response):
        waiting_list = response["playersWaitingFor"]
        ready_list = response["playersReady"]

        if waiting_list is not None:
            self.waiting_for = len(waiting_list) > 0
        if ready_list is not None:
            self.is_ready = name in ready_list
