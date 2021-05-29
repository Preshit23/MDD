import pandas as pd
from texture import *
from preprocess import *
from shape import *
from colour import *
import os

titles = [ 'area','perimeter','aspect_ratio','rectangularity','circularity',
           'contrast','correlation','inverse_difference_moments','entropy',
             'mean_r','mean_g','mean_b','std_r','std_g','std_b'
            ]



path  = 'D:\\MDD\\Leaf images - ALL Final'
file_itr = os.listdir(path)
df = pd.DataFrame([], columns=titles)
for file in file_itr:
    imgpath = path + "\\" + file
    image = cv2.imread(imgpath)
    cv2.imshow('leaf',image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # texture
    fv_texture = texture(image)
    # shape
    fv_shape = shape(image)
    # colour
    fv_colour = colour(image)

    fv_final = fv_shape + fv_texture + fv_colour

    print(fv_final)
    df_temp = pd.DataFrame([fv_final], columns= titles)
    df = df.append(df_temp)

df.to_csv("Leaf_data.csv")
