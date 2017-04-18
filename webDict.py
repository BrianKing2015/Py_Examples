#!/usr/bin/python

import re
import pandas as pd
import pickle
from collections import Counter


with open ('/home/brian/Documents/29765-8.txt', 'r') as f:
	webDict = f.read()

words = re.findall(r"(^[A-Z]{3}.*)", webDict[5668:28911300], flags = re.M)
data = re.split (r"(^[A-Z]{3}.*)", webDict[5668:28911300], flags = re.M)
etymPattern = re.compile(r'Etym: ')


word = []
etym = []
#partOfSpeech = []

validEtym = ['L.','F.', 'Cf', 'Gr', 'OE', 'Pr', 'Se', 'NL', 'Fr', 'OF', 'AS', 'LL','It', 'Sp', 'He', 'Na', 'Co', 'Fo', 'Pe', 'G.', 'D.']

# for i in range (len(words)):
# 	word.append (words[i])
# 	temp =(re.split (etymPattern,data[i]))
# 	try:
# 		if temp[1][1:3] != None: #in validEtym:
# 			etym.append(temp[1][1:3])
# 		else:
# 			etym.append ("Not Available")

# 	except IndexError:
# 		etym.append("Not Available")

count = 1
for i in range ((len (data)/2)):
	tempE = (re.split(etymPattern,data[count+1]))
	
	try:
		if tempE[1][1:3] != None:
			word.append(data[count].strip().lower())
			etym.append(tempE[1][1:3])
			#partOfSpeech.append()
			count = count +2 
		else:
			word.append(data[count].strip().lower())
			etym.append("Not Available")
			count = count +2 
	except IndexError:
			word.append(data[count].strip().lower())
			etym.append("Not Available")
			count = count +2 
		

webster = pd.DataFrame ({'Word':word, 'Origin':etym})

pickle.dump(webster, open("webD.p", "wb"))

def countThings(target):
	counts = Counter(target)
	return counts

def checkEtym(target):
	wordOrigin = webster.loc[(webster['Origin']== target)]
	return wordOrigin

def wOrigin(target):
	wOrigin = webster.loc[(webster['Word']== target)]
	return wOrigin


# 23736

"""
L. = Latin
F. = French
Cf = 

536682024
9A29-6A6F
514-287-1166

"""