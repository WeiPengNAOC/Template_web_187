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
import function
wavelengthStart=3800
wavelengthEnd=9000
wavelength=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

dr9_template=numpy.matrix(numpy.loadtxt("es_flux.dat"))

for i in range(0,428):
	
	filename="../result/"+str(i)+"/templatespectra.txt"
	if os.path.exists(filename):
		flux=numpy.matrix(numpy.loadtxt(filename)).getT()
		dis=numpy.ones(len(dr9_template))
		
		for j in range(len(dr9_template)):
			
			fluxA=numpy.matrix(dr9_template[j,:]).getT()
			'''
			p=numpy.polyfit(wavelength,fluxA/flux,4)
			
			wp=numpy.polyval(p,wavelength)
			wp=numpy.matrix(wp).getT()			
			
			fluxA=fluxA/wp
			#print flux.shape,fluxA.shape
			
			dr9_template[j]=fluxA[:,:].getT()
			'''
			dis[j]=1-function.sim(flux,fluxA)
		index=numpy.argsort(dis)
		
		#index=index[0]
		#print index.shape
		print str(i+1)+","+str(index[0]+1)+","+str(index[1]+1)+","+str(index[2]+1)
		'''
		ax=plt.subplot(5,1,1)
		ax.plot(wavelength,flux.getT(),'k')
		plt.setp( ax.get_yticklabels(), visible=False)
		#plt.setp( ax.get_xticklabels(), visible=False)
		#plt.subplots_adjust(hspace=0.000)  
		#plt.subplots_adjust(wspace=0.000) 
		plt.minorticks_on()	
		for j in range(4):
			
			
			ax=plt.subplot(5,1,j+2)			
			ax.plot(wavelength,flux.getT(),'k')
			ax.plot(wavelength,mk_template[index[j],:].getT(),'r--')
			#plt.ylim([numpy.min(numpy.min(flux),numpy.min(mk_template[index[j]])),numpy.max(numpy.max(flux),numpy.max(mk_template[index[j]]))])
			
			[y0,y1]=ax.get_ylim()
			ax.text(3200,y1-(y1-y0)*0.9,str(index[j]))
			plt.setp( ax.get_yticklabels(), visible=False)
			if j<3:
				plt.setp( ax.get_xticklabels(), visible=False)
			else:
				plt.setp( ax.get_xticklabels(), visible=True)
		'''
			
		#plt.plot(wavelengthout,mk_template[index[0,0],:].getT(),'r--')
		
		#plt.show()

			
		plt.savefig("es_png/t_es_"+str(i).zfill(3)+".png")
		plt.close()
