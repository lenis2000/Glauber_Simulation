import numpy
numpy.set_printoptions(threshold=numpy.nan)


n = 20			###DEPTH OF THE INTERLACING ARRAY
sim_steps = 25000	###Number of Glauber steps (times height of the system) per one simulation
biga = 1

la = numpy.zeros((n,n))
laprint = numpy.zeros((n,n))

###BOUNDARY CONDITIONS

###HEXAGON


AAA = n/2
FFF = n/6
addition = -AAA/2-1

for m in xrange(0,n):
	for j in xrange(0,m+1):
		if m >= n/2:
			if 0 <= j <= m - n/2:
				la[m][j] = AAA + 1 + addition
			if j >= n/2:
				la[m][j] = 1 + addition
		if n/2 - 1 <= m < n/2 - 1 + 2*FFF and (n/2-1)/2 - FFF + (m-n/2+1) < j < (n/2-1)/2 + FFF:
			la[m][j] = AAA/2 + 1 + addition
		if n/2 - 1 - 2*FFF < m <= n/2 - 1 and (n/2-1)/2 - FFF < j < (n/2-1)/2 + FFF + (m-n/2+1):
			la[m][j] = AAA/2 + 1 + addition
			# print str(m) + " " + str(j) + " " + str(la[m][j-1]-j)

		laprint[m][j]=la[m][j]-j-1

print laprint[n/2]
print laprint[n/2-1]

# for x in xrange(0,n/2):
# 	print la[n/2-1][x]-x


###SYMMETRIC CARDIOID

# for m in xrange(0,n):
# 	for j in xrange(0,m+1):
# 		if 2*n/3 <= m <= n and 0 <= j <= m - 2*n/3:
# 			la[m][j] = n + 1
# 		else:
# 			if n/3 <= m <= n and m - 2*n/3 < j <= m - n/3:
# 				la[m][j] = n/2 + 1
# 			else:
# 				la[m][j] = 1

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

###12-GON

# for m in xrange(0,n):
# 	for j in xrange(0,m+1):
# 		if 3*n/4 <= m <= n and 0 <= j <= m - 3*n/4:
# 			la[m][j] = 5*n/4 + 1
# 		else:
# 			if 2*n/4 <= m <= n and m - 3*n/4 < j <= m - 2*n/4:
# 				la[m][j] = 2*n/2 + 1
# 			else:
# 				if 1*n/4 <= m <= n and m - 2*n/4 < j <= m - 1*n/4:
# 					la[m][j] = n/15 + 1
# 				else:
					# la[m][j] = 1

##24-GON

# def top_row ( n, k ) :
# 	return ( (n-k-1) / (n/8) ) * (n/8) + 1

# for m in xrange(0,n):
# 	for j in xrange(0,m+1):
# 		# la[m][j] = numpy.random.random_integers(m/7,6*m/7)
# 		la[m][j] = n/2-5

# for m in xrange(0,n-1):
# 	la[n-1][m] = top_row(n,m)

# 	la[n-1][n-1] = 1

###INTERACTIVE SIMULATION 

# while True:
# 	inch = raw_input("any key - do simulation, 2 - do simulation and print, p - print to file, q - exit:")
		
# 	if inch == "q":
# 		break

# 	if inch == "p":

# 		f = open('output.txt', 'w')

# 		f.write("{")
# 		for m in xrange(0,n):
# 		    f.write("{")
# 		    for k in xrange(0,n):
# 		        if k == n-1:
# 		        	f.write(str(la[m][k]))
# 		        else:
# 		        	f.write(str(la[m][k]) + ", ")
# 		    if m == n-1:
# 		    	f.write("}")
# 		    else:
# 		    	f.write("},")
# 		f.write("}")

# 		f.close()


# 	for x in xrange(1,sim_steps*n):
		
# 		while True:			
# 			m = numpy.random.random_integers(1,n-1)
# 			j = numpy.random.random_integers(1,n-1)
# 			if j <= m:
# 				break

# 		coin = numpy.random.random_integers(0,1)

# 		# print m, j, coin

# 		if coin == 1:
# 			if la[m-1][j-1] < la[m][j-1]:
# 				if m==1 or j==1:
# 					la[m-1][j-1] += 1
# 				else:
# 					if la[m-1][j-1] < la[m-2][j-2]:
# 						la[m-1][j-1] += 1

# 		if coin == 0:
# 			if la[m-1][j-1] > la[m][j]:
# 				if m==1 or j==m:
# 					la[m-1][j-1] -= 1
# 				else:
# 					if la[m-1][j-1] > la[m-2][j-1]:
# 						la[m-1][j-1] -= 1

# 	if inch == "2":
# 		print la

###SIMULATION OF MULTIPLE OUTPUTS

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

		##KEEP HOLES

		if n/2 - 1 <= m < n/2 - 1 + 2*FFF and (n/2-1)/2 - FFF + (m-n/2+1) < j < (n/2-1)/2 + FFF:
			la[m][j] = AAA/2 + 1 + addition
		else:
			if n/2 - 1 - 2*FFF < m <= n/2 - 1 and (n/2-1)/2 - FFF < j < (n/2-1)/2 + FFF + (m-n/2+1):
				la[m][j] = AAA/2 + 1 + addition
			else:
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


				

