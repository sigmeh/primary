#!/usr/bin/env python
#file:primary2.py
'''	view time-point data from primary.py as simple ascii spreadsheet
	i.e., number of appearances per candidate per publication at selected time'''
import subprocess
def main():
	options = subprocess.Popen(['ls data/dat2_*'],stdout=subprocess.PIPE,shell=True).communicate()[0].split()
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
		data = [x.split(',') for x in f.read().split('\n')]
	
	print ' '*26,
	for name in names:
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

if __name__ == '__main__':
	main()