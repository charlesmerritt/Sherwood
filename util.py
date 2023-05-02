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


def json_to_call_object(json):
    """
    :param json: The json object to be parsed into a CallObject
    :return: CallObject: The call object which contains the data from the json object
    """
    id = json['id']
    type = json['type']
    daterange = json['daterange']
    ticker = json['ticker']
    name = json['name']
    return CallObject(id, type, daterange, ticker, name)


def json_to_csv(json):
    """
    :param json: The json object to be parsed into a CSV
    :return: csv: The csv which contains the data from the json object
    """
    df = pd.read_json(json)
    csv = df.to_csv('data.csv')
    return csv
