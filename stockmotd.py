#!/usr/bin/python
import requests
import argparse

def parse_args():
    """Parse arguments"""
    parser = argparse.ArgumentParser(description='Get the latest stock prices for symbols from IEX')
    parser.add_argument('-s', '--symbol', type=str, required=True, default='fds', nargs='+', dest='symbol_list', help='List of one or more symbols to get prices for')
    return parser.parse_args()

if __name__ == '__main__':
    headers = {
        'User-Agent': 'stockmotd',
    }

    #symbol = 'fds'
    args = parse_args()

    for symbol in args.symbol_list:
        url = 'https://api.iextrading.com/1.0/stock/%s/quote' % symbol

        data = requests.get(url, headers = headers)
        json_data = data.json()

        motd_string = '\x1b[0;36;40m' + json_data['symbol'] + '\x1b[0m' + ": "
        if json_data['latestPrice'] > json_data['previousClose']:
            motd_string += '\x1b[0;32;40m'
        elif json_data['latestPrice'] == json_data['previousClose']:
            motd_string += '\x1b[0;37;40m'
        elif json_data['latestPrice'] < json_data['previousClose']:
            motd_string += '\x1b[0;31;40m'
        motd_string += str(json_data['latestPrice']) + '\x1b[0m'
        print(motd_string)
