import copy
import re
import nltk
import numpy as np
import time 
from HostileSet import *
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import kstest
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from multiprocessing import Pool
from multiprocessing import Process , Queue


def tokenize_only(text):
	# first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
	tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
	filtered_tokens = []
	# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
	for token in tokens:
		if re.search('[a-zA-Z]', token):
			filtered_tokens.append(token)
	return filtered_tokens

def fetch_tweets():
	f = open('KashmirTwitterData.txt', 'r')
	l = {}
	for line in f.readlines():
		try:
			_id = line.split('\t')[3].strip()
			twt = line.split('\t')[4].strip()
			l[_id]=twt

		except IndexError:
			continue

	f.close()
	return l

#This function removes the Unrelated tweets from the data set using TF/IDF. 
#It uses 1.5 IQR technique to identify the outliers and remove them from the data set. 
def removeTfIdf():
	arr1=[]	
	temp_sentences = []
	sentences = []
	l1={}
	newarr=[]
	nwarr=[]	
	scores = []

	for key, value in l.iteritems():	
		arr1.append(value)	
	
	for i in arr1:

		if len(i) > 20:
			sentences.append(i)

	#define vectorizer parameters
	tfidf_vectorizer = TfidfVectorizer(max_df=0.93, max_features=200000, min_df=0.07, stop_words='english', use_idf=True, tokenizer=tokenize_only, ngram_range=(1,5))
	tfidf_matrix = tfidf_vectorizer.fit_transform(sentences) #fit the vectorizer to articles

	terms = tfidf_vectorizer.get_feature_names()
	#get the distance between the articles
	dist = 1 - cosine_similarity(tfidf_matrix)

	for i in range(len(sentences)):
		scores.append(sum(dist[i], 0.0) / (len(dist[i])))

	arr = copy.deepcopy(scores)
	arr = np.array(arr)
	iqr = np.percentile(arr, 75, interpolation= 'higher') - np.percentile(arr, 25, interpolation= 'lower')
	f = open("tf-idf distribution.txt", "w")
	n = len(scores)

	for i in range(n):
		f.write(str(scores[i]))
		f.write("\n")

	mean_dist = sum(scores)/n
	uppr=mean_dist - (1.5*iqr)
	lwr=mean_dist + (1.5*iqr)

	for ele in range(len(arr)):
		if arr[ele]<uppr or arr[ele]>lwr:
			newarr.append(ele)
	
	for ele1 in newarr:
		nwarr.append(arr1[ele1])

	for key, value in l.iteritems():	
		if value in nwarr:
			pass;
		else:
			l1[key]=value
	return l1

# Hostility Factor is the ratio of number of hostile words to total number of words in given sentence, in this case a tweet.
def hostilityfactor(x):
	count=0;
	for i in x:	
		if i.upper() in hostile: 
			count+=1		
	for i in x:		
		if i.lower() in stop:
			x.remove(i)	
	for i in x:		
		if i.lower() == "":
			x.remove(i)	
	frac = float(count)/float(len(x))
	return frac	

# This function extracts the top 0.05 percentage of most hostile tweets from the data set.
def Hostile():
	hos=[]
	top=0;

	for y in arr1:
		y=y.split(' ')
		red=hostilityfactor(y)
		hos.append(red)
		top+=1;
	top =top * 0.005
	print top
	li=[]
	for i in range(int(top)+1): 
		li.append(hos.index(max(hos)))
		hos[hos.index(max(hos))]=0.0	
	q1.put(li)

def Senti():
	sentences = []
	sentences_string = ""

	sid = SentimentIntensityAnalyzer()

	for i in arr1:
		sentences.append(i)
		
	sentiments = [None] * len(sentences)

	for i in range(len(sentences)):
		sentiments[i] = sid.polarity_scores(sentences[i])["compound"]

	#most negative
	print(sentences[ sentiments.index(sorted(sentiments)[0])] , sorted(sentiments)[0])
	print "-----------------------------------"
	#most positive
	print(sentences[ sentiments.index(sorted(sentiments)[len(sentiments)-1])], sorted(sentiments)[len(sentiments)-1])
	

if __name__=='__main__':			
	t0=time.clock()
	l = fetch_tweets()
	l2 = removeTfIdf()
	arr1=[]	
	q1=Queue()

	for key, value in l.iteritems():	
		arr1.append(value)	
		
	stop = set(stopwords.words('english'))
	
	p = Process(target=Hostile,args=())
	p.start()
	q = Process(target=Senti,args=())
	q.start()
	l3=q1.get()
	# l3=Hostile()
	# sid = SentimentIntensityAnalyzer()

	print "Most hostile Tweets"
	
	q.join()
	p.join()
	
	for x in l3:
		print(arr1[x]+"\n")
		print("----------------------------------------------------------")

	t1=time.clock()
	print(t1-t0)