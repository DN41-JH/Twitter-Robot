import tweepy
import time

print("This is my automatically replying Twitter robot")

API_KEY = '41JHa9mpYkeS0IyREeTQ9MKKZ'
API_SECRET = '9tJUqNisMaWocqIMKJPhjZ0T1gqfSXrvwC9TTp2LRKjVnbST6s'
ACCESS_TOKEN = '1355176972360495108-e6NdMoAObMtMifXnR3LtgLzzJ1iEJP'
ACCESS_SECRET = '6kVGz3Mv5OIW4Id9brBj7m8RdEw22QQNtXwkNgbNWhSNG'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')

	try:
		last_seen_id = int(f_read.read().strip())
		f_read.close()
		return last_seen_id
	except:
		f_read.close()
		return None

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def automatic_reply():
	last_seen_id = retrieve_last_seen_id(FILE_NAME)

	if last_seen_id is not None:
		mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
	else:
		mentions = api.mentions_timeline()

	for mention in reversed(mentions):
		print('New Messages: ' + str(mention.id) + " ---> " + mention.full_text)

		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)

		#api.update_status('@' + mention.user.screen_name + ' This is for universal replying', mention.id)

		if '?' in mention.full_text.lower():
			print("Found ?")
			print("responding back...")
			api.update_status('@' + mention.user.screen_name + ' Sorry I am currently busy, will get back to you soon', mention.id)
		elif 'dinner' in mention.full_text.lower() or 'lunch' in mention.full_text.lower():
			print("Found Food")
			print("responding back...")
			api.update_status('@' + mention.user.screen_name + ' Food? Lets GO!', mention.id)

while True:
	automatic_reply()
	time.sleep(10)
