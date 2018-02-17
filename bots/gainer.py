from core.bot import Bot
import time

#----------------------------------------------
#                Gainer Bot
#---------------------------------------------


class Gainer(Bot):

    def __init__(self, config):
        self._name = "Gainer"
        Bot.__init__(self, config)

    def trade(self):
        # Print Start Trading Message
        print(self._name + " Bot Started Trading.")
        # Run
        while self._run:
            #Get Market Summary
            data   = self._exchange.getSummary()
            #Analyze What To Do Based On Market Data
            action = self._algorithm.analyze(data)
            #Set Record In The Log
            # record = self.log(action, data['last'])
            # print(record)
            time.sleep(self._interval)
