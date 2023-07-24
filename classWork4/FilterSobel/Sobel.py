import numpy as np
import matplotlib.pyplot as plt

# Sobel Filter (Horizontal Sobel)
sobel_filter_horizontal = np.array([[-1, -2, -1],
                                    [0, 0, 0],
                                    [1, 2, 1]], dtype=np.float32)

# Perform the Fourier Transform (FFT) on the Sobel Filter
sobel_filter_fft = np.fft.fft2(sobel_filter_horizontal)

# Shift the zero frequency component to the center of the spectrum
sobel_filter_fft_shifted = np.fft.fftshift(sobel_filter_fft)

# Compute the magnitude spectrum (amplitude) for visualization
magnitude_spectrum = np.abs(sobel_filter_fft_shifted)

# Display the magnitude spectrum
plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
plt.title('Magnitude Spectrum of Sobel Filter')
plt.colorbar()
plt.show()
