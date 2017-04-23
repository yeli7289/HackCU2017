from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import urllib
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="z01GCrFhYjkobADgbkiqENnhP"
consumer_secret="APgmBGwJF3jnYA04glxuKmyM8HiKCx8F4SjAif6ISp5HbLOai5"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="3227882478-jOn6wQ2wESh2MYG7PGNCwpMqV9nTDlunvS1YBZP"
access_token_secret="JkSa1XPcINsrOqO4NMZD3DZmTUkQTkqasLOBNMNCTB5II"

keywords = ['#trump', '#obama']
tags = ['trump','obama']
class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        ret = json.loads(data)
        # print ("TEXT: "+ret['text'].encode('ascii','ignore'))
        hashtags = ret['entities']['hashtags']
        tag_set = set()
        d = dict()
        timestamp = ret['created_at']
        location = ret['user']['location']
        # print (hashtags)
        if location!=None and hashtags:
            for h in hashtags:
                tag_set.add(str(h['text']).lower())
            try:
                if tags[0] in tag_set and tags[1] not in tag_set:
                    ## analysis ret['text'].enode('ascii', 'ignore')
                    d['text'] = str(ret['text'])
                    params = urllib.urlencode(d)
                    s = urllib.urlopen("http://text-processing.com/api/sentiment/",params);
                    # sentiment = json.load(s)
                    if (not isinstance(s,str)):
                        print ('!!!!!'+timestamp)
                        print (keywords[0])
                        print (json.loads(s.read())['label'])
                        print (location)

                    ## sent into db
                elif tags[1] in tag_set and tags[0] not in tag_set:
                    ## analysis ret['text'].enode('ascii', 'ignore')
                    d['text'] = str(ret['text'])
                    params = urllib.urlencode(d)
                    s = urllib.urlopen("http://text-processing.com/api/sentiment/",params);
                    # sentiment = json.loads(s)
                    if (not isinstance(s,str)):
                        print ('!!!!!'+timestamp)
                        print (keywords[1])
                        print (json.loads(s.read())['label'])
                        print (location)
            except UnicodeEncodeError:
                pass
                ## sent into db
        # print (ret['text'].encode('ascii', 'ignore'))
        return True
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(languages=["en"],track=keywords)