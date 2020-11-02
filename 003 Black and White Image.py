#STEP 1:  Get the image.  

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







# Define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    ####### TODO 
    # Create an empty array the same size in x and y as the image 
        # but just a single channel
    # Apply the thresholds for RGB and 
        # assign 1's where threshold was exceeded
    return binary_image
