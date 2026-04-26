import os.path
from skimage.io import imread
from skimage import data_dir
import matplotlib.pyplot as plt
import numpy as np
# Original Image
img = imread(os.path.join(data_dir, 'ihc.png'))
plt.imshow(img)
h_slice = img.copy()
v_slice = img.copy()
h_slice = np.hsplit(h_slice,2)
v_slice = np.vsplit(v_slice,4)
''' Horizontal Split '''
plt.figure()
plt.imshow(h_slice[1])
h_stack = np.hstack( (h_slice[1],h_slice[0]) )
v_stack = np.vstack( (v_slice[1],v_slice[0]) )
''' Horizontal Merge '''
plt.figure()
plt.imshow(h_stack)
''' Vertical Merge '''
plt.figure()
plt.imshow(v_stack)
plt.show()