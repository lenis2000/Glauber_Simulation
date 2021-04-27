import numpy
numpy.set_printoptions(threshold=numpy.nan)


n = 20			###DEPTH OF THE INTERLACING ARRAY
sim_steps = 50000	###Number of Glauber steps (times height of the system) per one simulation
biga = 50

la = numpy.zeros((n,n))
laprint = numpy.zeros((n,n))

###BOUNDARY CONDITIONS

###HEXAGON


AAA = n
addition = -AAA/2-1
HOLE_SIZE = 3
OTHER_ADD = 0

#MAKE A PLAIN HEXAGON ; INITIAL CONDITION SPEEDS UP THE CONVERGENCE

for m in xrange(0,n):
	for j in xrange(0,m+1):
		if m >= n/2:
			if 0 <= j <= m - n/2:
				la[m][j] = AAA + 1 + addition
			if j >= n/2:
				la[m][j] = 1 + addition

for a in xrange(0,biga):
	f = open('output' + str(a) + '.txt', 'w')
	f.write("{")
	for m in xrange(0,n):
		f.write("{")
		for k in xrange(0,n):
			if k == n-1:
				f.write(str(la[m][k]))
			else:
				f.write(str(la[m][k]) + ", ")
		if m == n-1:
			f.write("}")
		else:
			f.write("},")
	f.write("}")
	f.close()
	print str(a) + " "
	for x in xrange(1,sim_steps*n) :
		m = numpy.random.random_integers(1,n-1)
		j = numpy.random.random_integers(1,m)

		if m == n/2 - 1 and m/2. - HOLE_SIZE <= j and j <= m/2. + HOLE_SIZE:
			la[m][j + OTHER_ADD] = OTHER_ADD
		if m < n/2 - 1 and (n/2 - 1)/2. - HOLE_SIZE <= j and j <= (n/2 - 1)/2. + HOLE_SIZE - (n/2 - 1 - m):
			la[m][j + OTHER_ADD] = OTHER_ADD
		if m > n/2 - 1 and (n/2 - 1)/2. - HOLE_SIZE - (n/2 - 1 - m)  <= j and j <= (n/2 - 1)/2. + HOLE_SIZE:
			la[m][j + OTHER_ADD] = OTHER_ADD

		coin = numpy.random.random()

		if coin < .5:
			if la[m-1][j-1] < la[m][j-1]:
				if m==1 or j==1:
					la[m-1][j-1] += 1
				else:
					if la[m-1][j-1] < la[m-2][j-2]:
						la[m-1][j-1] += 1
		else:
			if la[m-1][j-1] > la[m][j]:
				if m==1 or j==m:
					la[m-1][j-1] -= 1
				else:
					if la[m-1][j-1] > la[m-2][j-1]:
						la[m-1][j-1] -= 1

	for m in xrange(0,n):
		for j in xrange(0,n):
			if m == n/2 - 1 and m/2. - HOLE_SIZE <= j and j <= m/2. + HOLE_SIZE:
				la[m][j + OTHER_ADD] = OTHER_ADD
			if m < n/2 - 1 and (n/2 - 1)/2. - HOLE_SIZE <= j and j <= (n/2 - 1)/2. + HOLE_SIZE - (n/2 - 1 - m):
				la[m][j + OTHER_ADD] = OTHER_ADD
			if m > n/2 - 1 and (n/2 - 1)/2. - HOLE_SIZE - (n/2 - 1 - m)  <= j and j <= (n/2 - 1)/2. + HOLE_SIZE:
				la[m][j + OTHER_ADD] = OTHER_ADD