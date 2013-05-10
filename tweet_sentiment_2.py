import json
import sys

afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.


def check_twit(chars):
	this_word_score = []
	for word in chars:
		if word in scores:
#			print word + " " + str(scores[word])
			this_word_score.append(scores[word])
#			print this_word_score
			print sum(this_word_score)
		else:
			return 0

def process_file(file):
	response = open(file,"r+")
	str = []
	for item in response:
	#	list = item
		str.append(item)
	#print str[5]
	big_list ={}
	#for i in range(0,len(str)):
	i=0
	for item in str:
		big_list[i] = json.loads(item)
		if "delete" in big_list[i].keys():
			print 0
			i+=1
		else: 
			this_tweet = big_list[i]["text"].split()
			print check_twit(this_tweet)
			i+=1

print process_file(sys.argv[2])	

#print str
#print type(str)
#try_this = json.load(str)
	
#print type(response)