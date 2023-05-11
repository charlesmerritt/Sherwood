from taipy.gui import Markdown

Senate = Markdown("""
##### Select a state to view data for senators from that state.
<|layout|columns=1 3|
<|States|expandable|
<|Alabama|button|on_action={senator_state_clicked}|id=AL|>
<|Alaska|button|on_action={senator_state_clicked}|id=AK|>
<|Arizona|button|on_action={senator_state_clicked}|id=AZ|>
<|Arkansas|button|on_action={senator_state_clicked}|id=AR|>
<|California|button|on_action={senator_state_clicked}|id=CA|>
<|Colorado|button|on_action={senator_state_clicked}|id=CO|>
<|Connecticut|button|on_action={senator_state_clicked}|id=CT|>
<|Delaware|button|on_action={senator_state_clicked}|id=DE|>
<|Florida|button|on_action={senator_state_clicked}|id=FL|>
<|Georgia|button|on_action={senator_state_clicked}|id=GA|>
<|Hawaii|button|on_action={senator_state_clicked}|id=HI|>
<|Idaho|button|on_action={senator_state_clicked}|id=ID|>
<|Illinois|button|on_action={senator_state_clicked}|id=IL|>
<|Indiana|button|on_action={senator_state_clicked}|id=IN|>
<|Iowa|button|on_action={senator_state_clicked}|id=IA|>
<|Kansas|button|on_action={senator_state_clicked}|id=KS|>
<|Kentucky|button|on_action={senator_state_clicked}|id=KY|>
<|Louisiana|button|on_action={senator_state_clicked}|id=LA|>
<|Maine|button|on_action={senator_state_clicked}|id=ME|>
<|Maryland|button|on_action={senator_state_clicked}|id=MD|>
<|Massachusetts|button|on_action={senator_state_clicked}|id=MA|>
<|Michigan|button|on_action={senator_state_clicked}|id=MI|>
<|Minnesota|button|on_action={senator_state_clicked}|id=MN|>
<|Mississippi|button|on_action={senator_state_clicked}|id=MS|>
<|Missouri|button|on_action={senator_state_clicked}|id=MO|>
<|Montana|button|on_action={senator_state_clicked}|id=MT|>
<|Nebraska|button|on_action={senator_state_clicked}|id=NE|>
<|Nevada|button|on_action={senator_state_clicked}|id=NV|>
<|New Hampshire|button|on_action={senator_state_clicked}|id=NH|>
<|New Jersey|button|on_action={senator_state_clicked}|id=NJ|>
<|New Mexico|button|on_action={senator_state_clicked}|id=NM|>
<|New York|button|on_action={senator_state_clicked}|id=NY|>
<|North Carolina|button|on_action={senator_state_clicked}|id=NC|>
<|North Dakota|button|on_action={senator_state_clicked}|id=ND|>
<|Ohio|button|on_action={senator_state_clicked}|id=OH|>
<|Oklahoma|button|on_action={senator_state_clicked}|id=OK|>
<|Oregon|button|on_action={senator_state_clicked}|id=OR|>
<|Pennsylvania|button|on_action={senator_state_clicked}|id=PA|>
<|Rhode Island|button|on_action={senator_state_clicked}|id=RI|>
<|South Carolina|button|on_action={senator_state_clicked}|id=SC|>
<|South Dakota|button|on_action={senator_state_clicked}|id=SD|>
<|Tennessee|button|on_action={senator_state_clicked}|id=TN|>
<|Texas|button|on_action={senator_state_clicked}|id=TX|>
<|Utah|button|on_action={senator_state_clicked}|id=UT|>
<|Vermont|button|on_action={senator_state_clicked}|id=VT|>
<|Virginia|button|on_action={senator_state_clicked}|id=VA|>
<|Washington|button|on_action={senator_state_clicked}|id=WA|>
<|West Virginia|button|on_action={senator_state_clicked}|id=WV|>
<|Wisconsin|button|on_action={senator_state_clicked}|id=WI|>
<|Wyoming|button|on_action={senator_state_clicked}|id=WY|>
|>

<|Expand|button|on_action=toggle_sidebar|>
<|{show}|pane|persistent|anchor=right|on_close=toggle_sidebar|width=600px|partial={members}|>


|>
""")
