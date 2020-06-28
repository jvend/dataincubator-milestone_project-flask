import requests
import json
from datetime import datetime
import sys
import time

def build_url(ticker):
    current_time = round(time.time()) #Unix timestamp to nearest second
    start = current_time - 60*60*24*31
    end   = current_time
    interval = '5m'
    
    site = "https://query1.finance.yahoo.com/v7/finance/chart/" + str(ticker) + \
           "?symbol=" + str(ticker) + "&period1=" + str(start) + "&period2="  + \
           str(end) + "&interval=" + str(interval)

    return site
