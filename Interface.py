import Tkinter as tk


class Interface:

    def __init__(self):
        self.root = None
        self.turnsLabel = None
        self.cardsLabel = None
        self.rowsLabels = list()

    def createInterface(self):
        self.createMainWindow()
        self.createTurnsLabel()
        self.createRowsLabels()
        self.createCardsLabel()

        # self.root.mainloop()

    def createMainWindow(self):
        self.root = tk.Tk()
        # self.root.resizable(width="800", height="500")

    def createLabel(self, c, r, configs):
        label = tk.Label(self.root, text="")
        label.grid(column=c, row=r)

        self.updateLabel(label, configs)

        return label

    def updateLabel(self, label, config):
        for option, value in config.iteritems():
            if option == 'text':
                # print value
                label.configure(text=value)

            if option == 'foreground':
                label.configure(foreground=value)

            if option == 'background':
                label.configure(background=value)

            if option == 'padx':
                label.configure(padx=value)

            if option == 'pady':
                label.configure(pady=value)

    def createTurnsLabel(self):
        config = {'text': "Waiting for : "}

        self.turnsLabel = self.createLabel(0, 0, config)

    def createRowsLabels(self):

        for i in range(1, 5):
            config = {'text': "row" + str(i) + " = " + "0  0  0  0  0  0",
                      'foreground': "#892222",
                      'background': "#FFAAAA",
                      'pady': "10"}

            self.rowsLabels.append(self.createLabel(0, i, config))

    def createCardsLabel(self):
        config = {'text': "Cards = " + "X  X  X  X  X  X  X  X  X  X"}

        self.cardslabel = self.createLabel(0, 5, config)

    def format(self, config):
        f_config = {'text': config}
        # print f_config
        return f_config

    def updateInterface(self, rowsconfig, cardsconfig, turnconfig):
        for i in range(0, 4):
            f_rowsconfig = self.format("row" + str(i) + " = " + str(rowsconfig[i]))
            # self.rowsLabels.append(self.createLabel(0, i, f_rowsconfig))
            # f_rowsconfig = {'text': "row" + str(i) + " = " + "1  0  0  0  0  0"}
            self.updateLabel(self.rowsLabels[i], f_rowsconfig)

        """f_cardsconfig = self.format("Cards = " + str(cardsconfig))
        f_turnconfig = self.format("Waiting for : " + str(turnconfig))
        self.updateLabel(self.cardsLabel, f_cardsconfig)
        self.updateLabel(self.turnsLabel, f_turnconfig)"""


