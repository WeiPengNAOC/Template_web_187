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
import scipy.signal
import function
wavelengthStart=3800
wavelengthEnd=9000
wavelengA=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

wavelengthout=6100+numpy.linspace(0,724,725)*4

cols=numpy.logical_and(numpy.logical_or(wavelengthout>7700,wavelengthout<7500),numpy.logical_or(wavelengthout<6800,wavelengthout>7000))
wavelengthout=wavelengthout[cols]
wavelength=wavelengthout
filename="mk_stars.dat"
fileobj=open(filename)
lines=fileobj.readlines()
fileobj.close()




for i in range(0,428):
	mk_template=numpy.matrix(numpy.loadtxt("mk_flux.dat"))
	print i
	filename="../result/"+str(i)+"/templatespectra.txt"
	if os.path.exists(filename):
		fluxA=numpy.loadtxt(filename)
		tck = interpolate.interp1d(wavelengA,fluxA,bounds_error=0,fill_value=0) 
		flux= tck(wavelengthout)
		flux=numpy.matrix(flux).getT()
		
	
		dis=numpy.ones(len(mk_template))
		#p=numpy.polyfit(wavelengthout,flux.getT(),5)
		#c=numpy.polyval(p,wavelengthout)
		for j in range(len(mk_template)):
			fluxA=numpy.matrix(mk_template[j,:]).getT()
			
			p=numpy.polyfit(wavelengthout,fluxA/flux,4)
			
			wp=numpy.polyval(p,wavelength)
			wp=numpy.matrix(wp).getT()
			
			
			fluxA=fluxA/wp
			#print flux.shape,fluxA.shape,wp.shape
			dis[j]=1-function.sim(flux,fluxA)
			mk_template[j]=fluxA[:,:].getT()
			
		index=numpy.argsort(dis)
		
		#index=index[0]
		#print index.shape
		
		ax=plt.subplot(5,1,1)
		ax.plot(wavelength,flux,'k')
		#ax.plot(wavelengthout,c,'k')
		plt.setp( ax.get_yticklabels(), visible=False)
		#plt.setp( ax.get_xticklabels(), visible=False)
		#plt.subplots_adjust(hspace=0.000)  
		#plt.subplots_adjust(wspace=0.000) 
		plt.minorticks_on()	
		for j in range(4):
			ss=lines[index[j]].replace("\n","").split(",")
			cols=numpy.logical_and(wavelengthout>6500,wavelengthout<6600)
			ax=plt.subplot(5,2,j*2+3)			
			ax.plot(wavelengthout[cols],flux[cols],'k')
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
			
			ax.plot(wavelengthout[cols],flux[cols],'k')
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
