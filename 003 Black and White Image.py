"""
Plan:  
	First, we must import the image file.  
	Then, we get the image information.  
	Then, we create the function empty array according to the size in x and y as the image.  
	Then, we make it just a single channel.  
	Then, we apply the thresholds for RGB.
	Then, we assign 1's where threshold was exceeded.  
"""

#STEP 1:  Get the image, i.e. Import the image file.  

# Import some packages from matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
	
# Uncomment the next line for use in a Jupyter notebook
#%matplotlib inline
	
# Define the filename, read and plot the image
filename = 'sample.jpg'
image = mpimg.imread(filename)
plt.imshow(image)
plt.show()

#STEP 2:  Insert image into an array.  
	#STEP 2.1 Import numpy, to work with arrays.  

# Import the "numpy" package for working with arrays
import numpy as np
print(image.dtype, image.shape, np.min(image), np.max(image)) 
# uint8 (160, 320, 3) 0 255
# returns datatype (uint8), shape {size of the array is (160, 320, 3)}, min (0), max (255).  2^8 = 256 = limit of int datatype.  
# meaning the image size is 160 pixels in the y-direction (height), 320 pixels in the x-direction (width) and it has 3 layers or "color channels" (Red, Green, Blue).  

# We can also see that the minimum and maximum values are 0 and 255, respectively. 
# This comes from the fact that with 8 bits of information for each pixel in each color channel, 
# you have 2^8 or 256 possible values, with the minimum possible value being 0 and the maximum being 255. 
# Not all images are scaled this way so it's always a good idea to check the range and data type of the array after reading in an image if you're not sure.



# Define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    ####### TODO 
    # Create an empty array the same size in x and y as the image 
        # but just a single channel
    # Apply the thresholds for RGB and 
        # assign 1's where threshold was exceeded
    return binary_image
