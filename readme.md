<h4>primary</h4>



Sample matplotlib output data:
![primary sample 1](https://github.com/markedwinharvey/primary/blob/master/media/primary_2016-08-04_16:02:12.png)
![primary sample 2](https://github.com/markedwinharvey/primary/blob/master/media/jt_2016-08-04_16:02:07.png)


<h5>primary.py</h5>

<h6>Usage:</h6>

	python primary.py

Scrape US presidential candidates' names from news sources (news_sites.txt), compared against names in names.txt. 
Data is auto-saved in time-stamped csv format. 

The program is set to collect every 4 hours. 

All markup text is removed prior to name parsing (markup text, invisible to casual users, artificially inflates results). 

<h5>analyze.py</h5>

<h6>Usage:</h6>

	python analyze.py
	

Visualize the available data (numpy/matplotlib):<br>
<ul>
raw totals<br>
average percents<br>
linear regression<br>
simple moving averages<br>
cumulative moving averages<br>
color charts of total data spread<br>
</ul>