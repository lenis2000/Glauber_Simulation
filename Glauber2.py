import numpy
numpy.set_printoptions(threshold=numpy.nan)

n = 6

la = numpy.zeros((n,n))

for m in xrange(0,n):
	for j in xrange(0,m+1):
		if 2*n/3 <= m <= n and 0 <= j <= m - 2*n/3:
			la[m][j] = 2*n + 1
		else:
			if 2*n/3 <= m <= n and m - 2*n/3 < j <= m - n/3:
				la[m][j] = 3*n/2 + 1
			else:
				la[m][j] = 1


# for m in xrange(0,n):
# 	for j in xrange(0,m+1):
# 		if 3*n/4 <= m <= n and 0 <= j <= m - 3*n/4:
# 			la[m][j] = 3*n/2 + 1
# 		else:
# 			if 3*n/4 <= m <= n and m - 3*n/4 < j <= m - 2*n/4:
# 				la[m][j] = n + 1
# 			else:
# 				if 3*n/4 <= m <= n and m - 2*n/4 < j <= m - 1*n/4:
# 					la[m][j] = n/2 + 1
# 				else:
# 					la[m][j] = 1



		
for x in xrange(1,4):
	
	m = numpy.random.random_integers(1,n-1)
	j = numpy.random.random_integers(1,m)
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

# print la

print "{"
for m in xrange(0,n):
    print "{"
    for k in xrange(0,n):
        if k == n-1:
        	print (la[m][k])	
        else:
        	print (str(la[m][k]) + ", ")
    if m == n-1:
    	print "}"
    else:
    	print "},"
print "}"







