"""
Simple example of how to get a word count out of a peice of text using TextBlob
"""

from textblob import TextBlob
import pandas as pd 
import matplotlib.pyplot as plt



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


def grabTags(text):

	with open (text) as f:
		content = f.read()

	blob = TextBlob (content)
	partTags = blob.tags
	words = pd.DataFrame(partTags)
	words.columns = ['words', 'tags']

	# From: http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
	adjective = ['JJ', 'JJR', 'JJS']
	adverb = ['RB', 'RBR', 'RBS']
	nouns = ['NN', 'NNS', 'NNP', 'NNPS']
	verbs = ['VB', 'VBG', 'VBG', 'VBN', 'VBP', 'VBZ']

	adj = words[words['tags'].isin(adjective)]
	adv = words[words['tags'].isin(adverb)]
	nou = words[words['tags'].isin(nouns)]
	ver = words[words['tags'].isin(verbs)]

	adj = adj['words'].value_counts()
	adv = adv['words'].value_counts() 
	nou = nou['words'].value_counts()
	ver = ver['words'].value_counts()

	return adj, adv, nou, ver

def grabValues(text):

	with open (text) as f:
		content = f.read()

	blob = TextBlob (content)
	partTags = blob.tags
	words = pd.DataFrame(partTags)
	words.columns = ['words', 'tags']

	# From: http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
	adjective = ['JJ', 'JJR', 'JJS']
	adverb = ['RB', 'RBR', 'RBS', 'WRB']
	conjunction = ['CC', 'IN']
	determiner = ['DT', 'PDT','WDT']
	nouns = ['NN', 'NNS', 'NNP', 'NNPS','WP', 'WP$']
	verbs = ['VB', 'VBG', 'VBG', 'VBN', 'VBP', 'VBZ']


	adj = words[words['tags'].isin(adjective)]
	adv = words[words['tags'].isin(adverb)]
	con = words[words['tags'].isin(conjunction)]
	det = words[words['tags'].isin(determiner)]
	nou = words[words['tags'].isin(nouns)]
	ver = words[words['tags'].isin(verbs)]


	adj = adj['words'].value_counts()
	adv = adv['words'].value_counts() 
	con = con['words'].value_counts()
	det = det['words'].value_counts()
	nou = nou['words'].value_counts()
	ver = ver['words'].value_counts()


	totalLen = words['tags'].value_counts().sum()
	adj = adj.sum()/totalLen
	adv = adv.sum()/totalLen
	con = con.sum()/totalLen
	det = det.sum()/totalLen
	nou = nou.sum()/totalLen
	ver = ver.sum()/totalLen


	valuesSeri = {'Adjectives':adj, 'Adverbs':adv, 'Conjunctions':con, 'Determiner':det,'Nouns':nou, 'Verbs':ver}

	seri = pd.Series(valuesSeri)
	seri.plot(kind='bar',stacked=True)
	plt.show()


	#return words #seri, adj, adv, nou, ver, totalLen



