# Import the "numpy" package for working with arrays
import numpy as np
print(image.dtype, image.shape, np.min(image), np.max(image))
# uint8 (160, 320, 3) 0 255

"""
So, here we can see it's an 8-bit unsigned integer array (uint8), 
where the size of the array is (160, 320, 3) meaning the image size is 160 pixels in the y-direction (height), 
320 pixels in the x-direction (width) and it has 3 layers or "color channels".
	
We can also see that the minimum and maximum values are 0 and 255, respectively. 
This comes from the fact that with 8 bits of information for each pixel in each color channel, 
you have 2^8 or 256 possible values, with the minimum possible value being 0 and the maximum being 255. 
Not all images are scaled this way so it's always a good idea to check the range and data type of the array 
after reading in an image if you're not sure.
	
The three color channels of the image are red, green and blue or "RGB" for short. 
"""
