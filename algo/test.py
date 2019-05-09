#!/usr/bin/env python
#coding: utf-8
# from random import randint, sample
from collections import Counter

initdict = {'a':1, 'b':2}
a = {}
b = {}
a.keys() = initdict.keys()
b.bkeys() = initdict.keys()
print a
print b
a['a'] = 2
print a
print b

# card_col = {'black':"□",'white':"■"}
# card ={'black':[i for i in range(12)],'white':[i for i in range(12)]}

# cards = [(m, n) for m in list(card_col.keys()) for n in range(12)]

# test = range(5)

# def LRlist(num):
# 	list = []
# 	for i in range(num) :
# 		j = num - int(i) - 1
# 		print i,j
# 		if int(i) >= int(j) : return list 
# 		if 	randint(0,1) :
# 			list.append(int(i))
# 			list.append(int(j))
# 		else :
# 			list.append(int(j))
# 			list.append(int(i))

# print LRlist(10)

# numDat = [[[0, 1, 2, 3, 4, 5, 8], [0, 2, 4, 5, 6, 7, 8], [2, 4, 5, 6, 7, 8, 9], 10], [1, [2, 4, 5], 6, [6, 7, 8, 9, 10, 11]], [[0, 2], [2, 4], [3, 4, 5], 7], [[0, 2], 3, [4, 5, 8, 9], [5, 8, 9, 11]]]
# colDat = [['black', 'white', 'white', 'black'], ['white', 'white', 'black', 'white'], ['white', 'white', 'black', 'black'], ['white', 'white', 'black', 'black']]
# flat_numDat = [i for line in numDat for i in line]
# flat_colDat = [i for line in colDat for i in line]

# numList = [] # 重複カードの値を収納するリスト
# colList = [] # 重複カードの色を収納するリスト

# for i in flat_numDat :
# 	count = -1
# 	if not type(i) is list or i in numList : continue
# 	for j in flat_numDat :
# 		if i == j and flat_colDat[flat_numDat.index(i)] == flat_colDat[flat_numDat.index(j)]:
# 			count += 1
# 	if count and count + 1 == len(i) : # 重複数がカードの数と一致すれば重複とみなす
# 		numList.append(i)
# 		colList.append(flat_colDat[flat_numDat.index(i)])

# for nums,cols in zip(numDat,colDat) :
# 	for num,col in zip(nums,cols) :
# 		for numL,colL in zip(numList,colList) :
# 			if num == numL : continue
# 			if col == colL and type(num) is list :
# 				i = numDat.index(nums)
# 				j = numDat[i].index(num)
# 				for n in numL : 
# 					while n in numDat[i][j] : numDat[i][j].remove(n)
# print 
# for i,j in zip(numDat,colDat) :
# 	print i,j
