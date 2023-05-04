from main import *
import pandas as pd


def exception_handler(func):
    """
    Decorator to handle exceptions in functions
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"{func.__name__} raised an exception: {e}")

    return inner


def createProfile(json, id, name):
    for politican in json:
        if politican['id'] == id:
            party = politican['party']
    return CallObject(id, name, party)

def updateProfile(profile, ticker, daterange, tradetype):
    profile.setStockData(ticker=ticker,
        daterange=daterange, tradetype=tradetype)
    return profile

def parseJson(path):
    with open(path, 'r') as file:
        return json.load(file)
def json_to_csv(json):
    """
    :param json: The json object to be parsed into a CSV
    :return: csv: The csv which contains the data from the json object
    """
    df = pd.read_json(json)
    csv = df.to_csv('data.csv')
    return csv
