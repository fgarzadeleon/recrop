from medpy.io import load
from medpy.io import header

image_data, image_header = load('/home/ubuntu/dev/crf/CNNpredictions/DM_10000131_1_CTce_ThAb_29662_8_Segm.nii.gz')
imageOrig_data, imageOrig_header = load('/home/ubuntu/dev/crf/Volumes/DM_10000131_1_CTce_ThAb_29662_8.nii.gz')

print header.get_pixel_spacing(image_header)

print header.get_offset(image_header)

print header.get_pixel_spacing(imageOrig_header)

print header.get_offset(imageOrig_header)

