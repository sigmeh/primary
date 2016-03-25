#!/usr/bin/env python
#file:primary2.py
import json,subprocess
def main():
	options = subprocess.Popen(['ls data_*'],stdout=subprocess.PIPE,shell=True).communicate()[0].split()
	for i in range(len(options)):
		print i,options[i]

	selection = ''
	while not (selection in range(0,len(options))):
		selection = raw_input('Select data entry: ')
		try:
			selection = int(selection)
		except:
			print '  *not a number*'
			
	with open('names.txt','r') as f:
		names = f.read().split('\n')
	with open(options[selection],'r') as f:
		data = json.loads(f.read())

	if 'note' in data:
		note = data['note']
		del data['note']
	else:
		note = 'no note found'
	
	
	print len(data)
	print ' '*26,
	for name in names:
		print (6-len(name))*' ',
		print name,
		if len(name) <5:
			print ' ',	
	print
	for i in sorted(data):
		print i,(28-len(i))*' ',#data[i]['names'][0][1],
		#print 'good','i:',i
		for j in data[i]['names']:
			#print 'not good'
			print j[1],(7-len(str(j[1])))*' ',			
		print
	print ' data from file:',options[selection]
	print ' ## note:',note
		
if __name__ == '__main__':
	main()