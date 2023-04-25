import json
import requests

AUTH_TOKEN = 'REDACTED'

def houseTrades(name=None, ticker='', daterange=None):
    """
    :param name: The name of the Representative whose trades you want to viz,
    :param ticker: The name of the stock symbol which you want to viz. Prefixed by a '/' like '/TSLA'
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
               'Authorization': f'Token {AUTH_TOKEN}'}
    r = requests.get(url, headers=headers)
    print(r.content)
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
               'Authorization': f'Token {AUTH_TOKEN}'}
    r = requests.get(url, headers=headers)
    print(r.content)
    return r.content
