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

for mention in mentions:
	print('mention.id' + 'mention.full_text')