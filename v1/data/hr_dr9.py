'''
Compare template with MK
weipeng
NAOC CAS China
2013-6-30
'''
import os
from scipy import interpolate
import numpy
import matplotlib.pyplot as plt
import pyfits

hdulist=pyfits.open("spEigenStar-55734.fits")
tn=hdulist[0].header["NAXIS2"]-8

stype="OBAFGKM"
ltype=["I","II","III","IV","V"]
cindex=[3,4,2,1,0]
template=numpy.ones([tn,2])
for i in range(tn):
	cname=hdulist[0].header["NAME"+str(i)]
	cname=cname[0:cname.find("(")]
	for j in range(len(stype)):
		#print stype[j]
		if cname.find(stype[j])>=0:
			break
	template[i,0]=(j+1)*10
	for j in range(20):
		if cname.find(str(j/2))>=0:
			break
	template[i,0]=template[i,0]+j/2

	for j in range(len(cindex)):
		if cname.find(ltype[cindex[j]])>=0:
			break
	template[i,1]=cindex[j]+1
for j in range(len(stype)):
	plt.text((j+1)*10+5,0.7,stype[j]) 
for j in range(len(ltype)):
	plt.text(7,j+1,ltype[j]) 
'''
for i in range(10,81):
	plt.plot([i,i],[0.9,5.1],'k')
for i in range(1,6):
	plt.plot([9,81],[i,i],'k')
'''
ax=plt.subplot(111)
plt.plot(template[:,0],template[:,1],'k*')
plt.xlim(9,81)
plt.ylim(0.9,5.1)

plt.grid()
plt.setp( ax.get_yticklabels(), visible=False)				
plt.setp( ax.get_xticklabels(), visible=False)
plt.minorticks_on()
plt.show()
