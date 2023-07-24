import cv2
import numpy as np

# Load the image in grayscale
image_path = 'C:\\Users\\us\\Documents\\Python\\ClassWork4\\FreQuency\\cat.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform the Fourier Transform (FFT)
fft_result = np.fft.fft2(image)

# Shift the zero frequency component to the center of the spectrum
fft_result_shifted = np.fft.fftshift(fft_result)

# Compute the magnitude spectrum (amplitude) for visualization
magnitude_spectrum = np.abs(fft_result_shifted)

# Normalize the magnitude spectrum to 8-bit grayscale range (0 to 255)
magnitude_spectrum = (magnitude_spectrum / np.max(magnitude_spectrum)) * 255
magnitude_spectrum = magnitude_spectrum.astype(np.uint8)

# Save the magnitude spectrum as a grayscale image
output_path = 'magnitude_spectrum.jpg'  # Replace with the desired output path and filename
cv2.imwrite(output_path, magnitude_spectrum)

print("Magnitude spectrum saved as", output_path)

