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
import function
hdulist=pyfits.open("spEigenStar-55734.fits")

wavelengthStart=3800
wavelengthEnd=9000
wavelength=6100+numpy.linspace(0,724,725)*4
cols=numpy.logical_and(numpy.logical_or(wavelength>7700,wavelength<7500),numpy.logical_or(wavelength<6800,wavelength>7000))
wavelength=wavelength[cols]


wavelengthStart=3800
wavelengthEnd=9000
wavelengA=numpy.linspace(0,wavelengthEnd-wavelengthStart,wavelengthEnd-wavelengthStart+1)+wavelengthStart



for i in range(0,300):
	dr9_template=numpy.matrix(numpy.loadtxt("mk_flux.dat"))
	print i
	filename="../result/"+str(i)+"/templatespectra.txt"
	if os.path.exists(filename):
		#flux=numpy.matrix(numpy.loadtxt(filename)).getT()
		#flux=numpy.matrix(flux/numpy.sqrt(numpy.sum(flux*flux.getT())))
		dis=numpy.ones(len(dr9_template))
		fluxA=numpy.loadtxt(filename)
		tck = interpolate.interp1d(wavelengA,fluxA,bounds_error=0,fill_value=0) 
		flux= tck(wavelength)
		for j in range(len(dr9_template)):
			
			#dis[j]=numpy.sqrt(numpy.sum(numpy.power((flux-dr9_template[j]),2)))
			#dis[j]=1-flux*dr9_template[j].getT()
			fluxA=numpy.matrix(dr9_template[j,:]).getT()
			print flux.shape,fluxA.shape
			p=numpy.polyfit(wavelength,fluxA/flux,4)
			
			wp=numpy.polyval(p,wavelength)
			wp=numpy.matrix(wp).getT()
			
			#
			fluxA=fluxA/wp
			dis[j]=1-function.sim(flux,fluxA)
			dr9_template[j]=fluxA[:,:].getT()
			
		index=numpy.argsort(dis)
		
		#index=index[0]
		#print index.shape
		plt.figure(num=None, figsize=(10, 10), dpi=100, facecolor='w', edgecolor='k')
		ax=plt.subplot(5,1,1)
		ax.plot(wavelength,flux,'k')
		#ax.plot(wavelength,c,'r--')
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
				ax.plot(wavelength[cc],flux[cc],'k')
				ax.plot(wavelength[cc],dr9_template[index[j],:].getT()[cc],'r--')
				#plt.ylim([numpy.min(numpy.min(flux),numpy.min(mk_template[index[j]])),numpy.max(numpy.max(flux),numpy.max(mk_template[index[j]]))])
			
				[y0,y1]=ax.get_ylim()
				if k==0:
					cname=hdulist[0].header["NAME"+str(index[j])]

					cname=cname[0:cname.find("(")]
					ax.text(wa[0]-width[0]/2,y1-(y1-y0)*0.9,cname)
				plt.setp( ax.get_yticklabels(), visible=False)
				
				plt.setp( ax.get_xticklabels(), visible=False)
				if j==3 :
					plt.xlabel(linename[k])
				
					

			
		#plt.plot(wavelengthout,mk_template[index[0,0],:].getT(),'r--')
		
		#plt.show()

			
		plt.savefig("dr9_png/t_dr9_"+str(i).zfill(3)+".png")
		plt.close()
