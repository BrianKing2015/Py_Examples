#!/usr/bin/env python

"""
A simple helper utility for parsing files, currently set-up to run from the command line interface.


Example:
This is an extremely simple parsing function that looks for specific words within whatever text is provided.
Example usage from CLI:
	python ParseUtility.py randomLog.txt errorText

TODO:
   * Encase the argparse in a function so file can be import into other projects

"""

import argparse

parser = argparse.ArgumentParser(description = "Parse a file line by line and return lines that contain a certain word.")
parser.add_argument('filename')
parser.add_argument('targetText')
try:
	args = parser.parse_args()
except Exception :
	print ('Please input a valid file and a word to parse for.')



def parseU(file, target):
	"""
	Returns all lines in a given file that contain the target word or any portion of that word.
	Data type for the return is a list of strings.
	Example:
	parseU ("randomLog.txt", "errorText")
	"""
	pLines = []
	with open(file, 'r') as f:
		readIn = f.readlines()
	for i in readIn:
		if target in i:
			pLines.append(i)

	return pLines

if __name__ == "__main__":
	print (parseU(args.filename, args.targetText))