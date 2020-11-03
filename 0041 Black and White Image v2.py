import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image
# There are six more images available for reading
# called sample1-6.jpg, feel free to experiment with the others!
image_name = 'sample.jpg'
image = mpimg.imread(image_name)

# Define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    ###### TODO:
    # Create an empty array the same size in x and y as the image 
    # but just a single channel
    color_select = np.zeros_like(img[:,:,0])
    # Apply the thresholds for RGB and assign 1's 
    # where threshold was exceeded
    # Return the single-channel binary image
    return color_select

    # Create an empty array the same size in x and y as the image 
    # but just a single channel
        # Create an array of zeros same xy size as img, but single channel
    color_select = np.zeros_like(img[:,:,0])  # the numpy library's zeros_like function: Returns an array of zeros with the same shape and type as a given array.
                                              # Takes data of image (img) and creates an array of zeros with the same size in x and y as the image.  
                                              # The :,:,[0] input makes it an array with input from just a single channel, [0].  So that the array is exactly 1x as large.
        
    # Require that each pixel be above all three threshold values in RGB, (each pixel > all 3 RGB threshold values).
        # above_thresh will now contain a boolean array with "True"
        # wherever threshold is met.
    above_thresh = (img[:,:,0] > rgb_thresh[0]) \       # T/F?  0 = Red, image pixel is greater than Red.               (\ means continuation of line)
                & (img[:,:,1] > rgb_thresh[1]) \        # T/F?  1 = Green, image pixel is also (&) greater than Green.      
                & (img[:,:,2] > rgb_thresh[2])          # T/F?  2 = Blue, image pixel is also (&) greater than Blue.  
                                                        # Summary:  Where pixels ONLY larger than RGB are visible (White).  
    # Apply the thresholds for RGB and assign 1's 
    # where threshold was exceeded
    # Return the single-channel binary image
        # Index the array of zeros with the boolean array and set to 1.
    color_select[above_thresh] = 1   #The color_select array takes in the input of the boolean array above_thresh. is indexed to 1, wherever
        # Return the binary image
    return color_select 
    
# Define color selection criteria
###### TODO: MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
red_threshold = 0
green_threshold = 0
blue_threshold = 0
######
rgb_threshold = (red_threshold, green_threshold, blue_threshold)

# pixels below the thresholds
colorsel = color_thresh(image, rgb_thresh=rgb_threshold)

# Display the original image and binary               
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)
 
ax2.imshow(colorsel, cmap='gray')
ax2.set_title('Your Result', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
#plt.show() # Uncomment if running on your local machine
