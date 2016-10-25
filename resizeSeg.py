from medpy.io import load
from medpy.io import header
import numpy as np

def crop3D(image, Coords):
	croppedImage = None
	if (len(image.shape)==3) & (len(Coords)==6):
		croppedImage = image[Coords[0]:Coords[1],Coords[2]:Coords[3],Coords[4]:Coords[5]]
		return croppedImage
	else:
		print "The array or coordenates do not have 3 dimensions"
		return croppedImage

def uncrop3D(image, Coords, originalSize):
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



image_data, image_header = load('10000001_3_MRT1_wb_29662_4.nii.gz')
imageOrig_data, imageOrig_header = load('10000001_3_MRT1_wb.nii.gz')

print header.get_pixel_spacing(image_header)

print header.get_offset(image_header)

print header.get_pixel_spacing(imageOrig_header)

print header.get_offset(imageOrig_header)

data_dim = imageOrig_data.shape

coords2crop = [5,10,5,10,5,10]

croppedImage = crop3D(imageOrig_data, coords2crop)

uncroppedImage = uncrop3D(croppedImage,coords2crop,image_data.shape)

