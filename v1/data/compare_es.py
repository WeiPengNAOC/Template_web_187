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
wavelength=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

mk_template=numpy.matrix(numpy.loadtxt("es_flux.dat"))


for i in range(0,172):
	print i
	filename="../result/"+str(i)+"/templatespectra.txt"
	if os.path.exists(filename):
		flux=numpy.matrix(numpy.loadtxt(filename))
		flux=numpy.matrix(flux/numpy.sqrt(numpy.sum(flux*flux.getT())))
		dis=numpy.ones(len(mk_template))
		
		for j in range(len(mk_template)):
			dis[j]=numpy.sqrt(numpy.sum(numpy.power(flux-mk_template[j],2)))
			#dis[j]=1-flux*mk_template[j].getT()
			
		index=numpy.argsort(dis)
		
		#index=index[0]
		#print index.shape
		
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

			
		#plt.plot(wavelengthout,mk_template[index[0,0],:].getT(),'r--')
		
		#plt.show()

			
		plt.savefig("es_png/t_es_"+str(i).zfill(3)+".png")
		plt.close()
