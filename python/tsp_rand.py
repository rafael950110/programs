#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys, random, math, copy, tkinter

# パラメータ
SCREEN_WIDTH  = 360
SCREEN_HEIGHT = 360
POINTS_SIZE = 50
LOOP = 100000

# --------------------
# 経路の距離を計算
def calc_distance(points, route) :
	distance = 0
	for i in range(POINTS_SIZE) :
		x0, y0 = points[route[i]]
		if i == POINTS_SIZE - 1 :
			x1, y1 = points[route[0]]
		else :
			x1, y1 = points[route[i+1]]
		distance = distance + math.sqrt((x0-x1)**2 + (y0-y1)**2)
	return distance

# --------------------
# メイン処理

# ウィンドウ初期化
root = tkinter.Tk()
root.title(u"random TSP")

# ウィンドウサイズ
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))

# キャンバス作成
canvas = tkinter.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
canvas.place(x=0, y=0)

# 都市座標生成
points = []
for i in range(POINTS_SIZE) :
	points.append((random.random(), random.random()))

# 経路生成
route = list(range(POINTS_SIZE))

min_route = copy.copy(route)				# 最短経路
min_dist  = calc_distance(points, route)	# 最短経路

for c in range(LOOP) :
	root.title(u"random TSP (" + str(c + 1) + "回)")

	# 経路をランダムに入れ替える
	random.shuffle(route)

	dist = calc_distance(points, route)

	if min_dist > dist :
		min_route = copy.copy(route)
		min_dist  = dist

		# 描画
		canvas.delete('all')	# キャンバスをクリア
		for i in range(POINTS_SIZE) :
			x0, y0 = points[route[i]]
			if i == POINTS_SIZE - 1 :
				x1, y1 = points[route[0]]
			else :
				x1, y1 = points[route[i+1]]

			# 経路の描画
			canvas.create_line( \
				x0 * SCREEN_WIDTH,	\
				y0 * SCREEN_HEIGHT,	\
				x1 * SCREEN_WIDTH,	\
				y1 * SCREEN_HEIGHT,	\
				fill="black", width=1)

			# 都市の描画
			canvas.create_oval( \
				x0 * SCREEN_WIDTH  - 3,	\
				y0 * SCREEN_HEIGHT - 3,	\
				x0 * SCREEN_WIDTH  + 3,	\
				y0 * SCREEN_HEIGHT + 3,	fill="blue")

		canvas.create_text(5, 5, text = "{:.2f}".format(min_dist), anchor = "nw", fill = "red")
		canvas.update()

root.mainloop()