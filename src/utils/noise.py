import cv2
import math
import numpy as np
import scipy.stats as st


def gaussian_blur(img, sigma=1):
    ''' Apply gaussian blur with kernel_size of (3*sigma) * 2 + 1 '''
    kernel_size = int(math.ceil(3 * sigma) * 2 + 1)
    blur = cv2.GaussianBlur(img, ksize=(kernel_size, kernel_size), sigmaX=sigma, sigmaY=sigma)
    return blur


def white_noise(img, noise_std=0.3):
    ''' Copying SJL's implementation from pose-hg-syn '''
    noise = np.random.randn(*img.shape) * noise_std
    img_one = img / 255.0  # Between 0 and 1

    # Add noise
    img_one_w_noise = (img_one + noise).clip(0, 1)

    # Rescale back to 0-255 scale
    img_white_noise = img_one_w_noise * 255.
    return img_white_noise

