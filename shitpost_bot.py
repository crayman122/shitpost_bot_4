import twitter
import random
import time
import linecache

consumer_key = "SDjh70TQSJCy84hzYUtlG1Rse"

consumer_secret = "XW6ZXidtjRu3DcFA9L1ViLWSlOz3UUmctQy64ujD9UKkhred78"

access_key = "836955760177393665-CcrxT5uqFoaH81CS3kCBRAHdEE86W8P"

access_secret = "MvaKv7eF2xTy5HFmkQDT2fvd8rGTuimbWmwerK0M2uYPH"

blanks_list = 'blanks.txt'

question_list = 'questions.txt'

mentions_list = 'mentions.txt'

hashtag_list = 'hashtags.txt'

blanks_list_len = len(open(blanks_list).readlines())

questions_list_len = len(open(question_list).readlines())

mentions_list_len = len(open(mentions_list).readlines())

hashtag_list_len = len(open(hashtag_list).readlines())

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_key,
                  access_token_secret=access_secret)

def tweetContent():
	#Chooses what the tweet will contain
	#Returns a dict with the information
	tweetInfo = {'image' : False, 'onlyblank' : False, 'containsmention' : False, 'containshashtag' : False, 'containstext' : True}
	infoImage = random.randint(1,50)
	if infoImage == random.randint(1,50):
		tweetInfo['image'] = True
		onlyImage = random.randint(1, 10)
		if  onlyImage == random.randint(1, 10):
			tweetInfo['containstext'] = False
			return tweetInfo
	infoBlank = random.randint(1,2)
	if infoBlank == random.randint(1,2):
		tweetInfo['onlyblank'] = True
	infoMention = random.randint(1, 10)
	if infoMention == random.randint(1, 10):
		tweetInfo['containsmention'] = True
	infoHashtag = random.randint(1, 10)
	if infoHashtag == random.randint(1, 10):
		tweetInfo['containshashtag'] = True
	return tweetInfo




def post(text):
	if len(text) > 140:
		return 1
	else:
		status = api.PostUpdate(text)
		return 0

def fillBlanks(tweet):
	if tweet.count("%s") == 0:
		return tweet
	elif tweet.count("%s") == 1:
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	elif tweet.count("%s") == 2:
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	elif tweet.count("%s") == 3:
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	elif tweet.count("%s") == 4:
		tweet = str(tweet) % (linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)), linecache.getline(blanks_list, random.randint(0, blanks_list_len)))
		return tweet
	else:
		return tweet



def generate():
	info = tweetContent()
	tweet = ''
	if info['containstext'] == False:
		pass
	elif info['image'] == True:
		pass
	if info['onlyblank'] == True:
		tweet += linecache.getline(blanks_list, random.randint(0, blanks_list_len))
	else:
		tweet += linecache.getline(question_list, random.randint(0, questions_list_len))
		tweet = fillBlanks(tweet)
	if info['containshashtag'] == True:
		tweet += linecache.getline(hashtag_list, random.randint(0, hashtag_list_len))
	if info['containsmention'] == True:
		tweet += linecache.getline(mentions_list, random.randint(0, mentions_list_len))
	return tweet

while True:

	if int(time.strftime("%M", time.gmtime())) == 0:
		tweet = generate()
		print tweet
		post(tweet)
		time.sleep(60000)
	