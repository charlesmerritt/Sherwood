import taipy as tp
from taipy.gui import Gui, notify
import pandas as pd
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
##### This project was created as a final project for Data Science I at the University of Georgia under the instruction
##### of Dr. Maria Hybinette. The project was created by: Charles Merritt, Brennin Heinel, and Edward Hayashi. 
##### The goal of this project is to create a visualization tool that allows users to explore data from the House of
##### Representatives and the Senate. The data is pulled from the ProPublica Congress API, as well as the Quiver
##### Quantitative Finance API. The rest of the project is written in Python, using the Taipy library for the GUI, and
##### core data science libraries such as Pandas, Numpy, and Matplotlib.

### How to use Sherwood
=========================
##### To use Sherwood, simply click on the buttons below to navigate to the other pages. You can explore data from the
##### House of Representatives and the Senate. There you can select a state to view data for representatives from that
##### state. Once you have selected a representative, you can visualize their trades in a variety of ways. Such as
##### viewing their trades by date, or by ticker. You can also view the total value of their trades over time. You can
##### also view the total value of trades for all representatives from a given state. You can also view a pie chart
##### showing the distribution of stock purchases by industry.
<|layout|columns=1 3|> 

"""

House = """
##### Select a state to view data for representatives from that state.
<|layout|columns=1 1|
<|States|expandable|
<|Alabama|button|on_action=house_on_button_action|id=AL|>
<|Alaska|button|on_action=house_on_button_action|id=AK|>
<|Arizona|button|on_action=house_on_button_action|id=AZ|>
<|Arkansas|button|on_action=house_on_button_action|id=AR|>
<|California|button|on_action=house_on_button_action|id=CA|>
<|Colorado|button|on_action=house_on_button_action|id=CO|>
<|Connecticut|button|on_action=house_on_button_action|id=CT|>
<|Delaware|button|on_action=house_on_button_action|id=DE|>
<|Florida|button|on_action=house_on_button_action|id=FL|>
<|Georgia|button|on_action=house_on_button_action|id=GA|>
<|Hawaii|button|on_action=house_on_button_action|id=HI|>
<|Idaho|button|on_action=house_on_button_action|id=ID|>
<|Illinois|button|on_action=house_on_button_action|id=IL|>
<|Indiana|button|on_action=house_on_button_action|id=IN|>
<|Iowa|button|on_action=house_on_button_action|id=IA|>
<|Kansas|button|on_action=house_on_button_action|id=KS|>
<|Kentucky|button|on_action=house_on_button_action|id=KY|>
<|Louisiana|button|on_action=house_on_button_action|id=LA|>
<|Maine|button|on_action=house_on_button_action|id=ME|>
<|Maryland|button|on_action=house_on_button_action|id=MD|>
<|Massachusetts|button|on_action=house_on_button_action|id=MA|>
<|Michigan|button|on_action=house_on_button_action|id=MI|>
<|Minnesota|button|on_action=house_on_button_action|id=MN|>
<|Mississippi|button|on_action=house_on_button_action|id=MS|>
<|Missouri|button|on_action=house_on_button_action|id=MO|>
<|Montana|button|on_action=house_on_button_action|id=MT|>
<|Nebraska|button|on_action=house_on_button_action|id=NE|>
<|Nevada|button|on_action=house_on_button_action|id=NV|>
<|New Hampshire|button|on_action=house_on_button_action|id=NH|>
<|New Jersey|button|on_action=house_on_button_action|id=NJ|>
<|New Mexico|button|on_action=house_on_button_action|id=NM|>
<|New York|button|on_action=house_on_button_action|id=NY|>
<|North Carolina|button|on_action=house_on_button_action|id=NC|>
<|North Dakota|button|on_action=house_on_button_action|id=ND|>
<|Ohio|button|on_action=house_on_button_action|id=OH|>
<|Oklahoma|button|on_action=house_on_button_action|id=OK|>
<|Oregon|button|on_action=house_on_button_action|id=OR|>
<|Pennsylvania|button|on_action=house_on_button_action|id=PA|>
<|Rhode Island|button|on_action=house_on_button_action|id=RI|>
<|South Carolina|button|on_action=house_on_button_action|id=SC|>
<|South Dakota|button|on_action=house_on_button_action|id=SD|>
<|Tennessee|button|on_action=house_on_button_action|id=TN|>
<|Texas|button|on_action=house_on_button_action|id=TX|>
<|Utah|button|on_action=house_on_button_action|id=UT|>
<|Vermont|button|on_action=house_on_button_action|id=VT|>
<|Virginia|button|on_action=house_on_button_action|id=VA|>
<|Washington|button|on_action=house_on_button_action|id=WA|>
<|West Virginia|button|on_action=house_on_button_action|id=WV|>
<|Wisconsin|button|on_action=house_on_button_action|id=WI|>
<|Wyoming|button|on_action=house_on_button_action|id=WY|>
|>
|>
"""

Senate = """
##### Select a state to view data for senators from that state.
<|layout|columns=1 3|
<|States|expandable|
<|Alabama|button|on_action=senate_on_button_action|id=AL|>
<|Alaska|button|on_action=senate_on_button_action|id=AK|>
<|Arizona|button|on_action=senate_on_button_action|id=AZ|>
<|Arkansas|button|on_action=senate_on_button_action|id=AR|>
<|California|button|on_action=senate_on_button_action|id=CA|>
<|Colorado|button|on_action=senate_on_button_action|id=CO|>
<|Connecticut|button|on_action=senate_on_button_action|id=CT|>
<|Delaware|button|on_action=senate_on_button_action|id=DE|>
<|Florida|button|on_action=senate_on_button_action|id=FL|>
<|Georgia|button|on_action=senate_on_button_action|id=GA|>
<|Hawaii|button|on_action=senate_on_button_action|id=HI|>
<|Idaho|button|on_action=senate_on_button_action|id=ID|>
<|Illinois|button|on_action=senate_on_button_action|id=IL|>
<|Indiana|button|on_action=senate_on_button_action|id=IN|>
<|Iowa|button|on_action=senate_on_button_action|id=IA|>
<|Kansas|button|on_action=senate_on_button_action|id=KS|>
<|Kentucky|button|on_action=senate_on_button_action|id=KY|>
<|Louisiana|button|on_action=senate_on_button_action|id=LA|>
<|Maine|button|on_action=senate_on_button_action|id=ME|>
<|Maryland|button|on_action=senate_on_button_action|id=MD|>
<|Massachusetts|button|on_action=senate_on_button_action|id=MA|>
<|Michigan|button|on_action=senate_on_button_action|id=MI|>
<|Minnesota|button|on_action=senate_on_button_action|id=MN|>
<|Mississippi|button|on_action=senate_on_button_action|id=MS|>
<|Missouri|button|on_action=senate_on_button_action|id=MO|>
<|Montana|button|on_action=senate_on_button_action|id=MT|>
<|Nebraska|button|on_action=senate_on_button_action|id=NE|>
<|Nevada|button|on_action=senate_on_button_action|id=NV|>
<|New Hampshire|button|on_action=senate_on_button_action|id=NH|>
<|New Jersey|button|on_action=senate_on_button_action|id=NJ|>
<|New Mexico|button|on_action=senate_on_button_action|id=NM|>
<|New York|button|on_action=senate_on_button_action|id=NY|>
<|North Carolina|button|on_action=senate_on_button_action|id=NC|>
<|North Dakota|button|on_action=senate_on_button_action|id=ND|>
<|Ohio|button|on_action=senate_on_button_action|id=OH|>
<|Oklahoma|button|on_action=senate_on_button_action|id=OK|>
<|Oregon|button|on_action=senate_on_button_action|id=OR|>
<|Pennsylvania|button|on_action=senate_on_button_action|id=PA|>
<|Rhode Island|button|on_action=senate_on_button_action|id=RI|>
<|South Carolina|button|on_action=senate_on_button_action|id=SC|>
<|South Dakota|button|on_action=senate_on_button_action|id=SD|>
<|Tennessee|button|on_action=senate_on_button_action|id=TN|>
<|Texas|button|on_action=senate_on_button_action|id=TX|>
<|Utah|button|on_action=senate_on_button_action|id=UT|>
<|Vermont|button|on_action=senate_on_button_action|id=VT|>
<|Virginia|button|on_action=senate_on_button_action|id=VA|>
<|Washington|button|on_action=senate_on_button_action|id=WA|>
<|West Virginia|button|on_action=senate_on_button_action|id=WV|>
<|Wisconsin|button|on_action=senate_on_button_action|id=WI|>
<|Wyoming|button|on_action=senate_on_button_action|id=WY|>
|>|>

