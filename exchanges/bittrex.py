import os
import json
from core.exchange import Exchange
from bittrex.bittrex import Bittrex as _Bittrex


#----------------------------------------------
#        Bittrex Crypto Exchange API
#----------------------------------------------

class Bittrex(Exchange):

    def __init__(self, config):
        Exchange.__init__(self, config)
        self._name = "Bittrex"
        self.my_exchange = _Bittrex(self._key, self._secret)
        

    def setConfig(self):
        with open(os.getcwd() + "/core/keys.json") as config:
            keys = json.load(config)
            self._key = keys["BITTREX"]["KEY"]
            self._secret = keys["BITTREX"]["SECRET"]

    
    def getSummary(self):
        url = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=' + self._market
        resp = self.request(url)
        #resp = response.json()
        if not  resp["success"]:
            raise Exception('Bittrex: {resp["message"]} (Pair: ' + self._market +')')

        summary = {
            "endpoint"  :   url,
            "bid"       :   '{0:.8f}'.format(float(resp["result"][0]["Bid"])),
            "ask"       :   '{0:.8f}'.format(float(resp["result"][0]["Ask"])),
            "last"      :   '{0:.8f}'.format(float(resp["result"][0]["Last"])),
            "volume"    :   float(resp["result"][0]["BaseVolume"]),
            "yesterday" :   '{0:.8f}'.format(float(resp["result"][0]["PrevDay"]))
        }
        last = float(resp["result"][0]["Last"])
        yesterday = float(resp["result"][0]["PrevDay"])
        summary["change"] = round((last - yesterday)/((last + yesterday)/2) * 10**4)/10**2

        return summary


    def getBalance(self):
        return self.my_exchange.get_balance(self._coin)["result"]["Available"]


    def buy(self, quantity, price):
        response = self.my_exchange.buy_limit(self._market, quantity, price)
        if response["success"]:
            return response["result"]["uuid"]
        else:
            raise Exception(response["message"])


    def sell(self, quantity, price):
        response = self.my_exchange.sell_limit(self._market, quantity, price)
        if response["success"]:
            return response["result"]["uuid"]
        else:
            raise Exception(response["message"])


    def cancel(self, uid):
        return self.my_exchange.cancel(uid)["success"]


    def getOpenOrders(self):
        orders = self.my_exchange.get_open_orders()["result"]
        result = []
        for order in orders:
            message = f'Order {order["OrderUuid"]}\n\n{order["Exchange"]}\nType: {order["OrderType"]}\nQuantity: {order["Quantity"]}\nPrice: {order["Limit"]}\nBTC total: {order["Limit"]*order["Quantity"]}\n\nOpen: {order["Closed"] == None}'
            result.append(message)
        
        return result

    def getOrder(self, uid):
        order = self.my_exchange.get_order(uid)["result"]
        return order
    
    def getOrderStatus(self, uid):
        order = self.my_exchange.get_order(uid)["result"]
        return f'Order {order["OrderUuid"]}\n\n{order["Exchange"]}\nType: {order["Type"]}\nQuantity: {order["Quantity"]}\nPrice: {order["Limit"]}\nBTC total: {order["Reserved"]}\n\nOpen: {order["IsOpen"]}'
    
    def getAsk(self):
        return self.my_exchange.get_marketsummary(self._market)["result"][0]["Ask"]
    
    def getBid(self):
        return self.my_exchange.get_marketsummary(self._market)["result"][0]["Bid"]

    def getLast(self):
        return self.my_exchange.get_marketsummary(self._market)["result"][0]["Last"]














# $client = new-object System.Net.WebClient
# $client.DownloadFile("http://demo.interface.club/limitless/layout_1/RTL/default","C:\template\")