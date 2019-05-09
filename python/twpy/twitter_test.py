#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy
import urllib
import copy
import os

# 各種キーをセット
CONSUMER_KEY 		= 'WQw5XnD0EIVNj3AuT5m6ijiM6'
CONSUMER_SECRET = 'PJV59MHqotZg8IjcGqzqMmrd5YOQoWyWWuNTbXDhFlGiB9T8nR'
auth 						= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN 		= '232266833-muorp5MOVJNVop2ifUEsHQBJ45sZLCHDe8RAH6mb'
ACCESS_SECRET 	= 's6Z8Us7apm9ZXekmrodwxKcjcR7btgtEVrZrSWqwHz4Il'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

names = {	"kouyoumatsunaga":u"今日の一枚",
					"sasurainopink":u"朝のお絵描き"}
					# "i_yazawa_nico":u"safebooru"
					# "Strangestone":u"今日のたわわ　その"

for twi_id,tweet_text in names.items():

	maxid				= api.user_timeline(twi_id).max_id
	folder			= "./twifoto/" + twi_id + "/"
	END_FLAG = True
	l = 0

	if os.path.exists(folder) == False :
		os.makedirs(folder)

	print(twi_id,":",maxid)

	while END_FLAG and l < 16 :
		l += 1
		for twi in api.user_timeline(twi_id, count=200, max_id=maxid, include_rts=False):
			maxid = twi.id
			if hasattr(twi, "extended_entities"):
				if twi.extended_entities.has_key("media"):
					if twi.text[:len(tweet_text)] == tweet_text :
						
						NAME = twi.text.split()[0] + '.' + os.path.basename(twi.extended_entities["media"][0]["media_url_https"]).split('.')[1]
						
						if os.path.exists(folder + NAME) :
							print("  i have",NAME[len(tweet_text):],"\tid :",twi.id)
							END_FLAG = False
							break

						for index,media in enumerate(twi.extended_entities["media"]):
							print("  Downloading :",NAME[len(tweet_text):],"\tid :",twi.id)
							img_url = media["media_url_https"]
							img = urllib.urlopen(img_url)
							tmp_path = open(folder + NAME, "wb")
							tmp_path.write(img.read())
							img.close()
							tmp_path.close()


names = {
					"i_yazawa_nico":u"safebooru",
					"kazuharukina":u"safebooru"
				}

for twi_id,tweet_text in names.items():

	maxid				= api.user_timeline(twi_id).max_id
	folder			= "./twifoto/" + twi_id + "/"
	END_FLAG = True
	l = 0

	if os.path.exists(folder) == False :
		os.makedirs(folder)

	print(twi_id,":",maxid)

	while END_FLAG and l < 16 :
		l += 1
		for twi in api.user_timeline(twi_id, count=200, max_id=maxid, include_rts=False):
			maxid = twi.id
			if hasattr(twi, "extended_entities"):
				if twi.extended_entities.has_key("media"):
					
					NAME = twi.text.split()[0] + '.' + os.path.basename(twi.extended_entities["media"][0]["media_url_https"]).split('.')[1]
					
					if os.path.exists(folder + NAME) :
						print("  i have",NAME[len(tweet_text):],"\tid :",twi.id)
						END_FLAG = False
						break

					for index,media in enumerate(twi.extended_entities["media"]):
						print("  Downloading :",NAME[len(tweet_text):],"\tid :",twi.id)
						img_url = media["media_url_https"]
						img = urllib.urlopen(img_url)
						tmp_path = open(folder + NAME, "wb")
						tmp_path.write(img.read())
						img.close()
						tmp_path.close()