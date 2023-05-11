from main import *
import pandas as pd
import json
import runpy as rp
from congress import CongressMembers
from datetime import datetime


def exception_handler(func):
    """
    Decorator to handle exceptions in functions
    :param func: The function to be checked for exceptions
    :return: inner: The function which handles exceptions
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"{func.__name__} raised an exception: {e}")

    return inner


def parse_json(path):
    with open(path, 'r') as file:
        return json.load(file)


def convert_congress_members(json_dict):
    members = []
    for politician in json_dict:
        members.append(CongressMembers(politician['id'], f"{politician['first_name']} {politician['last_name']}",
                                       politician['state'],
                                       datetime.strptime(politician['last_updated'][0:10], '%Y-%m-%d').date()))

    return members


rp.run_path('./ProPublica_data.py')
senate_members = convert_congress_members(parse_json('./member_senate_data.json'))
house_members = convert_congress_members(parse_json('./member_house_data.json'))


def get_members(state, is_house):
    new_list = []
    encountered_ids = []
    members = house_members if is_house else senate_members
    for member in members:
        if member.state == state and member.id not in encountered_ids:
            new_list.append(member)
            encountered_ids.append(member.id)

    # API returns old senators so most recent 2 are selected
    if not is_house:
        new_list.sort(key=lambda m: m.last_updated)
        new_list = new_list[-2:]
    return new_list


def create_profile(json, id, name):
    for politician in json:
        if politician['id'] == id:
            party = politician['party']
    return CallObject(id, name, party)


def update_profile(profile, ticker, daterange, tradetype):
    profile.setStockData(ticker=ticker,
                         daterange=daterange, tradetype=tradetype)
    return profile


def json_to_csv(json):
    """
    :param json: The json object to be parsed into a CSV
    :return: csv: The csv which contains the data from the json object
    """
    df = pd.read_json(json)
    csv = df.to_csv('data.csv')
    return csv