
import cv2
import numpy as np
import pandas as pd
import os
import string
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from preprocess import preprocess
from shape import shape
from colour import colour
from texture import texture
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.multiclass import OneVsOneClassifier

dr = pd.read_csv("leaf_data.csv")

#adding target column in our dataset

target = list(range(14))  #for number of  different plant species
K = 10                   # number of samples
target_n =  [ele for ele in target for i in range(K)]
#print(target_n)

X = dr.iloc[:,1:]  #to remove unnamed first column in dataframe

pca = PCA()
pca.fit(X)
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, target_n, test_size=0.4,random_state=45)


#scaling

# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)


#prediction
#clf = OneVsOneClassifier(svm.SVC(C=100)).fit(X_train, y_train)
clf = svm.SVC(decision_function_shape='ovo',C=100,)
clf.fit(X_train,y_train)

#parameter tuning

parameters = [{'kernel': ['rbf'],
               'gamma': [1e-4, 1e-3, 0.01, 0.1, 0.2, 0.5],
               'C': [1, 10, 100, 1000]},
              {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}
             ]


svm_clf = GridSearchCV(svm.SVC(decision_function_shape='ovo'), parameters, cv=3)
svm_clf.fit(X_train, y_train)

print('best para = ',svm_clf.best_params_)
y_pred_svm = svm_clf.predict(X_test)


print('score after tuning',metrics.accuracy_score(y_test, y_pred_svm))

print(metrics.classification_report(y_test, y_pred_svm))






#test image

titles = ['area','perimeter','aspect_ratio','rectangularity','circularity',
          'contrast','correlation','inverse_difference_moments','entropy',
            'mean_r','mean_g','mean_b','std_r','std_g','std_b'
            ]



df = pd.DataFrame([], columns=titles)

test_image = cv2.imread('D:\\MDD\\Leaf images\\1001.jpg')
# texture
fv_texture = texture(test_image)
# shape
fv_shape = shape(test_image)
# colour
fv_colour = colour(test_image)

fv_final = fv_shape + fv_texture + fv_colour

#print(fv_final)
df_temp_cap = pd.DataFrame([fv_final], columns=titles)
df_cap = df.append(df_temp_cap)
X_final = df_cap
# df_cap_trans = sc_X.transform(df_cap)
# X_final  = df_cap_trans
########
print('features of leaf being tested\n',X_final)
# print(df_cap_trans)
y_pred_test = svm_clf.predict(X_final)





print('Prediction: ', y_pred_test[0])

leaf_names = ['Azadirachta indica',
                'Ocimum tenuiflorum',
                'Saraca asoca',
                'Holoptelea integrifolia',
                 'Eupatorium ayyappana',
                 'Ocimum basilicum',
                  'Laurus nobilis',
                  'Elettaria cardamomum',
                    'Canabis',
                    'Tinospora cordifolia',
                    'Solanum torvum',
                    'Piper betle ',
                    'Wrightia Tinctoria Pala',
                    'Zingiber officinale' ]

print('Detected Species = ' , leaf_names[y_pred_test[0]])

