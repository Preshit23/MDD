import pandas as pd
from GLCM import *
from Kmean import *

#Storing Foiler disease
image = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\foilerstraw.png')
masked_image , segmented_image = KM(image)
feature_vector1 = ["Foiler",GLCM(segmented_image, masked_image)]
print(feature_vector1)


#Storing Rust disease
image1 = cv2.imread('C:\\Users\\Admin\\Downloads\\applerust.jpg')
masked_image , segmented_image = KM(image1)
feature_vector2 = ["Rust",GLCM(segmented_image, masked_image)]
print(feature_vector2)

#Storing Powdery Mildew disease
image2 = cv2.imread('C:\\Users\\Admin\\OneDrive\\Desktop\\powderymildew.png')
masked_image , segmented_image = KM(image2)
feature_vector3 = ["PowderyMildew",GLCM(segmented_image, masked_image)]
print(feature_vector3)





df1 = pd.DataFrame([feature_vector1,feature_vector2,feature_vector3])
df1.to_excel('test.xlsx')