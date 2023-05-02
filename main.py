import json
import requests
import time
import os
from util import *

QUIVER = '20643798f4e7c8bdb2164cf3a4a3831d0cf3b4eb'
PROPUBLICA = 'Z41JVKlvZxtLM1ADHn7Myn7xiWLrW6PKZNwnNtRV'
live_quiverquant_url = 'https://api.quiverquant.com/beta/live/'
hist_quiverquant_url = 'https://api.quiverquant.com/beta/historical/'
congress_propublica_url = 'https://api.propublica.org/congress/v1/'


#TODO: Implement functions of the CallObject class to get the different attributes of the call object and return them
# as well as implement a function to parse the json into a call object.
class CallObject:
    def __init__(self, id, tradetype, daterange, ticker, name):
        self.id = id
        self.tradetype = tradetype
        self.daterange = daterange
        self.ticker = ticker
        self.name = name

#TODO: Maybe merge houseTrades and senateTrades into one function with fstrings
def houseTrades(name=None, ticker='', daterange=None):
    """
    :param name: The name of the Representative whose trades you want to grab,
    :param ticker: The name of the stock symbol which you want to grab. Prefixed by a '/' like '/TSLA'
    :param daterange: MMDDYYYY like [04072018, 05142019]
    :return: r.content: The content of the api call.
    """
    if ticker != '':
        url = f"https://api.quiverquant.com/beta/historical/housetrading{ticker}"
    else:
        url = f"https://api.quiverquant.com/beta/live/housetrading"
    print(url)
    headers = {'accept': 'application/json',
               'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
               'Authorization': f'Token {QUIVER}'}
    r = requests.get(url, headers=headers)
    print(r.content)
    #TODO: Parse r.content (json) into call objects and return those instead, separate function probably
    # obj = CallObject(id, type, daterange, ticker, name)
    return r.content
  
def senateTrades(name=None, ticker='', daterange=None):
    """
    :param name: The name of the Senator whose trades you want to viz,
    :param ticker: The name of the stock symbol which you want to viz. Prefixed by a '/' like '/TSLA'
    :param daterange: MMDDYYYY like [04072018, 05142019]
    :return: r.content: The content of the api call.
    """
    if ticker != '':
        url = f"https://api.quiverquant.com/beta/historical/senatetrading{ticker}"
    else:
        url = f"https://api.quiverquant.com/beta/live/senatetrading"
    print(url)
    headers = {'accept': 'application/json',
               'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
               'Authorization': f'Token {QUIVER}'}
    r = requests.get(url, headers=headers)
    json_data = json.loads(r.content)
    #TODO: Parse r.content into call objects and return those instead
    print(json_data)
    return json_data


def main():
    houseTrades(name='Nancy Pelosi', ticker='/TSLA')
    senateTrades(name='Mitch McConnell', ticker='/TSLA')


if __name__ == '__main__':
    main()
