import cv2 as cv
import random
import cv2

img = cv2.imread('C:/Users/us/Documents/Python/classWork3/aniea.jpg')


densit_salt = 0.1
density_pepper = 0.1

# Set number of white pixel (salt)
number_of_white_pixel = int( densit_salt * (img.shape[0] * img.shape[1]))

#Add salt to the image
for i in range(number_of_white_pixel):
        y_coord = random.randint(0, img.shape[0] -1)
        x_coord = random.randint(0, img.shape[1]-1)
        img[y_coord ][x_coord]= 255


# Set number of black pixel (pepper)
number_of_black_pixel = int( density_pepper *(img.shape[0] * img.shape[1]))
# Add pepper to the image
for i in range(number_of_black_pixel):
        y_coord = random.randint(0, img.shape[0]-1)
        x_coord = random.randint(0, img.shape[1]-1)
        img[y_coord ][x_coord] = 0

cv.imwrite('noise.png', img)

# Load the noisy image
noisy_img = cv.imread('noise.png', cv.IMREAD_GRAYSCALE)

# Apply median filtering
denoised_img = cv.medianBlur(noisy_img, 5) # Adjust the kernel size (5 in this example)

# Save the denoised image
cv.imwrite('denoised.png', denoised_img)