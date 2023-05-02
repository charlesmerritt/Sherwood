import taipy as tp
import pandas as pd
# Only used for clickable images
import webbrowser
from main import *
from util import exception_handler
import os
import datetime

root = """
## Sherwood Visualization Tool
<|navbar|>
"""

Home = """
### Welcome!
##### This is the home page, where you can find information about the project and the team.
##### Click on the buttons above to navigate to the other pages.
##### You can explore data from the House of Representatives and the Senate.

### About the Project   
=========================
<|layout|columns=1 3|>

"""

House = """
### Parameters
##### Enter a date range, or select 'live' to get the most recent data.
##### Enter a congress member's name, or choose one from the dropdown menu.
##### Enter a ticker symbol to search for, or leave it blank.
"""

Senate = """
## This is page 3
"""

pages = {
    "/": root,
    "Home": Home,
    "House": House,
    "Senate": Senate
}

logo = "img/arrow.png"


def get_data(path: str):
    dataset = pd.read_csv(path)
    dataset["Date"] = pd.to_datetime(dataset["Date"]).dt.date
    return dataset


def start_date_onchange(state, var_name, value):
    state.start_date = value.date()


def end_date_onchange(state, var_name, value):
    state.end_date = value.date()

def filter_by_date_range(dataset, start_date, end_date):
    mask = (dataset['Date'] > start_date) & (dataset['Date'] <= end_date)
    return dataset.loc[mask]


gui = tp.Gui(pages=pages)


if __name__ == '__main__':
    app = gui.run(title='Sherwood Visualization Tool',
                  dark_mode=True,
                  use_reloader=True,)