from medpy.io import load
from medpy.io import header
from medpy.io import save
import numpy as np
import recrop as recrop

# Manually segmented fake lesion for use with this example

image_file = 'data/manualTest.nii.gz'
image_data, image_header = load(image_file)

# Provide the coordenates or calculate the bounding box of the segmentation
coords2crop = [0,10,0,10,0,10] # You can do manual coordenates
coords2crop = recrop.bbox_3D(image_data) # Or calculated by a boundary box
print coords2crop

# Crop the image using the provided coordinates
croppedImage = recrop.crop_3D(image_data, coords2crop)

# Print the pixel spacing
print header.get_pixel_spacing(image_header)

targetSpacing = 2.0
targetSpacing = [2,1,1]

# Resample from 
croppedResampledImage, croppedResampledImage_header = recrop.resample(croppedImage, image_header,targetSpacing)




save(croppedImage, image_file[0:-7]+'.bbox.nii.gz', image_header)
save(croppedResampledImage, image_file[0:-7]+'.bboxResample.nii.gz', croppedResampledImage_header)
print 'Original:'
print croppedImage.shape
print 'Resampled:'
print croppedResampledImage.shape

targetSpacing = 1.0

croppedRegeneratedImage, croppedRegeneratedImage_header =
recrop.resample(croppedResampledImage, croppedResampledImage_header,
targetSpacing)

print 'Regenerated:'
print croppedRegeneratedImage.shape

save(croppedRegeneratedImage, image_file[0:-7]+'.bboxRegenerated.nii.gz', croppedRegeneratedImage_header)


uncroppedImage = recrop.uncrop_3D(croppedImage,coords2crop,image_data.shape)

print 'Uncropped:'
print uncroppedImage

reconstructed = recrop.reconstruct_3D(image_file,image_file[0:-7]+'.bbox.nii.gz',coords2crop)

save(reconstructed, image_file[0:-7]+'.rc.nii.gz', image_header)
