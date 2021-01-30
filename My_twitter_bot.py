import tweepy

print("This is my automatically replying Twitter robot")

API_KEY = '41JHa9mpYkeS0IyREeTQ9MKKZ'
API_SECRET = '9tJUqNisMaWocqIMKJPhjZ0T1gqfSXrvwC9TTp2LRKjVnbST6s'
ACCESS_TOKEN = '1355176972360495108-e6NdMoAObMtMifXnR3LtgLzzJ1iEJP'
ACCESS_SECRET = '6kVGz3Mv5OIW4Id9brBj7m8RdEw22QQNtXwkNgbNWhSNG'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

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

last_seen_id = retrieve_last_seen_id(FILE_NAME)
store_last_seen_id(last_seen_id+111, FILE_NAME)