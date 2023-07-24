import cv2
import numpy as np

def FourierTransform(img):
    img32 = img.astype(np.float32)  # Convert image data type to float32
    imgFourier = np.fft.fft2(img32)  # Apply Fourier Transform to the image
    imgFourier = np.fft.fftshift(imgFourier)
    # for magnitude spectrum
    imgReal = np.real(imgFourier)  # Extract the real component of the Fourier-transformed image
    imgImag = np.imag(imgFourier)  # Extract the imaginary component of the Fourier-transformed image
    imgMag = np.sqrt(imgReal**2 + imgImag**2)  # Calculate the magnitude spectrum
    imgMag = np.log(1 + imgMag)  # Compute the logarithm of the magnitude spectrum for visualization enhancement
    imgMag = cv2.normalize(imgMag, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)  # Normalize and convert the magnitude spectrum to uint8

    return imgFourier, imgMag

if __name__ == '__main__':

    img = cv2.imread('C:\\Users\\us\\Documents\\Python\\classWork4\\cat.jpg', 0)
    h, w = img.shape

    kernel_vert = np.array([
                            [1, 0, -1],  # Vertical Sobel filter Kernel
                            [2, 0, -2],
                            [1, 0, -1]
                        ])
    
    kernel_length = len(kernel_vert)
   
    kernel_pad = np.pad(kernel_vert, ((h // 2 , h // 2 - kernel_length), (w // 2 , w // 2 - kernel_length)), mode='constant')
    kernel = np.fft.fftshift(kernel_pad)
  
    filterF, filterMag = FourierTransform(kernel)
    imgF, imgMag = FourierTransform(img)
    cv2.imwrite('img.png', imgMag)
    cv2.imwrite('filter.png', filterMag)
  
    imgF_np = np.array(imgF)
    filterF_np = np.array(filterF)
   
    filterF_np = filterF_np.astype(np.float32)

    filterF_resized = cv2.resize(filterF_np, (imgF_np.shape[1], imgF_np.shape[0]), interpolation=cv2.INTER_LINEAR)

    dotProduct = imgF_np * filterF_resized

    imgF_filtered = np.fft.ifftshift(dotProduct)
    imgF_filtered = np.fft.ifft2(imgF_filtered)
    filtered = np.real(imgF_filtered)
    imgF_filtered = cv2.normalize(filtered, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)  # Normalize the filtered image
    cv2.imshow('Frequency domain', imgF_filtered)
    cv2.imwrite('Sobel-Frequency.png', imgF_filtered)


    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobelX = cv2.normalize(sobelX, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    cv2.imshow('Spatial domain', sobelX)
    cv2.imwrite('Sobel-Spatial.png', sobelX)

    compare_pics = np.concatenate((imgF_filtered, sobelX), axis=1)
    cv2.imshow('Frequency and Spatial domain', compare_pics)

    cv2.waitKey(0)
    cv2.destroyAllWindows()