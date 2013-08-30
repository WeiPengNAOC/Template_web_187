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

hdulist=pyfits.open("../total/m2.nactive.na.k.fits")
wavelengthStart=hdulist[0].header["CRVAL1"]
wavelengthA=numpy.linspace(0,(hdulist[0].header["NAXIS1"]-1)*hdulist[0].header["CD1_1"],hdulist[0].header["NAXIS1"])+wavelengthStart
fluxA=hdulist[0].data[0]



wavelengthStart=3800
wavelengthEnd=9000
wavelength=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

tck = interpolate.interp1d(wavelengthA,fluxA,bounds_error=0,fill_value=0) 
fluxA= tck(wavelength)

fluxA=fluxA/numpy.sqrt(numpy.sum(fluxA*fluxA))
fluxA=numpy.matrix(fluxA).getT()
filename="../result/236/templatespectra.txt"
if os.path.exists(filename):
		flux=numpy.matrix(numpy.loadtxt(filename)).getT()
		#flux=flux/numpy.sum(flux)
		p=numpy.polyfit(wavelength,flux/fluxA,3)
		wp=numpy.polyval(p,wavelength)
		wp=numpy.matrix(wp).getT()
		print wp
		plt.subplot(2,1,1)
		#flux=flux/wp
		plt.plot(wavelength,flux,'k')	
		#plt.xlim(4000,9000)
		#ax=plt.subplot(2,1,2)
		plt.plot(wavelength,fluxA,'r--')	
		plt.xlabel("Wavelength($\AA$)")
		plt.ylabel("Flux")
		plt.legend(['M2','M2 in Bochanski 2007'],loc=2)
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
		#plt.xlim(4000,9000)
		plt.show()
