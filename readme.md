`primary.py` uses the requests module to scrape US presidential candidates' names from 
news and politics sites listed in `news_sites.txt`, compared against names in `names.txt`. The 
data is automatically saved to a json-encoded file as 'data_'+current date/time, with optional note
to add per data set. 
All markup data (html invisible to casual user) and script data is removed prior to name lookup. Inclusion of 
markup data artificially inflates the results in terms of words visible/invisible to the user. On the other 
hand, it is said that a picture is worth a thousand trumps. ...So even including the markup data is arguably something
of an understatement of the percent content devoted to particular candidates (perhaps pixel count should factor in). 
In any case, the true number of trumps per front page news (total html content) can be calculated
by eliminating/commenting the area in the code where the website data is shrunk (i.e., function `remove_markup` in 
`primary.py`).

`primary2.py` offers to open a selection of the available data and displays the selected data as a 
mini ascii spreadsheet. 