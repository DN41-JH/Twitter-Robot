import tweepy # Please make sure to install tweepy before running the program
import time

print("This is my automatically replying Twitter robot")

API_KEY = '' # Please enter your Twitter account's developer API key here
API_SECRET = '' # Please enter your Twitter account's developer API key secret here
ACCESS_TOKEN = '' # Please enter your Twitter account's developer access token here
ACCESS_SECRET = '' # Please enter your Twitter account's access token secret here

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt' # The file that stores the message id after which we start to consider auto-replying

def retrieve_last_seen_id(file_name): # The function that reads the last_seen_id.txt file and returns the last_seen_id (None if empty file)
	f_read = open(file_name, 'r')

	try:
		last_seen_id = int(f_read.read().strip())
		f_read.close()
		return last_seen_id
	except:
		f_read.close()
		return None

def store_last_seen_id(last_seen_id, file_name): # The function that stores the latest scanned message id into the file
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return


def automatic_reply(): # The main function that sets up the automatical reply
	last_seen_id = retrieve_last_seen_id(FILE_NAME)

	if last_seen_id is not None:
		mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended') # Retrieve the information of messages after the latest scanned message
	else:
		mentions = api.mentions_timeline() # Else retrieve the information of all the messages in the history


	for mention in reversed(mentions):
		print("New Message: " + str(mention.id) + " --- " + mention.full_text)

		last_seen_id = mention.id # update the latest scanned message id 
		store_last_seen_id(last_seen_id, FILE_NAME) # store the latest scanned message id 

		#api.update_status('@' + mention.user.screen_name + ' This is for universal replying', mention.id)

		### Below specifies what messages to reply and how to reply
		if 'dinner' in mention.full_text.lower() or 'lunch' in mention.full_text.lower():
			print("Found Food")
			print("responding back...")
			api.update_status('@' + mention.user.screen_name + ' Food? Lets GO!', mention.id)
		elif '?' in mention.full_text.lower(): 
			print("Found ?")
			print("responding back...")
			api.update_status('@' + mention.user.screen_name + ' Sorry I am currently busy, will get back to you soon', mention.id)


### Execute the auto-reply function infinitely, till the program is terminated 
while True:
	automatic_reply()
	time.sleep(10)