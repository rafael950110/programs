#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys, random, math, copy, tkinter

# パラメータ
SCREEN_WIDTH  = 150
SCREEN_HEIGHT = 150
POINTS_SIZE = 100
POPULATION_SIZE = 20
GENERATION = 5000
MUTATE = 0.3
SELECT_RATE = 0.5


# --------------------
# 経路の距離計算（個体の適応度計算）
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
# 適応度で集団を昇順ソート
def sort_fitness(points, population) :
	fp = []
	for individual in population :
		fitness = calc_distance(points, individual)
		fp.append((fitness, individual))
	fp.sort()

	sorted_population = []

	for fitness, individual in fp :
		sorted_population.append(individual)

	return sorted_population


# --------------------
# 選択（適応度の高い個体を残す）
def selection(points, population) :
	sorted_population = sort_fitness(points, population)
	n = int(POPULATION_SIZE * SELECT_RATE)

	return sorted_population[0:n]


# --------------------
# 交叉（範囲は乱数で決める）
def crossover(ind1, ind2) :
	r1 = random.randint(0, POPULATION_SIZE - 1)
	r2 = random.randint(r1 + 1, POINTS_SIZE)

	# 使った都市のフラグのリストを0で初期化
	flag = [0] * POINTS_SIZE
	# 子の個体（-1で初期化）
	ind = [-1] * POINTS_SIZE

	# r1〜r2をind2から複製
	for i in range(r1, r2) :
		city = ind2[i]
		ind[i] = city
		# 使った都市のフラグに1をセット
		flag[city] = 1

	# 使われていない都市をind1から複製
	for i in list(range(0,r1)) + list(range(r2, POINTS_SIZE)) :
		city = ind1[i]
		# 未使用
		if flag[city] == 0 :
			ind[i] = city
			flag[city] = 1

	# 残った都市
	for i in range(0, POINTS_SIZE) :
		if ind[i] == -1 :
			for j in range(0, POINTS_SIZE) :
				city = ind1[j]
				if flag[city] == 0 :
					ind[i] = city
					flag[city] = 1
					break
	return ind

# --------------------
# 突然変異（ランダムな都市間の経路を逆順にする）
def mutation(ind1) :
	ind2 = copy.deepcopy(ind1)
	if random.random() < MUTATE :
		city1 = random.randint(0, POINTS_SIZE - 1)
		city2 = random.randint(0, POINTS_SIZE - 1)
		if city1 > city2 :
			city1, city2 = city2, city1
		ind2[city1:city2+1] = reversed(ind2[city1:city2+1])

	return ind2


# --------------------
# メイン処理

# ウィンドウ初期化
root = tkinter.Tk()
root.title(u"GA TSP")

width_size = 5
height_size = math.ceil(POPULATION_SIZE / width_size)
window_with = SCREEN_WIDTH * width_size
window_height = SCREEN_HEIGHT * width_size
root.geometry(str(window_with) + "x" + str(window_height))

# 集団の数だけキャンバス作成
canvas_list = []
for i in range(POPULATION_SIZE) :
	# キャンバス作成
	canvas = tkinter.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
	cx = i % width_size * SCREEN_WIDTH
	cy = int(i / width_size) * SCREEN_HEIGHT
	canvas.place(x=cx, y=cy)
	canvas_list.append(canvas)

# 都市座標生成
points = []
for i in range(POINTS_SIZE) :
	points.append((random.random(), random.random()))

# 初期集団を生成
population = []
for i in range(POPULATION_SIZE) :
	# 個体（経路）
	individual = list(range(POINTS_SIZE))
	# 経路をランダムに入れ替える
	random.shuffle(individual)
	population.append(individual)

for generation in range(GENERATION) :
	root.title(u"GA TSP （" + str(generation + 1) + "世代）")

	# 選択
	population = selection(points, population)

	# 交叉
	n = POPULATION_SIZE - len(population)
	for i in range(n) :
		r1 = random.randint(0, len(population) - 1)
		r2 = random.randint(0, len(population) - 1)
		individual = crossover(population[r1], population[r2])

		# 突然変異
		individual = mutation(individual)

		# 集団に追加
		population.append(individual)

	if generation % 500 : continue

	# 集団を適応度順にソート
	sort_fitness(points, population)

	for ind in range(POPULATION_SIZE) :
		canvas = canvas_list[ind]
		route = population[ind]
		dist = calc_distance(points, route)
		canvas.delete('all')
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

		canvas.create_rectangle( \
			0, 0, SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1, \
			outline = "gray", width=1)

		canvas.create_text( \
			5, 5, text = "{:.2f}".format(dist), \
			anchor = "nw", fill = "red")

		canvas.update()

root.mainloop()