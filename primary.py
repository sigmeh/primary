#!/usr/bin/env python
'''	frequency analysis from several news sites of selected 
	presidential candidates' names, current and former'''
import requests,subprocess
import time
from datetime import datetime
app_start = time.time()
current_time = datetime.now()

def remove_markup(r):
	#excise contents of script tags and remove markup
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

def main():
	with open('news_sites.txt','r') as f:	#get saved url data
		n_sites = f.read().split('\n')
	sites = {}
	for i in range(0,len(n_sites),2):
		sites[n_sites[i]] = n_sites[i+1]	
	with open('names.txt','r') as f:		#get saved pres. candidate data
		names_ = f.read().split('\n')
	
	results={}
	for site in sites.iteritems():
		names = [[name,0] for name in names_]
		r = requests.get(site[1]).text.encode('unicode-escape')
		r = remove_markup(r).lower().replace('\\n','').split()
	
		for name in range(len(names)):
			for word in r:
				if names[name][0] in word:
					names[name][1] += 1
		print site[0],names
		results[site[0]] = {'url':site[1],'names':names,'time':str(datetime.now())}
	print 'Completed in:',int(100*(time.time()-app_start))/100.,'s'	
	
	#data was previously json-serialized and saved here, but a 7-fold decrease in file 
	#size can be achieved by making a simple csv file, each of which still contains all relevant data
	note = raw_input('enter notes for this data: ')	
	if note:
		results['note'] = note
	else:
		results['note'] = 'no note'
	new_doc = []
	data = results
	for journal in data.iterkeys():
		if journal != 'note':
			new_doc.append(str(journal)+','+','.join([str(x[1]) for x in data[journal]['names']]))
	if not note:
		note = 'no note'
	time_now = str(datetime.now()).split('.')[0].replace(' ','_')
	new_doc = '\n'.join(['clinton,sanders,trump,cruz,kasich,rubio,carson,christie,bush,obama']+sorted(new_doc)+['#collected,'+time_now]+['#note,'+note])
	with open('data/dat2_'+time_now,'w') as f:
		f.write(new_doc)

if __name__ == '__main__':
	main()