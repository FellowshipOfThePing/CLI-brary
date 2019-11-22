import os
import argparse
import sys
import re


#Checks for regex pattern, and numbers files according to convention 01.filename, 02.filename, etc.
def number(files):
	numPattern = re.compile(r'\d\d\.\s')
	i = 1
	for filename in files:
		if (numPattern.search(filename[:4]) and i < 10):
			os.rename(filename, "0" + str(i) + ". " + filename[4:])
		elif (numPattern.search(filename[:4]) and i > 10):
			os.rename(filename, str(i) + ". " + filename[4:])
		elif i < 10:
			os.rename(filename, "0" + str(i) + ". " + filename)
		else:
			os.rename(filename, str(i) + ". " + filename)
		i += 1


#Check for regex pattern and undoes numbering
def undo():			
	numPattern = re.compile(r'\d\d\.\s')
	i = 1
	for filename in os.listdir("."):
		if numPattern.search(filename[:4]):
			os.rename(filename, filename[4:])



# Numbering Patterns/Options

#DEFAULT - AS IS
if len(sys.argv) == 1:		
	number(os.listdir("."))

#ALPHA
elif sys.argv[1] == '-a':	
	fileList = sorted(os.listdir("."), key=str.lower)
	number(fileList)

#REVERSE ALPHA
elif sys.argv[1] == '-r':	
	fileList = sorted(os.listdir("."), key=str.lower, reverse=True)
	number(fileList)

#UNDO
elif sys.argv[1] == '-u':	
	undo()

else:
	print('ERROR: Please enter valid option')

