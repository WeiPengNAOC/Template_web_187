'''
Convert   Southern MK Standards 5800-10200A to one file
Weipeng 2013-6-30
NAOC CAS China
'''
import pyfits
import numpy
import matplotlib.pyplot as plt
from scipy import interpolate



wavelengthStart=3800
wavelengthEnd=9000
wavelengthout=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart


fluxout=numpy.ones([55,len(wavelengthout)])
for i in range(1,56):
	
	print i
	fitsname="dat/es"+str(i).zfill(2)+".dat"
	data=numpy.loadtxt(fitsname,delimiter="  ", skiprows=0)
	
	wavelength=data[:,0]
	flux=data[:,1]
	tck = interpolate.interp1d(wavelength,flux,bounds_error=0,fill_value=0) 
	flux= tck(wavelengthout)
	flux=flux/numpy.sqrt(numpy.sum(flux*flux))
	fluxout[i-1]=flux
	plt.plot(wavelengthout,flux,'k')
	plt.xlabel("Wavelength($\AA$)")
	plt.ylabel("Flux")
	
	plt.ylim(numpy.min(flux),numpy.max(flux))
	plt.savefig("png/es"+str(i).zfill(2)+".png")
	plt.close()
	
numpy.savetxt("es_flux.dat",fluxout)





