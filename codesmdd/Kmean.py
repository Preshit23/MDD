import cv2
import numpy as np
import matplotlib.pyplot as plt

def KM(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = 5
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    labels = labels.flatten()
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)
    plt.imshow(segmented_image)
    plt.show()
#For cluster = 1
    masked_image = np.copy(segmented_image)
    masked_image = masked_image.reshape((-1, 3))
    cluster = 1
    masked_image[labels == cluster] = [0, 0, 0]
    masked_image = masked_image.reshape(image.shape)
    plt.title("Cluster = 1")
    plt.imshow(masked_image)
    plt.show()
# For cluster = 2
    masked_image = np.copy(segmented_image)
    masked_image = masked_image.reshape((-1, 3))
    cluster = 2
    masked_image[labels == cluster] = [0, 0, 0]
    masked_image = masked_image.reshape(image.shape)
    plt.title("Cluster = 2")
    plt.imshow(masked_image)
    plt.show()
# For cluster = 3
    masked_image = np.copy(segmented_image)
    masked_image = masked_image.reshape((-1, 3))
    cluster = 3
    masked_image[labels == cluster] = [0, 0, 0]
    masked_image = masked_image.reshape(image.shape)
    plt.title("Cluster = 3")
    plt.imshow(masked_image)
    plt.show()
# For cluster = 4
    masked_image = np.copy(segmented_image)
    masked_image = masked_image.reshape((-1, 3))
    cluster = 4
    masked_image[labels == cluster] = [0, 0, 0]
    masked_image = masked_image.reshape(image.shape)
    plt.title("Cluster = 4")
    plt.imshow(masked_image)
    plt.show()
 # For cluster = 5
    masked_image = np.copy(segmented_image)
    masked_image = masked_image.reshape((-1, 3))
    cluster = 5
    masked_image[labels == cluster] = [0, 0, 0]
    masked_image = masked_image.reshape(image.shape)
    plt.title("Cluster = 5")
    plt.imshow(masked_image)
    plt.show()

# Selection time
    masked_image = np.copy(segmented_image)
    masked_image = masked_image.reshape((-1, 3))
    cluster = int(input("cluster which is infected = "))
    masked_image[labels == cluster] = [0, 0, 0]
    masked_image = masked_image.reshape(image.shape)
    plt.imshow(masked_image)
    plt.show()
    return masked_image , segmented_image