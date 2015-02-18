import numpy
numpy.set_printoptions(threshold=numpy.nan)


n = 40				###DEPTH OF THE INTERLACING ARRAY
sim_steps = 10000 		###Number of Glauber steps per one simulation

la = numpy.zeros((n,n))

###BOUNDARY CONDITIONS

###HEXAGON

for m in xrange(0,n):
	for j in xrange(0,m+1):
		if n/2 <= m <= n and 0 <= j <= m - n/2:
			la[m][j] = n/2 + 1
		else:
			la[m][j] = 1

###CARDIOID

# for m in xrange(0,n):
# 	for j in xrange(0,m+1):
# 		if 2*n/3 <= m <= n and 0 <= j <= m - 2*n/3:
# 			la[m][j] = n + 1
# 		else:
# 			if n/3 <= m <= n and m - 2*n/3 < j <= m - n/3:
# 				la[m][j] = n/3 + 1
# 			else:
# 				la[m][j] = 1

###12-GON

# for m in xrange(0,n):
# 	for j in xrange(0,m+1):
# 		if 3*n/4 <= m <= n and 0 <= j <= m - 3*n/4:
# 			la[m][j] = 6*n/2 + 1
# 		else:
# 			if 2*n/4 <= m <= n and m - 3*n/4 < j <= m - 2*n/4:
# 				la[m][j] = 5*n/2 + 1
# 			else:
# 				if 1*n/4 <= m <= n and m - 2*n/4 < j <= m - 1*n/4:
# 					la[m][j] = n/2 + 1
# 				else:
# 					la[m][j] = 1

###INTERACTIVE SIMULATION

while True:
	inch = raw_input("1 - do simulation, 2 - do simulation and print, p - print to file, q - exit:")
		
	if inch == "q":
		break

	if inch == "p":

		f = open('output.txt', 'w')

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


	for x in xrange(1,sim_steps*n):
		
		while True:			
			m = numpy.random.random_integers(1,n-1)
			j = numpy.random.random_integers(1,n-1)
			if j <= m:
				break

		coin = numpy.random.random_integers(0,1)

		# print m, j, coin

		if coin == 1:
			if la[m-1][j-1] < la[m][j-1]:
				if m==1 or j==1:
					la[m-1][j-1] += 1
				else:
					if la[m-1][j-1] < la[m-2][j-2]:
						la[m-1][j-1] += 1

		if coin == 0:
			if la[m-1][j-1] > la[m][j]:
				if m==1 or j==m:
					la[m-1][j-1] -= 1
				else:
					if la[m-1][j-1] > la[m-2][j-1]:
						la[m-1][j-1] -= 1

	if inch == "2":
		print la







