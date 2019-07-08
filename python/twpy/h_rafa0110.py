#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy
import urllib
import copy
import os


def gettwitterdata(keyword,dfile):

	# 各種キーをセット
	CONSUMER_KEY 		= 'WQw5XnD0EIVNj3AuT5m6ijiM6'
	CONSUMER_SECRET = 'PJV59MHqotZg8IjcGqzqMmrd5YOQoWyWWuNTbXDhFlGiB9T8nR'
	auth 						= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	ACCESS_TOKEN 		= '232266833-muorp5MOVJNVop2ifUEsHQBJ45sZLCHDe8RAH6mb'
	ACCESS_SECRET 	= 's6Z8Us7apm9ZXekmrodwxKcjcR7btgtEVrZrSWqwHz4Il'
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	
	api = tweepy.API(auth, wait_on_rate_limit = True)

	#検索キーワード設定 
	q = keyword

	#つぶやきを格納するリスト
	tweets_data =[]

	#カーソルを使用してデータ取得
	for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():
		tweets_data.append(tweet.full_text + '\n')

	#出力ファイル名
  fname = r"'"+ dfile + "'"
  fname = fname.replace("'","")

  #ファイル出力
  with open(fname, "w",encoding="utf-8") as f:
  	f.writelines(tweets_data)

if __name__ == '__main__':

	#検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
	print ('====== Enter Serch KeyWord   =====')
	keyword = input('>  ')

	#出力ファイル名を入力(相対パス or 絶対パス)
	print ('====== Enter Tweet Data file =====')
	dfile = input('>  ')

	gettwitterdata(keyword,dfile)