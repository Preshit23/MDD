import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops
import matplotlib.pyplot as plt

def GLCM(segmented_image, masked_image):
    sub_image = segmented_image - masked_image
    plt.imshow(sub_image)
    plt.show()
    sub_image = cv2.cvtColor(sub_image, cv2.COLOR_RGB2BGR)
    x = int(input("x coordinate crop :"))
    y = int(input("y coordinate crop :"))
    w = int(input("w coordinate crop :"))
    h = int(input("h coordinate crop :"))
    crop_img = sub_image[y:y + h, x:x + w]
    cv2.imshow("Cropped",crop_img)
    gray_image = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    result = greycomatrix(gray_image, [1], [0, np.pi/2], levels=256)
    contrast = greycoprops(result, 'contrast')
    dissimilarity = greycoprops(result, 'dissimilarity')
    homogeneity = greycoprops(result, 'homogeneity')
    ASM = greycoprops(result, 'ASM')
    energy = greycoprops(result, 'energy')
    correlation = greycoprops(result,'correlation')
    feature_vector  =np.array([contrast[0],dissimilarity[0],homogeneity[0],ASM[0],energy[0],correlation[0]])
    print("Feature vector:")
    print(feature_vector)
    return feature_vector