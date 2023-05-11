from datetime import datetime
import time
from taipy.gui import Gui
from congress import CongressMembers
from pages.house import House
from pages.senate import Senate
from util import get_members, pull_house_data, pull_senate_data
from charts import Visualizations

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

show = True
logo = "img/arrow.png"
start_dt = datetime.fromtimestamp(time.time())
end_dt = datetime.fromtimestamp(time.time())

congress_list: list[CongressMembers] = []
selected_congress: CongressMembers = None
charts_list: list[Visualizations] = []
# data =

def senator_state_clicked(state, id):
    state.congress_list = get_members(id, False)


def house_state_clicked(state, id):
    state.congress_list = get_members(id, True)


def toggle_sidebar(state):
    state.show = not state.show


def filter_by_date_range(dataset, start_date, end_date):
    mask = (dataset['Date'] > start_date) & (dataset['Date'] <= end_date)


def on_change(state):
    print(state.start_dt)


pages = {
    "/": root,
    "Home": Home,
    "House": House,
    "Senate": Senate
}

gui = Gui(pages=pages)
members = gui.add_partial("""
<|Congress Members|expandable|
<|{selected_congress}|selector|lov={congress_list}|type=CongressMembers|adapter={lambda c: (c.id, c.name)}|>
|>

<|Visualization Options|expandable|
<|start date|text|><|{start_dt}|date|not with_time|> <|end date|text|> <|{end_dt}|date|not with_time|>
<|Select Visualization|selector|lov={charts}|type=VisualizationType|>
|>
""")

visualizer = gui.add_partial("""
<|Visualizer|expandable|>
""")

gui.run(title='Sherwood Visualization Tool',
                         dark_mode=True,
                         use_reloader=True)
