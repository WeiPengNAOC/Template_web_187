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

wavelengthStart=3800
wavelengthEnd=9000
wavelengA=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

wavelengthout=6100+numpy.linspace(0,724,725)*4

cols=numpy.logical_and(numpy.logical_or(wavelengthout>7700,wavelengthout<7500),numpy.logical_or(wavelengthout<6800,wavelengthout>7000))
wavelengthout=wavelengthout[cols]

filename="mk_stars.dat"
fileobj=open(filename)
lines=fileobj.readlines()
fileobj.close()

mk_template=numpy.matrix(numpy.loadtxt("mk_flux.dat"))


for i in range(0,172):
	print i
	filename="../result/"+str(i)+"/templatespectra.txt"
	if os.path.exists(filename):
		fluxA=numpy.loadtxt(filename)
		tck = interpolate.interp1d(wavelengA,fluxA,bounds_error=0,fill_value=0) 
		flux= tck(wavelengthout)
		flux=numpy.matrix(flux/numpy.sqrt(numpy.sum(flux*flux)))
		
	
		dis=numpy.ones(len(mk_template))
		
		for j in range(len(mk_template)):
			dis[j]=numpy.sqrt(numpy.sum(numpy.power(flux-mk_template[j],2)))
			#dis[j]=1-flux*mk_template[j].getT()
			
		index=numpy.argsort(dis)
		
		#index=index[0]
		#print index.shape
		
		ax=plt.subplot(5,1,1)
		ax.plot(wavelengA,fluxA,'k')
		plt.setp( ax.get_yticklabels(), visible=False)
		#plt.setp( ax.get_xticklabels(), visible=False)
		#plt.subplots_adjust(hspace=0.000)  
		#plt.subplots_adjust(wspace=0.000) 
		plt.minorticks_on()	
		for j in range(4):
			ss=lines[index[j]].replace("\n","").split(",")
			cols=numpy.logical_and(wavelengthout>6500,wavelengthout<6600)
			ax=plt.subplot(5,2,j*2+3)			
			ax.plot(wavelengthout[cols],flux.getT()[cols],'k')
			ax.plot(wavelengthout[cols],mk_template[index[j],:].getT()[cols],'r--')
			#plt.ylim([numpy.min(numpy.min(flux),numpy.min(mk_template[index[j]])),numpy.max(numpy.max(flux),numpy.max(mk_template[index[j]]))])
			plt.xlim([6500,6600])
			[y0,y1]=ax.get_ylim()
			ax.text(6520,(y1+y0)/2,ss[1])
			plt.setp( ax.get_yticklabels(), visible=False)
			if j<3:
				plt.setp( ax.get_xticklabels(), visible=False)
			else:
				plt.setp( ax.get_xticklabels(), visible=True)

			ax=plt.subplot(5,2,j*2+4)							
			cols=numpy.logical_and(wavelengthout>8400,wavelengthout<9000)
			
			ax.plot(wavelengthout[cols],flux.getT()[cols],'k')
			ax.plot(wavelengthout[cols],mk_template[index[j],:].getT()[cols],'r--')
			#plt.ylim([numpy.min(numpy.min(flux),numpy.min(mk_template[index[j]])),numpy.max(numpy.max(flux),numpy.max(mk_template[index[j]]))])
			[y0,y1]=ax.get_ylim()
			#ax.text(7500,y1*0.8,ss[1])
			plt.setp( ax.get_yticklabels(), visible=False)
			plt.xlim([8400,9000])
			if j<3:
				plt.setp( ax.get_xticklabels(), visible=False)
			else:
				plt.setp( ax.get_xticklabels(), visible=True)
		#plt.plot(wavelengthout,mk_template[index[0,0],:].getT(),'r--')
		
		#plt.show()

			
		plt.savefig("mk_png/t_mk_"+str(i).zfill(3)+".png")
		plt.close()
