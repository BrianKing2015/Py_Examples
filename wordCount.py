"""
Simple example of how to get a word count out of a peice of text using TextBlob
"""

from textblob import TextBlob
import pandas as pd 



stop_words = set (['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for',
	'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
	'to', 'was', 'were', 'will', 'with'])



def checkText (text):
	wordList =[]
	wordCount = []

	with open (text) as f:
		content = f.read()

	blob = TextBlob(content)
	
	for i in (set (blob.words) -stop_words):
		wordList.append (i)

	for i in wordList:
		wordCount.append (blob.word_counts[i])


	wordFrame = pd.DataFrame({'Word': wordList, 'Occurences': wordCount })
	wordFrame = wordFrame.sort_values(by =['Occurences'], ascending =[False])

	return wordFrame
