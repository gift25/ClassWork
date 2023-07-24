import cv2
import numpy as np

def horizontal_sobel_filter(image):
    # Horizontal Sobel Filter
    sobel_filter = np.array([[-1, -2, -1],
                             [0, 0, 0],
                             [1, 2, 1]])
    
    # Ensure the image is in grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convolve the image with the Sobel filter
    filtered_image = cv2.filter2D(image, -1, sobel_filter)
    return filtered_image

# Load an example image
image_path = 'C:/Users/us/Documents/Python/SobelFilter/cat.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Apply the Horizontal Sobel Filter
filtered_image = horizontal_sobel_filter(image)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image (Horizontal Sobel)', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
