import cv2
import numpy as np
import matplotlib.pyplot as plt
def shape(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #plt.imshow(img)
    #plt.show()

    #mask
    lower = np.array([0,30,0])
    higher = np.array([250,250,250])
    mask = cv2.inRange(img,lower,higher)
    #plt.imshow(mask,'gray')
    #plt.show()

    cont,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #seperating contour with max area
    c = max(cont,key = cv2.contourArea)


    c_img = cv2.drawContours(img,c,-1,255,3)
    #plt.imshow(c_img)
    #plt.show()
    #shape features
    M = cv2.moments(c)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)
    x,y,w,h = cv2.boundingRect(c)
    aspect_ratio = float(w)/h
    rectangularity = w*h/area
    circularity = ((perimeter)**2)/area


    vect = [area,perimeter,aspect_ratio,rectangularity,circularity]

    return vect