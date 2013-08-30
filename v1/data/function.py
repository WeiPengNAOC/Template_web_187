import numpy
def sim(x,y):
	
	x=numpy.matrix(x).getT()
	y=numpy.matrix(y).getT()
	return x*y.getT()/numpy.sqrt((x*x.getT())*(y*y.getT()))
def sim2(x,y):
	
	x=numpy.matrix(x)
	y=numpy.matrix(y)
	return x*y.getT()/numpy.sqrt((x*x.getT())*(y*y.getT()))
	
def polyfitWP(x,y,WX,n):
	#p=numpy.ones([1,n+1])
	m=len(x)
	#
	Y=numpy.matrix(numpy.ones([n+1,1]))
	'''
	X=numpy.matrix(numpy.ones([n+1,n+1]))
	for i in range(0,2*n+1):
		s=numpy.sum(numpy.power(x,i))		
		for j in range(0,n+1):
			if i-j>=0 and i-j<=n:
				#print i,j,i-j
				X[j,i-j]=s
	'''
	#print X
	for i in range(0,n+1):		
		Y[i,0]=numpy.sum(numpy.power(x,i)*y)
	
	p=WX.getI()*Y
	return p
def getWX(x,n):
	X=numpy.matrix(numpy.ones([n+1,n+1]))
	for i in range(0,2*n+1):
		s=numpy.sum(numpy.power(x,i))		
		for j in range(0,n+1):
			if i-j>=0 and i-j<=n:
				#print i,j,i-j
				X[j,i-j]=s
	return X
