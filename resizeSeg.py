from medpy.io import load
from medpy.io import header
from medpy.io import save
import numpy as np
import recrop

def reconstruct_3D(*arg):
	uncroppedImage = None
	if (len(arg)==2):
		image_data, image_header = load(arg[0])
		imageSegmentation_data, imageSegmentation_header = load(arg[1])
		# Coords = image_header get coordenates from header
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
	


# Need to write to header
image_file = 'manualTest.nii.gz'
image_data, image_header = load(image_file)

coords2crop = [0,10,0,10,0,10]
coords2crop = recrop.bbox_3D(image_data)
print coords2crop

croppedImage = recrop.crop_3D(image_data, coords2crop)

croppedImage[:] = 21+croppedImage[:] 

save(croppedImage, image_file[0:-7]+'.bbox.nii.gz', image_header)

uncroppedImage = recrop.uncrop_3D(croppedImage,coords2crop,image_data.shape)

reconstructed = reconstruct_3D(image_file,image_file[0:-7]+'.bbox.nii.gz',coords2crop)

save(reconstructed, image_file[0:-7]+'.rc.nii.gz', image_header)


# OR using boundary boxes

coords2crop = recrop.bbox_3D(image_data)

croppedImage = recrop.crop_3D(image_data, coords2crop)

uncroppedImage = recrop.uncrop_3D(croppedImage,coords2crop,image_data.shape)