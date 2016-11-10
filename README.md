# recrop

`recrop` is a package aimed at reducing computational processing and time. It provides functions to crop images and reduce image resolutions for use in machine learning algorithms. In turn it provides functions to reconstruct the images into original sizes and resolutions.

## Packages required 

Packages required `numpy` and `medpy.io`, to install type in the command line

`pip install numpy`

and 

`pip install medpy.io`

## How to install

To install the package, type in your command line the following:

`pip install recrop`

## Available functions
```python
crop_3D(image, Coords)
```
Crop an image image at the inputted coordenates

```python
uncrop_3D(image, Coords, originalSize)
```
Reconstruct full size image from a cropped image

```python
 bbox_3D(img)
```
Get the bounding box of a segmented image

```python 
resample(img, hdr, target_spacing, bspline_order=3, mode='constant')
```

Re-sample an image to a new voxel-spacing. Taken form medpy.io.

```python
reconstruct_3D(*arg)
```
Reconstruct full size image from a cropped image

## Test file & runthrough
We used publicly available data and created a manual lesion to work with. 

Use the `test.py` file to learn how to use the package.

#### Loading an image
We need to use the `medpy.io` and `numpy` packages. We import our package as `recrop`. We also load our manual test image using the `load()` function from `medpy.io`.

```python
from medpy.io import load
from medpy.io import header
from medpy.io import save
import numpy as np
import recrop as recrop

# Manually segmented fake lesion for use with this example

image_file = 'data/manualTest.nii.gz'
image_data, image_header = load(image_file)
```

#### Cropping an image
To crop an image you must first provide the coordenates (two values per dimension) of the 3D box you want to crop. You can provide these manually or we `recrop.bbox_3D()` can find the minimum box that contains all the segmented regions.

Using `recrop.crop_3D()` you provide the image data and the coordenates and it will output the cropped image. 

```python
# Provide the coordenates or calculate the bounding box of the segmentation
coords2crop = [0,10,0,10,0,10]
coords2crop = recrop.bbox_3D(image_data)
print coords2crop

# Crop the image using the provided coordinates
croppedImage = recrop.crop_3D(image_data, coords2crop)
```

#### Chaging the resolution of an image

From the `header` function of `medpy.io` we can obtain the current pixel spacing for each dimension.

```python
# Print the pixel spacing
print header.get_pixel_spacing(image_header)

targetSpacing = 2.0
targetSpacing = [2.0, 1.0, 1.0]

# Resample from 
croppedResampledImage, croppedResampledImage_header = recrop.resample(croppedImage, image_header,targetSpacing)

```
#### Saving the cropped and target spaced images

You can save the the cropped and changed target space images with the `save` function from `medpy.io`.

```python
save(croppedImage, image_file[0:-7]+'.bbox.nii.gz', image_header)
save(croppedResampledImage, image_file[0:-7]+'.bboxResample.nii.gz', croppedResampledImage_header)
print 'Original:'
print croppedImage.shape
print 'Resampled:'
print croppedResampledImage.shape
```

The output should be the following:

```bash
Original:
(17, 25, 19)
Resampled:
(9, 25, 19)
```

As you can see by changing the image spacing we've changed the resolution of one dimension.

#### Changing back to the original resolution

The original target spacing was `1.0` so we use the `recrop.resample()` function to return it to its original spacing.

```python
targetSpacing = 1.0

croppedRegeneratedImage, croppedRegeneratedImage_header = recrop.resample(croppedResampledImage, croppedResampledImage_header, targetSpacing)

print 'Regenerated:'
print croppedRegeneratedImage.shape

save(croppedRegeneratedImage, image_file[0:-7]+'.bboxRegenerated.nii.gz', croppedRegeneratedImage_header)
```
The output should give you the size of the segmented image.

```bash
Regenerated:
(17, 25, 19)
```

#### Taking the cropped image and making it the same size as the original image

In some cases for comparison of the segmentations we want to take the smaller, cropped image and reconstruct it into the same size as the original image from which it was cropped.

The functions `recrop.uncrop_3D()` or `recrop.reconstruct_3D()` generate the same size image from the original image, using the cropped image.

```python
uncroppedImage = recrop.uncrop_3D(croppedImage,coords2crop,image_data.shape)

print 'Uncropped:'
print uncroppedImage

reconstructed = recrop.reconstruct_3D(image_file,image_file[0:-7]+'.bbox.nii.gz',coords2crop)

save(reconstructed, image_file[0:-7]+'.rc.nii.gz', image_header)
```

The only difference between the two is the arguments you send to the functions. `recrop.uncrop_3D()` takes in similar arguments as before, the image, coordenates and size of the original image. Whilst `recrop.reconstruct_3D()` works with the filenames.


## Data 
The data used can be found at [http://hdl.handle.net/1926/1714](http://hdl.handle.net/1926/1714)

Title: Lupus001
Authors: Jeremy Bockholt, Mark Scully
Institution: The MIND Research Network
Publication date: 2010-04-12 14:23
Modification date: 2010-04-12 14:23:23-04

### License for the data 
This work is licensed under the Creative Commons 3.0 Unported License.

You are free:
  * to Share - to copy, distribute and transmit the work
  * to Remix - to adapt the work

Under the following conditions:
  * Attribution. You must attribute the work in the manner specified by the author or licensor 
   (but not in any way that suggests that they endorse you or your use of the work).

To view a copy of this license, visit http://creativecommons.org/licenses/by-a/3.0/ 
or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.