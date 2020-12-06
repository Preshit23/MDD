import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops

def GLCM(segmented_image, masked_image):
    sub_image = segmented_image - masked_image
    sub_image = cv2.cvtColor(sub_image, cv2.COLOR_RGB2BGR)
    gray_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
    result = greycomatrix(gray_image, [1], [0, np.pi/2], levels=256)
    contrast = greycoprops(result, 'contrast')
    dissimilarity = greycoprops(result, 'dissimilarity')
    homogeneity = greycoprops(result, 'homogeneity')
    ASM = greycoprops(result, 'ASM')
    energy = greycoprops(result, 'energy')
    correlation = greycoprops(result,'correlation')
    feature_vector  =[contrast,dissimilarity,homogeneity,ASM,energy,correlation]
    return feature_vector