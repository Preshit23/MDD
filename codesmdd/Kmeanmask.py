import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops

image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Desktop\\apple.png')
cv2.imshow("Original",image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_values = image.reshape((-1, 3))
# convert to float
pixel_values = np.float32(pixel_values)
print(pixel_values.shape)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 4
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# convert back to 8 bit values
centers = np.uint8(centers)

# flatten the labels array
labels = labels.flatten()
# convert all pixels to the color of the centroids
segmented_image = centers[labels.flatten()]
# reshape back to the original image dimension
segmented_image = segmented_image.reshape(image.shape)
# show the image
plt.imshow(segmented_image)
plt.show()

#Masking the unwanted regions to extract ROI

# disable only the cluster number 2 (turn the pixel into black)
masked_image = np.copy(segmented_image)
# convert to the shape of a vector of pixel values
masked_image = masked_image.reshape((-1, 3))
# color (i.e cluster) to disable
cluster = 1

masked_image[labels == cluster] = [0, 0, 0]

# convert back to original shape
masked_image = masked_image.reshape(image.shape)
# show the image
plt.imshow(masked_image)
plt.show()

#Grayscale

sub_image = segmented_image - masked_image
sub_image = cv2.cvtColor(sub_image, cv2.COLOR_RGB2BGR)
gray_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray_image)
cv2.waitKey(0)

#now GLCM finallyyyyyy damnnn
result = greycomatrix(gray_image, [1], [0, np.pi/2], levels=256)
contrast = greycoprops(result, 'contrast')
dissimilarity = greycoprops(result, 'dissimilarity')
homogeneity = greycoprops(result, 'homogeneity')
ASM = greycoprops(result, 'ASM')
energy = greycoprops(result, 'energy')
correlation = greycoprops(result,'correlation')
feature_vector  =[contrast,dissimilarity,homogeneity,ASM,energy,correlation]
print("Features=")
print(feature_vector)
