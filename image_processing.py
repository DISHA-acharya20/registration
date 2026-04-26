import os.path
from skimage.io import imread, imsave
from skimage import data_dir
import matplotlib.pyplot as plt
import numpy as np

# Load the original image
img = imread(os.path.join(data_dir, 'ihc.png'))

# Display original image
plt.figure()
plt.imshow(img)
plt.title('Original Image')

# Create copies for processing
h_slice = img.copy()
v_slice = img.copy()

# Split horizontally into 2 parts
h_slice = np.hsplit(h_slice, 2)

# Split vertically into 4 parts
v_slice = np.vsplit(v_slice, 4)

# Display one of the horizontal splits
plt.figure()
plt.imshow(h_slice[1])
plt.title('Horizontal Split [1]')

# Merge horizontally (swap the parts)
h_stack = np.hstack((h_slice[1], h_slice[0]))

# Merge vertically (stack parts 1 and 0)
v_stack = np.vstack((v_slice[1], v_slice[0]))

# Display horizontal merge
plt.figure()
plt.imshow(h_stack)
plt.title('Horizontal Merge')

# Display vertical merge
plt.figure()
plt.imshow(v_stack)
plt.title('Vertical Merge')

# Show all plots
plt.show()

# Optionally save the results
imsave('h_stack.png', h_stack)
imsave('v_stack.png', v_stack)