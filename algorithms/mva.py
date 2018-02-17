import time
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
from core.algorithm import Algorithm
from datetime import datetime, timedelta
from scipy.optimize import fsolve

#----------------------------------------------
#         Moving Avarage Algorithm
#---------------------------------------------

class MVA(Algorithm):

    def __init__(self):
        self._name = "MVA"
        Algorithm.__init__(self) 
    
    def analyze(self, data):
       
        days   = []
        prices = []

        for i in range(len(data)): 
            
            date = time.strftime("%H:%M", time.localtime(int(data[i][0]) / 1000))
            days.append(date)
            prices.append(float(data[i][4]))

        window = 3
        x = days
        y = prices

        print(str(days))
        print(str(len(prices)))
        weights = np.repeat(1.0, window)/window
        moving_average = np.convolve(y, weights, 'valid')
        	

        plt.plot(x[len(x)-len(moving_average):],moving_average, label="Moving Average")
        plt.title('Litecoin')
        plt.ylabel('Price (BTC)')
        plt.xlabel('Minutes')
        
        plt.plot(x,y, label="LTC Price")
        plt.legend()
        plt.grid(True)
        plt.show()

        # #Check if data values exists
        # # if data['last'] is None:
        # #     return None
        
        # # if data['lastAction'] is None:
        # #     return None

        # #Get mean average 
        # avg = self.getAvg(data)
        # print(float(data['last']))
        # #Check if avg is higher And your last action is sell and data['lastAction'] == 'sell'
        # if(avg > float(data['last']) ):       
        #     return 'buy'
        #     #  and data['lastAction'] == 'buy'
        # if( avg < float(data['last'])):            
        #     return 'sell'

        # return None

    def getAvg(self, data):
        return 3