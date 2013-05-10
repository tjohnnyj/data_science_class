import urllib
import json

#response = urllib.urlopen("http://search.twitter.com/search.json?q=happy")
#pyresponse =  json.load(response)
#print type(pyresponse)
#print pyresponse.keys()
#resultset = pyresponse["results"]
#tweeter =  resultset[0]["text"]
#twit =  tweeter.split()
#print type(twit)
afinnfile = open("AFINN-111.txt")
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
			print this_word_score
			print sum(this_word_score)	
		
	
response = open("output.json","r+")
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
		print "calling check_twit"
		check_twit(big_list[i]["text"])
		i+=1


#print scores.items() # Print every (term, score) pair in the dictionary

