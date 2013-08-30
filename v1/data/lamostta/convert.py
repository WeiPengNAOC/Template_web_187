'''
Convert   SDSS DR9 to one file
Weipeng 2013-6-30
NAOC CAS China
'''
import pyfits
import numpy
import matplotlib.pyplot as plt
from scipy import interpolate


hdulist=pyfits.open("spEigenStarA-miles.fits")
ncount=hdulist[0].header["NAXIS2"]

wavelengthStart=3800
wavelengthEnd=9000
wavelength=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart

wavelengthA=numpy.power(10,numpy.linspace(0,hdulist[0].header["NAXIS1"]-1,hdulist[0].header["NAXIS1"])*hdulist[0].header["COEFF1"]+hdulist[0].header["COEFF0"])


fluxout=numpy.ones([ncount,len(wavelength)])



for i in range(ncount):
	
	print i	
	flux=hdulist[0].data[i]
	print wavelengthA.shape,flux.shape
	tck = interpolate.interp1d(wavelengthA,flux,bounds_error=0,fill_value=0) 
	flux= tck(wavelength)
	flux=flux/numpy.sqrt(numpy.sum(flux*flux))
	fluxout[i]=flux
	plt.plot(wavelength,flux,'k')
	plt.xlabel("Wavelength($\AA$)")
	plt.ylabel("Flux")
	plt.title(hdulist[0].header["NAME"+str(i)])
	plt.ylim(numpy.min(flux),numpy.max(flux))
	plt.savefig("png/"+str(i)+".png")
	plt.close()
	
numpy.savetxt("dr9_flux.dat",fluxout)





