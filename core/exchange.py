import json
import os
import time
import urllib.request as request
from datetime import datetime
import numpy as np

#----------------------------------------------
#   Base Class Of Exchange Trading Platform
#----------------------------------------------

class Exchange:
    _key      = None
    _secret   = None
    _name     = None
    _balance  = None
    _market   = None
    _coin     = None
 
    def __init__(self, config):
        self._market = config['market']
        self._coin   = config['coin']
        self.setConfig()

    def request(self, url):
        response = request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        data     = json.loads(response.read().decode(encoding))
        return data

    def getName(self):
        return self._name

    def setConfig(self):
            pass 

    def getAccountDetails(self):
        pass

    def getOrder(self, uid):
        pass

    def getOrders(self):
        pass

    def getSummary(self):
        pass

    def getBalance(self):
        pass

    def buy(self, quantity, price):
        pass 

    def sell(self, quantity, price):
        pass
    
    def cancel(self, uid):
        pass

    
    
