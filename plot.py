import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
from PIL import Image

image_path = r'C:\Image\Encrypted\scenery.png'
image = Image.open(image_path).convert('RGB')
image_array = np.array(image)

# Plot the histogram
plt.hist(image_array.ravel(), bins=256, color='r')
plt.show()
plt.hist(image_array[:,:,1].ravel(), bins=256, color='g')
plt.show()
plt.hist(image_array[:,:,2].ravel(), bins=256, color='b')
plt.show()

# Load the image
img = cv2.imread(r'C:\Image\Encrypted\scenery.png')

# Calculate the histogram
hist, bins = np.histogram(img.ravel(), 256, [0,256])

# Calculate the probability density function
pdf = hist / np.sum(hist)
epsilon = 1e-12
pdf[pdf == 0] = epsilon
# Calculate the entropy
entropy = -np.sum(pdf * np.log2(pdf))

print(f"Entropy of the Image: {entropy:0.4f}")
