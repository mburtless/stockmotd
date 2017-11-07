#!/usr/bin/python
import requests
import argparse

parser = argparse.ArgumentParser(description='Generate a MOTD for stock prices from IEX')
parser.add_argument('-s', '--symbol',help='One or more symbols to include in MOTD text', nargs='*', dest='symbol_list')
args = parser.parse_args()

headers = {
    'User-Agent': 'stockmotd',
}

#symbol = 'fds'
for symbol in args.symbol_list:
    url = 'https://api.iextrading.com/1.0/stock/%s/quote' % symbol

    data = requests.get(url, headers = headers)
    json_data = data.json()

    motd_string = '\x1b[0;36;40m' + json_data['symbol'] + '\x1b[0m' + ": "
    if json_data['latestPrice'] > json_data['previousClose']:
        motd_string += '\x1b[0;32;40m' + str(json_data['latestPrice']) + '\x1b[0m'
    elif json_data['latestPrice'] == json_data['previousClose']:
        motd_string += '\x1b[0;37;40m' + str(json_data['latestPrice']) + '\x1b[0m'
    elif json_data['latestPrice'] < json_data['previousClose']:
        motd_string += '\x1b[0;31;40m' + str(json_data['latestPrice']) + '\x1b[0m'
    print(motd_string)
