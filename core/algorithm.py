import json
import time
import urllib.request as request
from datetime import datetime
import numpy as np

#----------------------------------------------
#       Base Class Of Algorithm
#---------------------------------------------

class Algorithm:

    def __init__(self):
        pass 
    
    def analyze(self, data):
        pass

    def getName(self):
        return self._name

