#!/usr/bin/env python
#file:primary2.py
import json,subprocess
def main():
	with open('names.txt','r') as f:
		names = f.read().split('\n')
	print names
	options = subprocess.Popen(['ls data_*'],stdout=subprocess.PIPE,shell=True).communicate()[0].split()
	for i in range(len(options)):
		print i,options[i]
	selection = 0
	#'''
	selection = ''
	while not (selection in range(0,len(options))):
		selection = raw_input('Select data entry: ')
		try:
			selection = int(selection)
		except:
			print '  *not a number*'
	#'''
	with open(options[selection],'r') as f:
		data = json.loads(f.read())
	print '                             clinton  sanders   trump     cruz    kasich'
	for i in sorted(data):
		print i,(30-len(i))*' ',data[i]['names'][0][1],(7-len(str(data[i]['names'][0][1])))*' ',data[i]['names'][1][1],(7-len(str(data[i]['names'][1][1])))*' ',data[i]['names'][2][1],(7-len(str(data[i]['names'][2][1])))*' ',data[i]['names'][3][1],(7-len(str(data[i]['names'][3][1])))*' ',data[i]['names'][4][1]
	
	
	
	#print options
if __name__ == '__main__':
	main()