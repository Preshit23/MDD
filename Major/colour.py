
from preprocess import *
def colour(main_img):
    #main_img= preprocess(main_img)
    img = cv2.cvtColor(main_img, cv2.COLOR_BGR2RGB)

    # Colour features
    red_channel = img[:, :, 0]
    green_channel = img[:, :, 1]
    blue_channel = img[:, :, 2]
    blue_channel[blue_channel == 255] = 0
    green_channel[green_channel == 255] = 0
    red_channel[red_channel == 255] = 0
    #mean values
    red_mean = np.mean(red_channel)
    green_mean = np.mean(green_channel)
    blue_mean = np.mean(blue_channel)
    #std values
    red_std = np.std(red_channel)
    green_std = np.std(green_channel)
    blue_std = np.std(blue_channel)
    vect = [red_mean,green_mean,blue_mean,red_std,green_std,blue_std]
    return vect