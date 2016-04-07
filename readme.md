Sample matplotlib output data:
![primary sample 1](https://github.com/markedwinharvey/primary/blob/master/media/analyze.avgs.png)
![primary sample 2](https://github.com/markedwinharvey/primary/blob/master/media/journal_timelines.png)

`primary.py` uses the requests module to scrape US presidential candidates' names from 
news and politics sites listed in `news_sites.txt`, compared against names in `names.txt`. The 
data is automatically saved in a csv-formatted file as 'dat2_'+current date/time, with optional note
to add per data set. 

The program is currently set to run every four hours. 

All markup data (html invisible to casual user) and script data is removed prior to name parsing. Inclusion of 
markup data artificially inflates the results in terms of words visible/invisible to the user. 
On the other hand, some sites load content dynamically, so the results are only an estimate of the relative
proportion of names in the data. 

But some might say that a picture is worth a thousand trumps. ...So even including the markup/script data 
(which has a noticeable effect on the results)
is arguably something
of an understatement of the percent content devoted to particular candidates
(perhaps pixel count should factor in). 
In any case, the true number of trumps per front page news (total html content) can be calculated
by eliminating/commenting the area in the code where the website data is shrunk (i.e., function `remove_markup` in 
`primary.py`).

`primary2.py` offers to open a selection of the available data and displays the selected data as a 
mini ascii spreadsheet. 

`analyze.py` is a work in progress script to refine and visualize the data. The script uses matplotlib and numpy
to assist in these efforts. Currently, average candidate data per query (over all journals) is visualized, 
as well as the breakdown of results from each journal, plotted over time. 