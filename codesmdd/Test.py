import pandas as pd
from scipy.spatial import distance
from GLCM import *
from Kmean import *
from preprocessing import *
import os

APP_PATH = 'C:\\Users\\Admin\\PycharmProjects'
dfrec=pd.read_excel(
     os.path.join(APP_PATH, "pythonProject", "test.xlsx"),
     sheet_name=None,
     engine='openpyxl', header=None
)


#Retrieving vectors from dataframe

v1 =dfrec['Sheet1'].values[1]
v2 =dfrec['Sheet1'].values[2]
v3 =dfrec['Sheet1'].values[3]
v4 =dfrec['Sheet1'].values[4]
v5 =dfrec['Sheet1'].values[5]
v6 =dfrec['Sheet1'].values[6]
#slicing away name and index

vs1 = v1[2:14]
vs2 = v2[2:14]
vs3 = v3[2:14]
vs4 = v4[2:14]
vs5 = v5[2:14]
vs6 = v6[2:14]

#Converting into float array

vfloat1 = [float(i) for i in vs1]
vfloat2 = [float(i) for i in vs2]
vfloat3 = [float(i) for i in vs3]
vfloat4 = [float(i) for i in vs4]
vfloat5 = [float(i) for i in vs5]
vfloat6 = [float(i) for i in vs6]

#For test leaf again generate feature vector

image_test = cv2.imread('D:\\MDD\\Leaf images\\Healthyleaf.jpg')
image_test = preprocess(image_test)
masked_image_test , segmented_image_test = KM(image_test)
feature_vector_test = GLCM(segmented_image_test, masked_image_test)
feature_vector_test = np.append(np.array(['Testleaf']),feature_vector_test)

#Display test feature vector

#print(feature_vector_test)

#Slicing away leafname and float conversion

feature_vector_test_sliced= feature_vector_test[1:14]
test_feature = [float(i) for i in feature_vector_test_sliced]
#print("testfeature final :")
#print(test_feature)
#print("vfloat1:")
#print(vfloat1)


#Calculating difference factor

d1 = distance.euclidean(vfloat1,test_feature)
d2 = distance.euclidean(vfloat2,test_feature)
d3 = distance.euclidean(vfloat3,test_feature)
d4 = distance.euclidean(vfloat4,test_feature)
d5 = distance.euclidean(vfloat5,test_feature)
d6 = distance.euclidean(vfloat6,test_feature)
#print("Difference factor / Euclidean distance: for 1")
#print(d1)
#print("Difference factor / Euclidean distance: for 2")
#print(d2)

#Finding the best match on the basis of min distance
l = (d1,d2,d3,d4,d5,d6)
#index of smallest item in list
X = l.index(min(l))
#Using index to display name of disease

if X == 0:
     print(" Disease Name: ")
     print(v1[1])
elif X==1:
     print(" Disease Name: ")
     print(v2[1])
elif X==2:
     print(" Disease Name: ")
     print(v3[1])
elif X==3:
     print(" Disease Name: ")
     print(v4[1])
elif X==4:
     print(" Disease Name: ")
     print(v5[1])
elif X==5:
     print(" No Disease detected: ")
     print(v6[1])
