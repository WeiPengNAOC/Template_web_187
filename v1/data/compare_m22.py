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
ncount=hdulist[0].header["NAXIS2"]


wavelengthStart=5000
wavelengthEnd=9000
wavelength=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

wavelengthStart=3800
wavelengthEnd=9000
wavelengthB=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

wavelengthA=numpy.power(10,numpy.linspace(0,hdulist[0].header["NAXIS1"]-1,hdulist[0].header["NAXIS1"])*hdulist[0].header["COEFF1"]+hdulist[0].header["COEFF0"])

fluxA=hdulist[0].data[19]
tck = interpolate.interp1d(wavelengthA,fluxA,bounds_error=0,fill_value=0) 
fluxA= tck(wavelength)
fluxA=fluxA/numpy.sqrt(numpy.sum(fluxA*fluxA))
fluxA=numpy.matrix(fluxA).getT()

filename="../result/236/templatespectra.txt"

hdulist=pyfits.open("../total/m2.nactive.na.k.fits")
wavelengthStart=hdulist[0].header["CRVAL1"]
wavelengthA=numpy.linspace(0,(hdulist[0].header["NAXIS1"]-1)*hdulist[0].header["CD1_1"],hdulist[0].header["NAXIS1"])+wavelengthStart
fluxB=hdulist[0].data[0]

tck = interpolate.interp1d(wavelengthA,fluxB,bounds_error=0,fill_value=0) 
fluxB= tck(wavelength)

fluxB=fluxB/numpy.sqrt(numpy.sum(fluxB*fluxB))
fluxB=numpy.matrix(fluxB).getT()

if os.path.exists(filename):
		flux=numpy.loadtxt(filename)
		tck = interpolate.interp1d(wavelengthB,flux,bounds_error=0,fill_value=0) 
		flux= tck(wavelength)
		flux=flux/numpy.sqrt(numpy.sum(flux*flux))
		flux=numpy.matrix(flux).getT()
		#flux=flux/numpy.sum(flux)
		plt.subplot(2,1,1)
		p=numpy.polyfit(wavelength,flux/fluxA,3)
		wp=numpy.polyval(p,wavelength)
		wp=numpy.matrix(wp).getT()
		#print wp.shape
		
		flux=flux/wp
		
		plt.plot(wavelength,flux,'k')		
		plt.plot(wavelength,fluxA,'r--')
		
		plt.xlabel("Wavelength($\AA$)")
		plt.ylabel("Flux")
		plt.legend(['M2','M2(Wang et al. 2010)'],loc=4)
		plt.subplot(2,1,2)
		p=numpy.polyfit(wavelength,flux/fluxB,3)
		wp=numpy.polyval(p,wavelength)
		wp=numpy.matrix(wp).getT()
		#print wp.shape
		
		flux=flux/wp
		
		plt.plot(wavelength,flux,'k')		
		plt.plot(wavelength,fluxB,'r--')
		
		plt.xlabel("Wavelength($\AA$)")
		plt.ylabel("Flux")
		plt.legend(['M2','M2(Bochanski et al. 2007)'],loc=4)
		'''
		wa=[3940,4102,4341,4862,6564]
		width=[40,40,40,40,50]
		linename=['Ca H&K','H $\delta$','H $\gamma$','H $\\beta$','H $\\alpha$']
		plt.minorticks_on()
		
		#plt.xlim(3800,7400)
		for k in range(len(wa)):	
					
				ax=plt.subplot(2,len(wa),6+k)	
				cc=numpy.logical_and(wavelength>wa[k]-width[k],wavelength<wa[k]+width[k])
				
				ax.plot(wavelength[cc],flux[cc],'k')
				ax.plot(wavelength[cc],fluxA[cc],'r--')
				
			
				[y0,y1]=ax.get_ylim()				
				plt.xlabel(linename[k])
				plt.setp( ax.get_yticklabels(), visible=False)
				
				plt.setp( ax.get_xticklabels(), visible=False)
		'''	
		#plt.subplot(2,1,2)
		#plt.plot(wavelength,100*(flux-fluxA)/fluxA,'k')
		
		plt.show()
