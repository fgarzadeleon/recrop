## Project
* output that's compatible with original data
* Segmentation current output, 1by1by1 resolution
* Scale it back up to original resolution

original scan, read resolution and apply that resolution

take cropped kidney

unseen scan, cropping

output of crf cropped image, resolution

information is in heaeder files, you know where the image was cropped out of 

* coordenates are in the header where the kidney was taken from

Script how he cropped image

1. Start Original data
2. crop something out
3. resample resolution, function called resampled, 3 numbers resample to new resolution
	1. Paste that back 
3. cropped image, how to paste back in the scan

### Downsample file

deepRenal / utils / createDMdb.py

for loop loops through volumes, two loops two kidneys

bbox calculates corners of kidney

region function takes input

### Data

One Segmentation file

### Pip install

Fede import fede to use function

### Small goal

0800 561 00 61

Load nifti file, convert it into numpy matrix

crop it and save

extract submatrix withing that and save it into a nifti file

### Coords

If six coordenates supplied then use that if not read from header

Medpy.io resample
