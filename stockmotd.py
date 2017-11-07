#!/usr/bin/python
import requests

headers = {
    'User-Agent': 'stockmotd',
}

symbol = 'fds'
url = 'https://api.iextrading.com/1.0/stock/%s/quote' % symbol

data = requests.get(url, headers = headers)
json_data = data.json()

print str(json_data['symbol']) + ": " + str(json_data['latestPrice'])
