import numpy as np
from scipy.ndimage.interpolation import zoom
from medpy.io import header
import numbers
from medpy.io import load




def crop_3D(image, Coords):
	"""
    Crop an image image at the inputted coordenates
        
    Parameters
    ----------
    image : array_like
        The image.
    Coords : ndarray
    	Coordenates of the bounding box: minimum and maximum columns, rows and 3rd dimension

    Returns
    -------
    croppedImage : array_like
    	The image that was cropped from the original image using the bounding box coordenates
    
    """
	croppedImage = None
	if (len(image.shape)==3) & (len(Coords)==6):
		croppedImage = image[Coords[0]:Coords[1],Coords[2]:Coords[3],Coords[4]:Coords[5]]
		return croppedImage
	else:
		print "The array or coordenates do not have 3 dimensions"
		return croppedImage

def uncrop_3D(image, Coords, originalSize):
	"""
    Reconstruct full size image from a cropped image
        
    Parameters
    ----------
    image : array_like
        The image.
    Coords : ndarray
    	Coordenates of the bounding box: minimum and maximum columns, rows and 3rd dimension
	originalSize : ndarray
		Original size of the image from which the cropped image was taken

    Returns
    -------
    uncroppedImage : array_like
    	Original size image reconstructed from the cropped image
    
    """	


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
	"""
    Get the bounding box of a segmented image
        
    Parameters
    ----------
    img : array_like
        The image.

    Returns
    -------
    rmin, rmax : ndarray
        Row minimum and maximum
    cmin, cmax : ndarray
        Column minimum and maximum
    zmin, zmax : 
    	3rd dimension minimum and maximum

    """
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

        print "Zoom Factors"
        print zoom_factors

        oldImageShape = img.shape
    
        # zoom image
        img = zoom(img, zoom_factors, order=bspline_order, mode=mode)

        newImageShape = img.shape
        old_pixel_spacing = header.get_pixel_spacing(hdr)

        new_pixel_spacing = np.divide(np.multiply(oldImageShape,old_pixel_spacing),newImageShape)

        print "Target Pixel Spacing"
        print target_spacing

        print "Actual Pixel Spacing"
        print new_pixel_spacing


        
        # set new voxel spacing
        header.set_pixel_spacing(hdr, new_pixel_spacing)
        
        return img, hdr

def reconstruct_3D(*arg):
	"""
    Reconstruct full size image from a cropped image
        
    Parameters
    ----------
    image : array_like
        The image.
    Coords : ndarray
    	Coordenates of the bounding box: minimum and maximum columns, rows and 3rd dimension
	originalSize : ndarray
		Original size of the image from which the cropped image was taken

    Returns
    -------
    uncroppedImage : array_like
    	Original size image reconstructed from the cropped image
    
    """	

	uncroppedImage = None
	if (len(arg)==2):
		return "You need to supply the bounding box coordinates"
	elif (len(arg)==3):
		image_data, image_header = load(arg[0])
		imageSegmentation_data, imageSegmentation_header = load(arg[1])
		Coords = arg[2]
		originalSize = image_data.shape
		if (len(image_data.shape)==3) & (all(np.greater(image_data.shape,imageSegmentation_data.shape))):
			if (Coords[0]<originalSize[0]) & (Coords[1]<originalSize[0]) & (Coords[2]<originalSize[1]) & (Coords[3]<originalSize[1]) & (Coords[4]<originalSize[2]) & (Coords[5]<originalSize[2]): 
				uncroppedImage = np.zeros(originalSize)
				uncroppedImage[Coords[0]:Coords[1],Coords[2]:Coords[3],Coords[4]:Coords[5]] = imageSegmentation_data
				return uncroppedImage
			else:
				return "Original size is smaller than the supplied coordenates"
				return uncroppedImage
		else:
			print "the original image is smaller than the segmentation."
			print "The array or coordenates do not have 3 dimensions"
			return uncroppedImage
	elif (len(arg)<2):
		print "Not enough arguments."
	elif (len(arg)>3):
		print "Too many arguments."
	croppedImage = None



