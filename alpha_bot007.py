import tweepy
import time

CONSUMER_KEY = 'ijqTnFaY2vlYCusdT24UZUrz6'
CONSUMER_SECRET = 'ublA24VMFlJ42XKxlsQ9f7fqqI8mKA2fL8QEYXTKY0Cxe2ZoSD'
ACCESS_KEY = '396538152-mmH0C0YupndTZzmUqTMBN8NOAsn0NcGJ6lExsRHM'
ACCESS_SECRET = 'lFlQXCBeaxeirwBSbTunN5OqnTtUKSYI8CeopTGVqPkcJ'

# flush = True is used for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/

print('This is Sharim's twitter bot')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...'
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                    '#HelloWorld back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
