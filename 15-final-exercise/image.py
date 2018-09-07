def image_plot(filename):
    import numpy as np
    import astropy.units as u
    from astropy.io import fits
    from astropy.wcs import WCS
    from astropy.wcs.utils import wcs_to_celestial_frame
    import sunpy.coordinates
    from astropy.coordinates import SkyCoord
    
    image=fits.getdata('WISE_12.fits')
    print(image.shape)
    
    hdulist=fits.open('WISE_12.fits')
    hdulist.verify('silentfix')
    
    wcs = WCS(hdulist[0].header)
    import matplotlib.pyplot as plt
    ax = plt.subplot(projection=wcs)   #normally has a projection=... keyword
    ax.imshow(hdulist[0].data, origin='lower')
    ax.coords.grid(hdulist[0].data,grid_type='contours',color='white',linewidth=0.3,linestyle='dashed')
    
    overlay = ax.get_coords_overlay('galactic')
    overlay.grid(color='orange', alpha=1, linestyle='solid')
    overlay['l'].set_axislabel("Galactic Longitude [degrees]")
    overlay['b'].set_axislabel("Galactic Latitude [degrees]")

    
image_plot('WISE_12.fits')
