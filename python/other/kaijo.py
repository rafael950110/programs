
for i in range(1,101) :
	num = 1
	for j in range(1,i+1) : num = num * int(j)
	print "{: 4}! > {}.{} * 10^{}".format(i,str(num)[0],str(num)[1:3],len(str(num)))