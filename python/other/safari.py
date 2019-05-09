# coding:utf-8

import os
import time
from selenium import webdriver
 
if __name__ == '__main__':
	try:
		# 検索したい単語の入力
		print('Input srarch word : ', end='')
		search_word = input()
 
		# ブラウザの起動
		browser = webdriver.Safari()
		# ページ推移
		browser.get('http://www.google.com')
		time.sleep(1)
		# Googleの検索フォーム要素を取得
		search_input = browser.find_element_by_name('q')
		# 検索フォームに検索単語を入力して検索
		search_input.send_keys(search_word)
		search_input.submit()
		time.sleep(1)
		# 検索結果ページのタイトルを出力
		print(browser.title)
	finally:
		print('.......END.......')
		# browser.quit()			# ブラウザを閉じたかったらこれ