import json
import time
import numpy as np
import os
import urllib.request as request
from datetime import datetime
from algorithms.mva import MVA
from exchanges.bittrex import Bittrex
from exchanges.binance import Binance


#----------------------------------------------
#          Base Class Of Trading Bot
#----------------------------------------------

class Bot:
    _name      = None
    _exchange  = None
    _algorithm = None
    _interval  = None
    _run       = True
    _config    = None

    def __init__(self, config):
        self._config    = config
        self._interval  = config['interval']
        self.setAlgorithm(config['algorithm'])
        self.setExchange(config['exchange'])
    
    def getName(self):
        return self._name

    def setAlgorithm(self, algorithm):
        if(algorithm.lower() == 'mva'):
            self._algorithm = MVA()

    def getAlgorithm(self):
        return self._algorithm

    def setExchange(self, exchange):
        if(exchange.lower() == 'bittrex'):
            self._exchange = Bittrex(self._config)
        elif(exchange.lower() == 'binance'):
            self._exchange = Binance(self._config)
        else:
            raise Exception("Invalid Exchange")

    def getExchange(self):
        return self._exchange

    def trade(self):
        pass

    def stop(self):
        print(self._name + " Bot Stopped Trading.")
        self._run = False

    def generateLog(self):
        pass

    def log(self, action, price):
        now = datetime.now()
        file = open(os.getcwd() + '/logs/' + self._name + '_' + self._exchange.getName() + '_' + self._algorithm.getName() +'_' + self._exchange._market + '_' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '.txt','a') 
        text = str(now) + ' - ' + action.upper() + ', Price: ' + price
        file.write(text + '\n') 
        file.close()
        return text
