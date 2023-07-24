import cv2
import numpy as np
from scipy.signal import convolve2d

def create_line_kernel(length, angle):
    angle_rad = np.deg2rad(angle)
    x = np.cos(angle_rad) * np.arange(length)
    y = np.sin(angle_rad) * np.arange(length)
    x = np.clip(x, 0, length - 1)
    y = np.clip(y, 0, length - 1)

    kernel = np.zeros((length, length))
    kernel[np.round(y).astype(int), np.round(x).astype(int)] = 1

    return kernel

def convolve_with_line(image, length, angle):
    line_kernel = create_line_kernel(length, angle)
    convolved_image = convolve2d(image, line_kernel, mode='same', boundary='symm')

    return convolved_image

# Load the object image
object_image_path =  'C:\\Users\\us\\Documents\\Python\\classWork1\\liner.jpg'  # Replace with the actual path to the object image
object_image = cv2.imread(object_image_path, cv2.IMREAD_GRAYSCALE)

# Define line properties (length and angle)
line_length = 50
line_angle_degrees = 45

# Perform convolution of the object image with the straight line kernel
convolved_image = convolve_with_line(object_image, line_length, line_angle_degrees)

# Now you can use the 'convolved_image' as needed without displaying any figures.
# For example, you can save it to a file or use it for further processing.


