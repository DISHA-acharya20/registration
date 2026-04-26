import os.path
from skimage.io import imread, imsave
from skimage import data_dir
img = imread(os.path.join(data_dir, 'checker_bilevel.png'))
imsave('checker_bilevel.png', img)