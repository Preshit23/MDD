
import mahotas as mt
import numpy as np
import cv2


def texture(img):
    gs  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray',gs)
    # cv2.waitKey(500)
    # cv2.destroyAllWindows()
    textures = mt.features.haralick(gs)
    ht_mean = textures.mean(axis=0)
    contrast = ht_mean[1]
    correlation = ht_mean[2]
    inverse_diff_moments = ht_mean[4]
    entropy = ht_mean[8]
    vect = [contrast,correlation,inverse_diff_moments,entropy]

    return vect