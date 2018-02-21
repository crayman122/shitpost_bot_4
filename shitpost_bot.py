#Made by Red in 2017
#https://reddragonte.ch/
#Greetings from Cleveland!

# This code is really broke, so you better stay woke.
# This code is really bad so please dont contact me if you dont understand it.
# Good luck.

import twitter #Needed for interacting with twitter
import random #Needed to pick randoms
import time #Schedule tasks
import linecache #Random access to external files

#Define constants needed
# (Remove before flight)
consumer_key = <Put your Consumer Key Here>

consumer_secret = <Put your Consumer Secret Here>

access_key = <Put your Access Key Here>

access_secret = <Put you Access Secret Here>

#Define names opf files used to create robot

blanks_list = 'blanks.txt'

question_list = 'questions.txt'

mentions_list = 'mentions.txt'

hashtag_list = 'hashtags.txt'

#Really really ineffient way to get the length of each file. Causes issues sometimes.

blanks_list_len = len(open(blanks_list).readlines())

questions_list_len = len(open(question_list).readlines())

mentions_list_len = len(open(mentions_list).readlines())

hashtag_list_len = len(open(hashtag_list).readlines())


#here we login to twitter. The only part of the code that doesn't suck.
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_key,
                  access_token_secret=access_secret)


#I hate myself for writing this. I'm sorry. 
def tweetContent():
	#Chooses what the tweet will contain
	#Returns a dict with the information
	tweetInfo = {'image' : False, 'onlyblank' : False, 'containsmention' : False, 'containshashtag' : False, 'containstext' : True} #Define default content. Some of these parts are unused. Was gonna add more, but never did, this project is abandoned.
	infoImage = random.randint(1,50) #Part of the code that doesn't do anything. 
	if infoImage == random.randint(1,50): #Generate a random number for some reason.
		tweetInfo['image'] = True #Still unused stuff 
		onlyImage = random.randint(1, 10) #not used
		if  onlyImage == random.randint(1, 10): #still not used, i still hate myself
			tweetInfo['containstext'] = False #not used but still important I guess
			return tweetInfo #Early return. 
	
	#Is it only a blank or is it the full tweet
	infoBlank = random.randint(1,2)
	if infoBlank == random.randint(1,2):
		tweetInfo['onlyblank'] = True
	
	#Does the tweet contain a mention? It's probabaly @realDonaldTrump or @CNN
	infoMention = random.randint(1, 10)
	if infoMention == random.randint(1, 10):
		tweetInfo['containsmention'] = True
		
	#Does the tweet contain a hashtag? #vapenation
	infoHashtag = random.randint(1, 10)
	if infoHashtag == random.randint(1, 10):
		tweetInfo['containshashtag'] = True
	
	return tweetInfo #Return info dict




#Posts the tweet.
def post(text):
	#Is the tweeet longer than 280 characters (Maximum as of 2018)
	if len(text) > 280:
		return 1 #If more than 280, it will regenerate tweet. Possible to create an infinite loop.
	else:
		status = api.PostUpdate(text)
		return 0 #If sucessfully posted, program will go to sleep.

def fillBlanks(tweet):
	#inefficient way to fill the blanks.
	if tweet.count("%s") == 0:
		#fill zero blanks ( Speaking of zeros Arrays fucking start at zero).
		return tweet
	elif tweet.count("%s") == 1:
		#Fill one blank
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	elif tweet.count("%s") == 2:
		#Fill two blanks
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	elif tweet.count("%s") == 3:
		#Fill 3 blanks
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	elif tweet.count("%s") == 4:
		#Fill 4 blanks.
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	#There should not be more than 4 blanks. If there is, the program will crash.
	else:
		return tweet



def generate():
	#Builds a template for the tweet.
	info = tweetContent() #Generate content dict.
	tweet = '' #Blank tweet.
	if info['containstext'] == False:
		#I told you it was unused.
		pass
	elif info['image'] == True:
		#so is this
		pass
	if info['onlyblank'] == True:
		#is the tweet only a blank, if so, add the blank
		tweet += linecache.getline(blanks_list, random.randint(0, blanks_list_len))
	else:
		#add the template and then fill the blanks
		tweet += linecache.getline(question_list, random.randint(0, questions_list_len))
		tweet = fillBlanks(tweet)
	if info['containshashtag'] == True:
		#add a hashtag if needed
		tweet += linecache.getline(hashtag_list, random.randint(0, hashtag_list_len))
	if info['containsmention'] == True:
		#add a mention if needed.
		tweet += linecache.getline(mentions_list, random.randint(0, mentions_list_len))
	return tweet

while True:
	# wait for the hour.
	if int(time.strftime("%M", time.gmtime())) == 0:
		tweet = generate()
		print tweet
		post(tweet) #Post the tweet.
		time.sleep(60000) #Used to prevent the program from using 100% CPU and bricking an entire server.
	
