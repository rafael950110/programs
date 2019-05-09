#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy
import urllib
import copy
import os
from timeout_decorator import timeout, TimeoutError

# keys
CONSUMER_KEY 		= 'WQw5XnD0EIVNj3AuT5m6ijiM6'
CONSUMER_SECRET = 'PJV59MHqotZg8IjcGqzqMmrd5YOQoWyWWuNTbXDhFlGiB9T8nR'
auth 						= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN 		= '232266833-muorp5MOVJNVop2ifUEsHQBJ45sZLCHDe8RAH6mb'
ACCESS_SECRET 	= 's6Z8Us7apm9ZXekmrodwxKcjcR7btgtEVrZrSWqwHz4Il'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# api set
api = tweepy.API(auth)

names = []
with open('twpy_ids.txt','r') as f:
	for line in f : names.append(line[:-1])

@timeout(10)
def get_img(twi_id,maxid,sinceid,folder):
	global api
	print("\033[1m" + twi_id + "\033[0m start download mediafile")
	
	for l in range(16):
		for twi in api.user_timeline(twi_id, count=200, max_id=maxid, since_id=sinceid, include_rts=False):
			maxid = twi.id
			if hasattr(twi, "extended_entities"):
				if twi.extended_entities.has_key("media"):
					for index,media in enumerate(twi.extended_entities["media"]):

						if media["type"] == 'photo' :
							img_url = media["media_url_https"]
							print("\t" + str(media["id"]))
							 # + " image save to " + folder)
							img = urllib.urlopen(img_url)
							tmp_path = open(folder + str(twi.id) + "_" + os.path.basename(img_url), "wb")
							tmp_path.write(img.read())
							img.close()
							tmp_path.close()
							continue

						# elif media["type"] == 'video' :
						else :
							bit, ind = 0, 0
							for index,video in enumerate(media["video_info"]["variants"]):
								if 'bitrate' in video.keys() :
									if bit < video["bitrate"] :
										bit, ind = video["bitrate"], index
							img_url = media["video_info"]["variants"][ind]['url']
							# print("\t" + str(media["id"]) + " video save to " + folder + "")
							urllib.urlretrieve(media["video_info"]["variants"][ind]['url'],folder + str(twi.id) + "_" + os.path.basename(img_url))
							continue
			twiided = twi.id
			if sinceid >= maxid :
				print("BREAK")
				break

if __name__ == '__main__':

	for twi_id in names :

		try : maxid = api.user_timeline(twi_id).max_id
		except tweepy.error.TweepError	: print("Failed to get maxid")
		sinceid			= 1
		folder			= "./twifoto/" + twi_id + "/"

		if os.path.exists(folder) == False :
			os.makedirs(folder)

		elif os.path.exists(folder+'tweet_id') :
			with open(folder + 'tweet_id','r') as f:
				line	= f.readline()
				if line : sinceid = int(line)

				
		if sinceid >= maxid : continue

		try :
			get_img(twi_id,maxid,sinceid,folder)
			with open(folder + 'tweet_id','w') as f:
				f.write(str(maxid))
		except TimeoutError : print(twi_id,"TIMEOUT")
		except : print("Error")
		else :
			with open(folder + 'tweet_id','w') as f:
				f.write(str(maxid))