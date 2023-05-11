import requests
from util import *

QUIVER = '20643798f4e7c8bdb2164cf3a4a3831d0cf3b4eb'
PROPUBLICA = 'Z41JVKlvZxtLM1ADHn7Myn7xiWLrW6PKZNwnNtRV'
live_quiverquant_url = 'https://api.quiverquant.com/beta/live/'
hist_quiverquant_url = 'https://api.quiverquant.com/beta/historical/'
congress_propublica_url = 'https://api.propublica.org/congress/v1/'

class CallObject:
    def __init__(self, id, name, party, leadershipRole=''):
        self.id = id
        self.party = party
        self.name = name
        self.leadershipRole = leadershipRole
    def setStockData(self, ticker, daterange, tradetype):
        self.ticker = ticker
        self.daterange = daterange
        self.tradetype = tradetype
    def getPoliticianInfo(self):
        return self.id, self.party, self.name, self.leadershipRole
    def getStockData(self):
        return self.ticker, self.daterange, self.tradetype


def get_trades(name=None, ticker='', daterange=None, is_house = True):
    """
    :param name: The name of the Representative whose trades you want to grab,
    :param ticker: The name of the stock symbol which you want to grab. Prefixed by a '/' like '/TSLA'
    :param daterange: MMDDYYYY like [04072018, 05142019]
    :return: r.content: The content of the api call.
    """
    if ticker != '':
        if is_house:
            chamber = 'house'
            url = f"https://api.quiverquant.com/beta/historical/{chamber}trading{ticker}"
        else:
            chamber = 'senate'
            url = f"https://api.quiverquant.com/beta/historical/{chamber}trading{ticker}"
    else:
        if is_house:
            chamber = 'house'
            url = f"https://api.quiverquant.com/beta/live/{chamber}trading"
        else:
            chamber = 'senate'
            url = f"https://api.quiverquant.com/beta/live/{chamber}trading"
    print(url)
    headers = {'accept': 'application/json',
               'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
               'Authorization': f'Token {QUIVER}'}
    r = requests.get(url, headers=headers)
    json_data = json.loads(r.content)
    if name:
        filtered_data = []
        for trade in json_data:
            if is_house:
                if trade['Representative'].strip() == name:
                    filtered_data.append(trade)
            else:
                if trade['Senator'].strip() == name:
                    filtered_data.append(trade)
        print(filtered_data)
        return filtered_data
    else:
        print(json_data)
        return json_data


def main():
    get_trades(name='Nancy Pelosi', ticker='')
    get_trades(name='Nancy Pelosi', ticker='/TSLA')
    get_trades(name='Whitehouse, Sheldon', ticker='/T', is_house=False)
    get_trades(name='Whitehouse, Sheldon', ticker='', is_house=False)


if __name__ == '__main__':
    main()
