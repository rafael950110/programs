# _*_ coding: utf-8 _*_
import itertools

numlist = ["2.0","3.0","5.0","7.0"]
operator = ["+","-","*","/","**"]

nums = list(itertools.permutations(numlist))
opes = list(itertools.permutations(operator,3))
print opes
for num in nums :
	for op in opes :
		(n1,n2,n3,n4) = num
		(o1,o2,o3) 		= op
		calc = n1+o1+n2+o2+n3+o3+n4
		if eval(calc) == -6 : print calc.replace(".0","")