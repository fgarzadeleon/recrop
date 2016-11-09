# recrop

`recrop` is a package aimed to reduce computational processing and time. It provides functions to crop images and reduce image resolutions for use in machine learning algorithms. In turn it provides functions to reconstruct the images into original sizes and resolutions.

## PAckages required 

Packages required `numpy` and `medpy.io`, to install type in the command line

`pip install numpy`

and 

`pip install medpy.io`

## How to install

To install the package, type in your command line the following:

`pip install recrop`

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

```python
# Provide the coordenates or calculate the bounding box of the segmentation
coords2crop = [0,10,0,10,0,10]
coords2crop = recrop.bbox_3D(image_data)
print coords2crop

# Crop the image using the provided coordinates
croppedImage = recrop.crop_3D(image_data, coords2crop)
```





### Data 
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