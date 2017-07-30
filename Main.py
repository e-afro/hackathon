# import Player
import Ai
import urllib2
# import Interface
# from multiprocessing import Pool, Process, freeze_support
# import time

def createBot(index):
    try:
        return Ai.Ai("pascal_bot_"+str(index))
    except urllib2.HTTPError:
        createBot(index + 1)

i = 0
ai = createBot(i)
ai.startGame()

"""freeze_support()

pool = Pool(processes=2)
ais = list()
bot_number = 2
for i in range(bot_number, bot_number+1):
    ais.append(Ai.Ai("new_bot_test"+str(i)))

for a in ais:
    pool.apply_async(a.startGame())
    time.sleep(1)"""

"""if __name__ == "__main__":
    freeze_support()"""
