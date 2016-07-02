import numpy
numpy.set_printoptions(threshold=numpy.nan)


n = 10			###DEPTH OF THE INTERLACING ARRAY
sim_steps = 25000	###Number of Glauber steps (times height of the system) per one simulation
biga = 1

la = numpy.zeros((n,n))
laprint = numpy.zeros((n,n))

###BOUNDARY CONDITIONS

###SYMMETRIC CARDIOID

for m in xrange(0,n):
	for j in xrange(0,m+1):
		if 2*n/3 <= m <= n and 0 <= j <= m - 2*n/3:
			la[m][j] = n + 1
		else:
			if n/3 <= m <= n and m - 2*n/3 < j <= m - n/3:
				la[m][j] = n/2 + 1
			else:
				la[m][j] = 1

###NON-SYMMETRIC CARDIOID

# p=0.4

# for m in xrange(0,n):
# 	for j in xrange(0,m+1):
# 		if p*n <= m <= n and 0 <= j <= m - p*n:
# 			la[m][j] = n + 1
# 		else:
# 			if n/3 <= m <= n and m - p*n < j <= m - n/3:
# 				la[m][j] = 2*n/7 + 1
# 			else:
# 				la[m][j] = 1

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

	for x in xrange(1,sim_steps*n):
		
		while True:			
			m = numpy.random.random_integers(1,n-1)
			j = numpy.random.random_integers(1,n)
			if j <= m:
				break
				


