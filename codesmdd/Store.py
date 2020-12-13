import pandas as pd
from GLCM import *
from Kmean import *
from preprocessing import *

#Storing AppleRust
image1 = cv2.imread('D:\\MDD\\Leaf images\\Applerust.jpg')
image1 = preprocess(image1)
masked_image1 , segmented_image1 = KM(image1)
feature_vector1 = GLCM(segmented_image1, masked_image1)
feature_vector1 = np.append(np.array(['Applerust']),feature_vector1)
print(feature_vector1)


#Storing Powdery Mildew
image2 = cv2.imread('D:\\MDD\\Leaf images\\powder.jpg')
image2 = preprocess(image2)
masked_image2 , segmented_image2 = KM(image2)
feature_vector2 = GLCM(segmented_image2, masked_image2)
feature_vector2 = np.append(np.array(['PowderyMildew']),feature_vector2)
print(feature_vector2)

#Storing Blight
image3 = cv2.imread('D:\\MDD\\Leaf images\\Blight.jfif')
image3 = preprocess(image3)
masked_image3 , segmented_image3 = KM(image3)
feature_vector3 = GLCM(segmented_image3, masked_image3)
feature_vector3 = np.append(np.array(['Blight']),feature_vector3)
print(feature_vector3)

#Storing Foiler
image4 = cv2.imread('D:\\MDD\\Leaf images\\foiler.jpg')
image4 = preprocess(image4)
masked_image4 , segmented_image4 = KM(image4)
feature_vector4 = GLCM(segmented_image4, masked_image4)
feature_vector4 = np.append(np.array(['Foiler']),feature_vector4)
print(feature_vector4)

#Storing Downy Mildew
image5 = cv2.imread('D:\\MDD\\Leaf images\\downyMildew.jpeg')
image5 = preprocess(image5)
masked_image5 , segmented_image5 = KM(image5)
feature_vector5 = GLCM(segmented_image5, masked_image5)
feature_vector5 = np.append(np.array(['DownyMildew']),feature_vector5)
print(feature_vector5)

#Storing Healthy leaf
image6 = cv2.imread('D:\\MDD\\Leaf images\\Healthyleaf.jpg')
image6 = preprocess(image6)
masked_image6 , segmented_image6 = KM(image6)
feature_vector6 = GLCM(segmented_image6, masked_image6)
feature_vector6 = np.append(np.array(['HealthyLeaf']),feature_vector6)
print(feature_vector6)





df1 =pd.DataFrame(np.array([feature_vector1, feature_vector2,feature_vector3, feature_vector4, feature_vector5, feature_vector6]),
                   columns=['Name','contrast','','dissimilarity','','homogeneity','','ASM','','energy','','correlation',''])


df1.to_excel('test.xlsx')