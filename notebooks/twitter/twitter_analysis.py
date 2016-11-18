#!/usr/bin/python3
import twitter

CONSUMER_KEY = 'slAIp8kYfqM4yjEm7G8hzJJo8'
CONSUMER_SECRET = 'kBBNIMiEdLYGTiJt7Lt3oZP52G2X8jM8Os1u82VXs2u1Ape1WN'
OAUTH_TOKEN = '788273630945742849-ghgqY1rsJVeYLBCQZ0IuHfUjz3ejTe1'
OAUTH_TOKEN_SECRET = 'kxuZpgWPjyTVYscJKFml2RI2nvjBRVND4qg878gPEePq9'

auth = twitter.oauth.OAuth(OAUTH_TOKEN , OAUTH_TOKEN_SECRET , CONSUMER_KEY , CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth =auth)

print (twitter_api)

import json

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
IND_WOE_ID = 23424848

world_trends = twitter_api.trends.place(_id = WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id = US_WOE_ID)
india_trends = twitter_api.trends.place(_id = IND_WOE_ID)

print (json.dumps(world_trends,indent = 2))
print (us_trends)
print (india_trends)