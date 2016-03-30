#!/usr/bin/env python
'''	primary.py scrapes candidate name data from several news sources for frequency analysis'''
import requests,subprocess,time
from datetime import datetime

#excise contents of script tags and remove markup
def remove_markup(r):
	start=0
	while start != -1:
		start=r.find('<script')					#remove all script data
		end=r.find('</script>',start)
		if start == -1 or end == -1:
			break
		r=r[:start]+r[end+9:]
	start=0
	while start != -1:
		start=r.find('<')						#remove all markup (invisible to user)
		end=r.find('>',start)
		if start == -1 or end == -1:
			break
		r=r[:start]+r[end+1:]
	return r

#compile data by iteration over site list
def get_site_data(names_,sites):
		app_start = time.time()
		results={}
		for site in sorted(sites.iteritems()):
			names = [[name,0] for name in names_]
			r = requests.get(site[1]).text.encode('unicode-escape')
			r = remove_markup(r).lower().replace('\\n','').split()
	
			for name in range(len(names)):
				for word in r:
					if names[name][0] in word:
						names[name][1] += 1
			results[site[0]] = {'url':site[1],'names':names,'time':str(datetime.now())}
		print 'Completed in:',int(100*(time.time()-app_start))/100.,'s'	
		return results

#save results as csv file
def save_results(names_,results):
		note='add epoch time, four-hour increment test'		#can add raw_input for note following query
		if note:
			results['note'] = note
		else:
			results['note'] = 'no note'
		new_doc = []
		for journal in results.iterkeys():
			if journal != 'note':
				new_doc.append(str(journal)+','+','.join([str(x[1]) for x in results[journal]['names']]))
		time_now = str(datetime.now()).split('.')[0].replace(' ','_')
		new_doc = '\n'.join([','.join(names_)]+sorted(new_doc)+['#collected,'+time_now+',since_epoch,'+str(time.time())]+['#note,'+note])
		with open('data/dat2_'+time_now,'w') as f:
			f.write(new_doc)
		return new_doc

#display newest results (formatted for viewing)
def display_results(names_,results):	
	data = [x.split(',') for x in results.split('\n')]
	print ' '*26,
	for name in names_:
		print (6-len(name))*' ',
		print name,
		if len(name) <5:
			print ' ',	
	print
	for line in data[1:]:
		print line[0],(28-len(line[0]))*' ',	
		for word in line[1:]:
			print word,(7-len(word))*' ',
		print	

#main 
def main():
	with open('news_sites.txt','r') as f:			#get saved news source url data
		n_sites = f.read().split('\n')
	sites = {n_sites[i]:n_sites[i+1] for i in range(0,len(n_sites),2)}

	with open('names.txt','r') as f:				#get saved name data
		names_ = f.read().split('\n')
	
	#get site data and save results
	print 'Tabulating results...'
	while 1:
		results = get_site_data(names_,sites)
		results = save_results(names_,results)
		display_results(names_,results)
		time.sleep(60*60*4)							#current setting to collect data every 4 hours
	
if __name__ == '__main__':
	main()