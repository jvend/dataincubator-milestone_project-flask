#ticker, security_type
#expiry_date = None, start_date = None, end_date = None

import numpy as np
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
  
def scrape_stock_data(ticker):
    url = build_url(ticker)
    page = requests.get(url)
    html = page.content.decode('utf-8')
    data = json.loads(html)['chart']['result'][0]
    datetimes = list(map(datetime.fromtimestamp,data['timestamp']))
    close_data  = np.array(data['indicators']['quote'][0]['close']       )
