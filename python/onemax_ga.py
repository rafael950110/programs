#!/usr/bin/python
# -*- Coding: utf-8 -*-
import random
import copy

# パラメータ
LIST_SIZE 			= 10		# 0/1のリスト長（遺伝子長）
POPULATION_SIZE = 10		# 集団の個体数
GENERATION 			= 25		# 世代数
MUTATE 					= 0.1		# 突然変異の確率
SELECT_RATE 		= 0.5		# 選択割合


# --------------------
# 適応度の計算
def calc_fitness(individual):
	return sum(individual)

# --------------------
# 集団を適応度順にソート
def sort_fitness(population):
	fp = []

	# 集団ごとに適応度の計算
	for individual in population :
		fitness = calc_fitness(individual)
		fp.append((fitness,individual))
	fp.sort(reverse=True)

	# 適応度で降順にソート
	sorted_population = []
	for fitness, individual in fp :
		sorted_population.append(individual)

	return sorted_population


# --------------------
# (2)選択：適応度の高い個体を残す
def selection(population):
	sorted_population = sort_fitness(population)
	n = int(POPULATION_SIZE * SELECT_RATE)
	# nで計算された個体数だけ上から順に残す
	return sorted_population[0:n]


# --------------------
# (3)交叉：ind1をind2のランダムな範囲の遺伝子で書き換える
def crossover(ind1, ind2):
	r1 = random.randint(0, LIST_SIZE-1)
	r2 = random.randint(r1+1, LIST_SIZE)
	ind = copy.deepcopy(ind1)
	ind[r1:r2] = ind2[r1:r2]
	return ind


# --------------------
# (4)：突然変異：確率で突然変異
def mutation(ind1):
	ind2 = copy.deepcopy(ind1)
	for i in range(LIST_SIZE) :
		if random.random() < MUTATE :
			ind2[i] = random.randint(0,1)
	return ind2

population = []
for i in range(POPULATION_SIZE):
	individual = []
	for j in range(LIST_SIZE):
		individual.append(random.randint(0,1))
	population.append(individual)

for generation in range(GENERATION) :
	print(str(generation+1) + u"世代")

	population = selection(population)

	n = POPULATION_SIZE - len(population)
	for i in range(n):
		r1 = random.randint(0,len(population)-1)
		r2 = random.randint(0,len(population)-1)

		individual = crossover(population[r1], population[r2])

		individual = mutation(individual)

		population.append(individual)

	for individual in population :
		print(individual)