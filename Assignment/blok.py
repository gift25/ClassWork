import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



img = cv.imread('C:/Users/us/Documents/Python/Assignment/Nasion.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()




img = cv.imread('C:/Users/us/Documents/Python/Assignment/Nasion.jpg',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()



img = cv.imread('C:/Users/us/Documents/Python/Assignment/Nasion.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()




import cv2





# Read the image
img = cv2.imread('C:/Users/us/Documents/Python/Assignment/Nasion.jpg', 0)

# Create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255

# Apply the mask to the image using bitwise AND
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Calculate histograms with and without the mask
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

# Plot the original image, mask, masked image, and histograms
plt.subplot(221), plt.imshow(img, 'gray')
plt.title('Original Image')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('Mask')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.title('Masked Image')
plt.subplot(224)
plt.plot(hist_full, color='b')
plt.plot(hist_mask, color='r')
plt.xlim([0, 256])
plt.title('Histograms')
plt.legend(['Full Image', 'Masked Region'])
plt.show()


# Read the image
img = cv2.imread('C:/Users/us/Documents/Python/Assignment/Nasion.jpg', 0)

# Create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255

# Apply the mask to the image using bitwise AND
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Calculate histograms with and without the mask
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

# Plot the original image, mask, masked image, and histograms
plt.subplot(221), plt.imshow(img, 'gray')
plt.title('Original Image')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('Mask')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.title('Masked Image')
plt.subplot(224)
plt.plot(hist_full, color='b')
plt.plot(hist_mask, color='r')
plt.xlim([0, 256])
plt.title('Histograms')
plt.legend(['Full Image', 'Masked Region'])
plt.show()
