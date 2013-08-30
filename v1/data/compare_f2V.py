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

dr9_template=numpy.matrix(numpy.loadtxt("dr9_flux.dat"))



wavelengthStart=3800
wavelengthEnd=9000
wavelength=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart


fluxA=dr9_template[56]
fluxA=numpy.matrix(fluxA).getT()
#fluxA=fluxA/numpy.sqrt(numpy.sum(fluxA*fluxA))

filename="../result/58/templatespectra.txt"
if os.path.exists(filename):
		flux=numpy.matrix(numpy.loadtxt(filename)).getT()
		#flux=flux/numpy.sum(flux)
		p=numpy.polyfit(wavelength,flux/fluxA,3)
		wp=numpy.polyval(p,wavelength)
		wp=numpy.matrix(wp).getT()
		#print wp.shape
		plt.subplot(2,1,1)
		flux=flux/wp
		plt.plot(wavelength,flux,'k')	
		#plt.xlim(4000,9000)
		#ax=plt.subplot(2,1,2)
		plt.plot(wavelength,fluxA,'r--')	
		plt.xlabel("Wavelength($\AA$)")
		plt.ylabel("Flux")
		plt.legend(['F4V','F3V/F5V(Bolton et al. 2012) '],loc=1)

		wa=[3940,4102,4341,4862,6564,8500]
		width=[40,40,40,40,50,500]
		linename=['Ca H&K','H $\delta$','H $\gamma$','H $\\beta$','H $\\alpha$','$8000-9000\AA$']
		plt.minorticks_on()
		
		plt.xlim(3800,9200)
		for k in range(len(wa)):	
					
				ax=plt.subplot(2,len(wa),7+k)	
				cc=numpy.logical_and(wavelength>wa[k]-width[k],wavelength<wa[k]+width[k])
				
				ax.plot(wavelength[cc],flux[cc],'k')
				ax.plot(wavelength[cc],fluxA[cc],'r--')
				
			
				[y0,y1]=ax.get_ylim()				
				plt.xlabel(linename[k])
				plt.setp( ax.get_yticklabels(), visible=False)
				
				plt.setp( ax.get_xticklabels(), visible=False)
			
		#plt.subplot(2,1,2)
		#plt.plot(wavelength,100*(flux-fluxA)/fluxA,'k')
		
		plt.show()
