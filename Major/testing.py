
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
from search import search
from GUI import*

def SName(path_img):
    dr = pd.read_csv("leaf_data.csv")

    #adding target column in our dataset

    target = list(range(47))  #for number of  different plant species
    K = 10                   # number of samples
    target_n =  [ele for ele in target for i in range(K)]
    #print(target_n)

    X = dr.iloc[:,1:]  #to remove unnamed first column in dataframe


    pca = PCA()
    pca.fit(X)
    print(X)

    X_train, X_test, y_train, y_test = train_test_split(X, target_n, test_size=0.33,random_state=42)


    #scaling

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)


    #prediction
    #clf = OneVsOneClassifier(svm.SVC(C=100)).fit(X_train, y_train)

    clf = svm.SVC(decision_function_shape='ovo',C=100)
    clf.fit(X_train,y_train)

    #parameter tuning

    parameters = [{'kernel': ['rbf'],
               'gamma': [1e-4, 1e-3, 0.01, 0.1, 0.2, 0.5],
               'C': [1, 10, 100, 1000]},
              {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}
             ]


    svm_clf = GridSearchCV(svm.SVC(decision_function_shape='ovo'), parameters,cv=2)
    svm_clf.fit(X_train, y_train)

    print('best para = ',svm_clf.best_params_)
    y_pred_svm = svm_clf.predict(X_test)


    print('score after tuning',metrics.accuracy_score(y_test, y_pred_svm))

    print(metrics.classification_report(y_test, y_pred_svm))




    #   TEST ___ IMAGE

    titles = ['area','perimeter','aspect_ratio','rectangularity','circularity',
          'contrast','correlation','inverse_difference_moments','entropy',
            'mean_r','mean_g','mean_b','std_r','std_g','std_b'
            ]



    df = pd.DataFrame([], columns=titles)
    img_path = path_img
    img_path = img_path.replace("/", "\\")
    test_image = cv2.imread(img_path)
    #cv2.imshow('Test Image',test_image)
    #cv2.waitKey(1000)
    #cv2.destroyAllWindows()

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
    df_cap_trans = sc_X.transform(df_cap)
    X_final  = df_cap_trans
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
    'Zingiber officinale' ,
    'Helicteres isora',
    'Phyllostachys edulis ',
    'Aesculus chinensis',
    'Berberis anhweiensis Ahrendt',
    'Cercis chinensis',
    'Indigofera tinctoria L.',
    'Phoebe nanmu (Oliv.) Gamble',
    'Acer Palmatum',
    'Kalopanax septemlobus (Thunb. ex A.Murr.) Koidz.',
    'Cinnamomum japonicum Sieb',
    'Koelreuteria paniculata Laxm.',
    'Ilex macrocarpa Oliv',
    'Pittosporum tobira (Thunb.) Ait. f.',
    'Chimonanthus praecox L.',
    'Cinnamomum camphora (L.) J. Presl',
    'Viburnum awabuki K.Koch',
    'Osmanthus fragrans Lour.',
    'Cedrus deodara (Roxb.) G. Don',
    'Ginkgo biloba L.',
    'Lagerstroemia indica (L.) Pers.',
    'Nerium oleander L.',
    'Podocarpus macrophyllus (Thunb.) Sweet',
    'Prunus serrulata Lindl. var. lannesiana auct.',
    'Ligustrum lucidum Ait. f.',
    'Tonna sinensis M. Roem.',
    'Prunus persica (L.) Batsch',
    'Manglietia fordiana Oliv.',
    'Acer buergerianum Miq.',
    'Mahonia bealei (Fortune) Carr.',
    'Magnolia grandiflora L.',
    'Populus ×canadensis Moench',
    'Liriodendron chinense (Hemsl.) Sarg.',
    'Citrus reticulata Blanco'
    ]

    species_name = leaf_names[y_pred_test[0]]

    print('Detected Species = ' , species_name)

    return species_name

