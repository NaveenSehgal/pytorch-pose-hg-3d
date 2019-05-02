import cv2
import math
import numpy as np
import scipy.stats as st


def gaussian_blur(img, sigma=1):
    ''' Apply gaussian blur with kernel_size of (3*sigma) * 2 + 1 '''
    kernel_size = int(math.ceil(3 * sigma) * 2 + 1)
    blur = cv2.GaussianBlur(img, ksize=(kernel_size, kernel_size), sigmaX=sigma, sigmaY=sigma)
    return blur, blur2


def white_noise(img, noise_std=0.3):
    ''' Copying SJL's implementation from pose-hg-syn '''
    noise = np.random.randn(*img.shape) * noise_std
    img_one = img / 255.0  # Between 0 and 1

    # Add noise
    img_one_w_noise = (img_one + noise).clip(0, 1)

    # Rescale back to 0-255 scale
    img_white_noise = img_one_w_noise * 255.
    return img_white_noise


# Test
if __name__ == '__main__':
	img_path = '/home/naveen/synthetic/SYN_RR_amir_180329_0624_G20190212_1843_P2000_A00/images/image_000001.png'
	img = cv2.imread(img_path)
	blur, blur2 = gaussianBlur(img)
	wnoise = white_noise(img)

	cv2.imwrite('orig.png', img)
	cv2.imwrite('blur.png', blur)
	cv2.imwrite('wnoise.png', wnoise)
	cv2.imwrite('blur2.png', blur2)
