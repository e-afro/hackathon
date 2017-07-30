import JsonSend


format_data = {"playCard": ["card", "action"],
               "selectRow": ["row", "action"],
               "join": ["username", "authorization"],
               "userID": ["userID", "authorization"]}


class JsonHandler:

    def __init__(self):
        self.json_send = JsonSend.JsonSend()

    def load_data(self, action, value):
        form = format_data[action]

        if form[1] == "action":
            self.json_send.action_data = {form[0]: value}
        elif form[1] == "authorization":
            self.json_send.auth_data = {form[0]: value}
        else:
            self.json_send.action_data.clear()

    def get_data(self):
        return dict(self.json_send.data)
