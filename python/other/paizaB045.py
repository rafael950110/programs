#!/usr/bin/env python
#coding: utf-8

# 文字コード通らず

from random import randint
def main() :
	opnum = list(map(int, input().split()))
	oprat = ['+','-']
	work = []
	while (opnum[0] + opnum[1]) != 0 :
		i = randint(0,2)
		a = randint(0,98)
		b = randint(1,99)
		if (opnum[0] and i) or not opnum[1]  :
			i = 0
			opnum[0] = opnum[0] - 1
		else :
			i = 1
			opnum[1] = opnum[1] - 1 
		work.append(" ".join(list(map(str, [b,oprat[i],a,"= "]))))

	for i in work[:-1] :
		print(i)
	print(work[-1])

if __name__ == "__main__" :
	main()