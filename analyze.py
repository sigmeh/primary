#!/usr/bin/env python
#file:a3.py
import subprocess, matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def journal_timelines_maker(journal_timelines,this_data):
	for row in this_data:
		row_nums = [float(x) for x in row[1:]]
		if sum(row_nums):												#avoid division by zero if zero name occurrences
			row_nums = [int(1000.*x/sum(row_nums))/10. for x in row_nums]		
		if not len(journal_timelines[row[0]]):			
			journal_timelines[row[0]] = np.array([row_nums])							#not populated, initialize array			
		else:
			journal_timelines[row[0]] = np.vstack([journal_timelines[row[0]],row_nums])	#found populated, stack new row
	return journal_timelines

def graph_journal_timelines(journal_timelines,num_files):
	for journal in journal_timelines.iterkeys():
		plt.scatter(range(num_files),journal_timelines[journal][:,0],color='red',alpha=.15)
		plt.scatter(range(num_files),journal_timelines[journal][:,1],color='green',alpha=.15)
		plt.scatter(range(num_files),journal_timelines[journal][:,2],color='blue',alpha=.15)
		plt.scatter(range(num_files),journal_timelines[journal][:,3],color='yellow',alpha=.15)
		plt.scatter(range(num_files),journal_timelines[journal][:,4],color='orange',alpha=.15)
	plt.show()

def main():
	#open relevant files and append each data-set to data_sets
	files = subprocess.Popen(['ls data'],stdout=subprocess.PIPE,shell=True).communicate()[0].split('\n')
	files = [x for x in files if x[:4] == 'dat2']
	num_files = len(files)
	data_sets = []
	for file in files:	
		with open('data/'+file,'r') as f:
			data_sets.append(f.read())	
	
	#define some things
	curr_cand = 'clinton sanders trump cruz kasich'.split(' ')
	with open('news_sites.txt','r') as f:
		journals = f.read().split('\n')[::2]
	journal_timelines = {journal:np.array([]) for journal in journals}
	coll_totals = []
	coll_percents = []
	
	for data in data_sets:
		this_data = np.array([x.split(',')[0:6] for x in data.split('\n')[1:-2]])	
			#parse each data set
		journal_timelines = journal_timelines_maker(journal_timelines,this_data)
			#add each data set to journal-dependent timeline
		this_data = this_data[:,1:].astype('i1')			
			#remove journal label and convert to integer matrix
		single_coll_total = [sum(this_data[:,x]) for x in range(len(curr_cand))]
		coll_totals.append(single_coll_total)				#total mentions for each candidate in all journals per query

	graph_journal_timelines(journal_timelines,num_files)
		#graph journal-dependent data
	
	for i in coll_totals:
		all_cand_sum = sum(i)
		coll_percents.append([int(1000.*x/all_cand_sum)/10. for x in i])
	coll_percents = np.array(coll_percents)

	for i in  coll_percents:
		pass#print i	

	avg_percents = [int(10*sum(coll_percents[:,x])/num_files)/10. for x in range(5)]
	print np.array(avg_percents),'(avg)'
	
	#'''
	for cand in range(len(curr_cand)):
		plt.plot(range(len(files)),coll_percents[:,cand])
	plt.show()
	#'''

if __name__ == '__main__':
	main()