<|Expand|button|on_action={lambda s: s.assign("show", True)}|>
<|{show}|pane|persistent|anchor=right|on_close={lambda s: s.assign("show", False)}|width=600px|
<|Senators|expandable|

|>
<|{dt}|date|not with_time|on_change=start_date_onchange|>
|>
|>
"""

pages = {
    "/": root,
    "Home": Home,
    "House": House,
    "Senate": Senate
}

show = True
logo = "img/arrow.png"
dt = datetime.datetime.now().strftime("%Y-%m-%d")

def senate_on_button_action(id):
    member_df, member_data = createStateLedger(id, 0)
    #TODO create an actionable set of buttons with the names from the data frame
    # Could create a dynamically allocated array of buttons here
    # Make sure the button stores the id of the politician so it can be called by createProfile
    # Have there be a call to a method in util.py: createProfile(json, id, name) when a name is clicked on
    # id is the variable id at the top of each section in the json, it's unique to each official
    # Then there needs to be some type of input bar, scrollable selector, or smth which allows for the input of a daterange
    # Could create a separate method which creates this popup that displays necessary info from the politician as well as input spots
    # Maybe not something to be done tn, but possibly make it so that the pop ups can be closed


def month_slider_action(state, var_name, value):
    pass

def house_on_button_action(id):
    id = id
    print(id)


def pullUpProfile(id):
    return createProfile()


def get_data(path: str, id):
    dataset = pd.read_json(path)
    for item in dataset:
        if id == None:
            break
    dataset["first_name"]
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
    Gui(pages=pages).run(title='Sherwood Visualization Tool',
                         dark_mode=True,
                         use_reloader=True)
