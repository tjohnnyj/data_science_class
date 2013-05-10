import json
import sys

afinnfile = open(sys.argv[1],"r")
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
			return sum(this_word_score)
		else:
			this_word_score = 0
			return this_word_score

def process_file(file):
	response = open(file,"r")
	str = []
	for item in response:
	#	list = item
		str.append(item)
	big_list ={}
	i=0
	for item in str:
		big_list[i] = json.loads(item)
		if "delete" in big_list[i].keys():
			sentiment = 0
			print sentiment
			i+=1
		else:
			this_tweet = big_list[i]["text"].split()
			sentiment = check_twit(this_tweet)
			print sentiment
			i+=1
	response.close()


process_file(sys.argv[2])	

#print str
#print type(str)
#try_this = json.load(str)
	
#print type(response)