import numpy as np
from scipy.ndimage.interpolation import zoom
from medpy.io import header
import numbers



def crop_3D(image, Coords):
	croppedImage = None
	if (len(image.shape)==3) & (len(Coords)==6):
		croppedImage = image[Coords[0]:Coords[1],Coords[2]:Coords[3],Coords[4]:Coords[5]]
		return croppedImage
	else:
		print "The array or coordenates do not have 3 dimensions"
		return croppedImage

def uncrop_3D(image, Coords, originalSize):
	uncroppedImage = None
	if (len(image.shape)==3) & (len(Coords)==6) & (len(originalSize)==3):
		if (Coords[0]<originalSize[0]) & (Coords[1]<originalSize[0]) & (Coords[2]<originalSize[1]) & (Coords[3]<originalSize[1]) & (Coords[4]<originalSize[2]) & (Coords[5]<originalSize[2]): 
			uncroppedImage = np.zeros(originalSize)
			uncroppedImage[Coords[0]:Coords[1],Coords[2]:Coords[3],Coords[4]:Coords[5]] = image
			return uncroppedImage
		else:
			return "Original size is smaller than the supplied coordenates"
			return uncroppedImage
	else:
		print "The array, coordenates or original size do not have 3 dimensions"
		return uncroppedImage		

def bbox_3D(img):

    r = np.any(img, axis=(1, 2))
    c = np.any(img, axis=(0, 2))
    z = np.any(img, axis=(0, 1))

    rmin, rmax = np.where(r)[0][[0, -1]]
    cmin, cmax = np.where(c)[0][[0, -1]]
    zmin, zmax = np.where(z)[0][[0, -1]]

    return rmin, rmax, cmin, cmax, zmin, zmax

def resample(img, hdr, target_spacing, bspline_order=3, mode='constant'):
        """
        Re-sample an image to a new voxel-spacing.
        
        Parameters
        ----------
        img : array_like
            The image.
        hdr : object
            The image header.
        target_spacing : number or sequence of numbers
            The target voxel spacing to achieve. If a single number, isotropic spacing is assumed.
        bspline_order : int
            The bspline order used for interpolation.
        mode : str
            Points outside the boundaries of the input are filled according to the given mode ('constant', 'nearest', 'reflect' or 'wrap'). Default is 'constant'.
            
        Warning
        -------
        Voxel-spacing of input header will be modified in-place!
            
        Returns
        -------
        img : ndarray
            The re-sampled image.
        hdr : object
            The image header with the new voxel spacing.
        """
        if isinstance(target_spacing, numbers.Number):
            target_spacing = [target_spacing] * img.ndim
        
        # compute zoom values
        zoom_factors = [old / float(new) for new, old in zip(target_spacing, header.get_pixel_spacing(hdr))]
    
        # zoom image
        img = zoom(img, zoom_factors, order=bspline_order, mode=mode)
        
        # set new voxel spacing
        header.set_pixel_spacing(hdr, target_spacing)
        
        return img, hdr



