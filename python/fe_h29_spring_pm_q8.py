Distance = [[0,2,8,4,-1,-1,-1],
						[2,0,-1,-1,3,-1,-1],
						[8,-1,0,-1,2,3,-1],
						[4,-1,-1,0,-1,8,-1],
						[-1,3,2,-1,0,-1,9],
						[-1,-1,3,8,-1,0,3],
						[-1,-1,-1,-1,9,3,0]]
nPoint = len(Distance)
sp, dp = 0,6
pRoute = [0 for i in range(nPoint)]

sDist  = 9999
sRoute = [  -1   for i in range(nPoint)]
pDist  = [ 9999  for i in range(nPoint)]
pFixed = [ False for i in range(nPoint)]

pDist[sp] = 0

while True :
	i = 0
	while i < nPoint :
		if not pFixed[i] :
			break
		i += 1

	if i == nPoint :
		break

	for j in range(i+1,nPoint) :
		if not pFixed[j] and pDist[j] < pDist[i] :
			i = j

	sPoint = i
	pFixed[sPoint] = True

	for j in range(nPoint) :
		if Distance[sPoint][j] > 0 and not pFixed[j] :
			newDist = pDist[sPoint] + Distance[sPoint][j]
			if newDist < pDist[j] :
				pDist[j] = newDist
				pRoute[j] = sPoint

	sDist = pDist[dp]
	j = 0
	i = dp
	while i != sp :
		sRoute[j] = i
		i = pRoute[i]
		j = j + 1
	sRoute[j] = sp

print(sRoute,"\n",sDist)