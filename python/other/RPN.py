# _*_ coding: utf-8 _*_

def numASCII(char):
	return 47 < ord(char) < 58

def priority(char):
	operator = ["+","-","*","/","^"]
	return char in operator

def priorityComp(A,B):
	operator = {"+":1,"-":1,"*":2,"/":2,"^":3}
	if 39 < ord(A) < 42 or 39 < ord(B) < 42:
		return 0
	else:
		return operator[A] >= operator[B]

def calc(num1,num2,operator):
	if   operator == "+" : return num1 +  num2
	elif operator == "-" : return num1 -  num2
	elif operator == "*" : return num1 *  num2
	elif operator == "/" : return num1 /  num2
	elif operator == "^" : return num1 ** num2

def main(line) :
	num 		= 0		
	Polist  = []
	op_list = []

	for i in line:
		if numASCII(i):
			num = num * 10 + int(i)
			continue
			# 数字であればnumに格納をしていく
		if num:
			Polist.append(num)
			num = 0
			# iが数字でないとき、numに数字があればPolistへ格納
		op_list.append(i)
		j = 1

		# 演算子の優先順序により格納を行う処理
		while j < len(op_list):
			for p in reversed(range(1,j+1)):
				if priorityComp(op_list[p-1],op_list[p]):
					Polist.append(op_list[p-1])
					del op_list[p-1]
				else:
					j += 1

		if ord(i) == 41:
			j = op_list.index(i) - 1
			while(op_list[j] != "("):
				Polist.append(op_list[j])
				del op_list[j]
				j -= 1
			del op_list[j+1],op_list[j]
			if j-1 >= 0:
				Polist.append(op_list[j-1])
				del op_list[j-1]

	Polist.append(num)

	for j in reversed(range(len(op_list))):
		Polist.append(op_list[j])

	for i in Polist:
		print i,

	List = []
	for i in Polist:
		List.append(i)
		if priority(i):
			List.append(calc(float(List[len(List)-3]),float(List[len(List)-2]),List[len(List)-1]))
			for j in range(3):
				del List[len(List)-2]
	print "\n",List[0]

if __name__ == '__main__' :
	# line 	= list(raw_input('input:'))
	line = "3^3+4^4+5^5"
	print line
	main(line)