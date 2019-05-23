#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys, random, math, copy, tkinter, time

# パラメータ
SCREEN_WIDTH  = 720
SCREEN_HEIGHT = 720
POINTS_SIZE = 1000
LOOP = 3
K = 5
OVAL = 5
color = ['red','blue','green','yellow','purple','black','orange','gray','cyan','magenta']

# 点群座標，クラスタの設定
points = []
belong = []
for i in range(POINTS_SIZE) :
	points.append((random.random(), random.random()))
	belong.append(random.randint(0,K-1))
old_belong = list(reversed(belong))
clusters = [[0,0] for i in range(K)]
count = 0

# --- 所属クラスタの設定 -----------------
def set_cluster(points, belong, clusters) :
	for i in range(POINTS_SIZE) :
		distance = 0
		min_dist = 9999
		for j in range(K) :
			x0, y0 = points[i]
			x1, y1 = clusters[j]
			distance = math.sqrt((x0-x1)**2 + (y0-y1)**2)
			if distance < min_dist :
				min_dist = distance
				belong[i] = j
	return belong

# --- クラスタの座標計算 -----------------
def calc_average_cluster(points, belong) :
	clusters = [[0,0] for i in range(K)]
	for i in range(POINTS_SIZE) :
		clusters[belong[i]][0] += points[i][0]
		clusters[belong[i]][1] += points[i][1]

	for i in range(K) :
		if belong.count(i) :
			clusters[i][0] /= belong.count(i)
			clusters[i][1] /= belong.count(i)
	return clusters

# --- メイン処理 -----------------
# ウィンドウ初期化
root = tkinter.Tk()
root.title(u"random TSP")
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))

# キャンバス作成
canvas = tkinter.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = 'gray10')
canvas.place(x=0, y=0)

clusters = calc_average_cluster(points, belong)

while belong != old_belong :

	root.title(u"k-means（" + str(count + 1) + "回)")
	count += 1

	canvas.delete('all')	# キャンバスをクリア
	
	for i in range(POINTS_SIZE) :
		x0, y0 = points[i]
		x1, y1 = clusters[belong[i]]

		# 経路の描画
		canvas.create_line( \
			x0 * SCREEN_WIDTH,	\
			y0 * SCREEN_HEIGHT,	\
			x1 * SCREEN_WIDTH,	\
			y1 * SCREEN_HEIGHT,	\
			fill=color[belong[i]], width=1)

		# 点群の描画
		canvas.create_oval( \
			x0 * SCREEN_WIDTH  - OVAL,	\
			y0 * SCREEN_HEIGHT - OVAL,	\
			x0 * SCREEN_WIDTH  + OVAL,	\
			y0 * SCREEN_HEIGHT + OVAL,	fill=color[belong[i]])

	canvas.update()

	old_belong = belong.copy()
	belong = set_cluster(points, belong, clusters)
	clusters = calc_average_cluster(points, belong)

	time.sleep(0.2)

root.title(u"k-means（" + str(count) + "回で終了)")
root.mainloop()