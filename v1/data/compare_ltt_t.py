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

hdulist=pyfits.open("spEigenStar-56240.fits")
wavelengthStart=3800
wavelengthEnd=9000
wavelength=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

dr9_template=numpy.matrix(numpy.loadtxt("ltt_flux.dat"))

templateflux=numpy.zeros([172,len(wavelength)])

for i in range(0,172):
	print i
	filename="../result/"+str(i)+"/templatespectra.txt"
	if os.path.exists(filename):
		flux=numpy.matrix(numpy.loadtxt(filename))
		flux=numpy.matrix(flux/numpy.sqrt(numpy.sum(flux*flux.getT())))
		#dis=numpy.ones(len(dr9_template))
		templateflux[i]=flux
for j in range(len(dr9_template)):
		for i in range(0,172):
			dis[j]=numpy.sqrt(numpy.sum(numpy.power(flux-dr9_template[j],2)))
			#dis[j]=1-flux*mk_template[j].getT()
			
		index=numpy.argsort(dis)
		
		#index=index[0]
		#print index.shape
		plt.figure(num=None, figsize=(10, 10), dpi=100, facecolor='w', edgecolor='k')
		ax=plt.subplot(5,1,1)
		ax.plot(wavelength,flux.getT(),'k')
		ax.plot(wavelength,dr9_template[index[0],:].getT(),'r--')
		plt.setp( ax.get_yticklabels(), visible=False)
		#plt.setp( ax.get_xticklabels(), visible=False)
		#plt.subplots_adjust(hspace=0.000)  
		#plt.subplots_adjust(wspace=0.000) 
		wa=[3940,4102,4341,4862,6564,8500]
		width=[40,40,40,40,50,500]
		linename=['Ca H&K','H $\delta$','H $\gamma$','H $\\beta$','H $\\alpha$','$8000-9000\AA$']
		plt.minorticks_on()
		
		for j in range(4):
			for k in range(len(wa)):	
					
				ax=plt.subplot(5,len(wa),(j+1)*len(wa)+k+1)	
				cc=numpy.logical_and(wavelength>wa[k]-width[k],wavelength<wa[k]+width[k])
				#print wa[k],width[k]
				ax.plot(wavelength[cc],flux.getT()[cc],'k')
				ax.plot(wavelength[cc],dr9_template[index[j],:].getT()[cc],'r--')
				#plt.ylim([numpy.min(numpy.min(flux),numpy.min(mk_template[index[j]])),numpy.max(numpy.max(flux),numpy.max(mk_template[index[j]]))])
			
				[y0,y1]=ax.get_ylim()
				if k==0:
					cname=hdulist[0].header["NAME"+str(index[j])]

					print cname
					ax.text(wa[0]-width[0]/2,y1-(y1-y0)*0.9,cname)
				plt.setp( ax.get_yticklabels(), visible=False)
				
				plt.setp( ax.get_xticklabels(), visible=False)
				if j==3 :
					plt.xlabel(linename[k])
				
					

			
		#plt.plot(wavelengthout,mk_template[index[0,0],:].getT(),'r--')
		
		#plt.show()

			
		plt.savefig("ltt_png/t_ltt_"+str(i).zfill(3)+".png")
		plt.close()
