'''
Convert   Southern MK Standards 5800-10200A to one file
Weipeng 2013-6-30
NAOC CAS China
'''
import pyfits
import numpy
import matplotlib.pyplot as plt
from scipy import interpolate


filename="stars.dat"
fileobj=open(filename)
lines=fileobj.readlines()
fileobj.close()

wavelengthout=6100+numpy.linspace(0,724,725)*4
cols=numpy.logical_and(numpy.logical_or(wavelengthout>7700,wavelengthout<7500),numpy.logical_or(wavelengthout<6800,wavelengthout<7000))
wavelengthout=wavelengthout[cols]


fluxout=numpy.ones([len(lines),len(wavelengthout)])

for i in range(len(lines)):
	print i
	ss=lines[i].replace("\n","").split(",")
	
	fitsname=ss[10]
	hdulistlist=pyfits.open("fits/"+fitsname.upper().replace(".FIT",".fit"))
	wavelength=hdulistlist[0].header["CRVAL1"]+numpy.linspace(0,hdulistlist[0].header["NAXIS1"]-1,hdulistlist[0].header["NAXIS1"])*hdulistlist[0].header["CDELT1"]
	flux=hdulistlist[0].data
	tck = interpolate.interp1d(wavelength,flux,bounds_error=0,fill_value=0) 
	flux= tck(wavelengthout)
	flux=flux/numpy.sqrt(numpy.sum(flux*flux))
	fluxout[i]=flux
	plt.plot(wavelengthout,flux,'k')
	plt.xlabel("Wavelength($\AA$)")
	plt.ylabel("Flux")
	plt.title(ss[1])
	plt.ylim(numpy.min(flux),numpy.max(flux))
	plt.savefig("png/"+str(i)+"_"+fitsname+".png")
	plt.close()
	
numpy.savetxt("mk_flux.dat",fluxout)





