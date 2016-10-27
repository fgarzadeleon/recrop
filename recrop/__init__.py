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


