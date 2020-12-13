import cv2
from PIL import Image
from skimage import measure
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel
img = cv2.imread('C:\\Users\\Admin\\Downloads\\LEAF.jpg',0)
cv2.imshow("Gray",img)
cv2.waitKey(0)
ret,bw = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Binary",bw)
edgy = sobel(bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
contours = measure.find_contours(edgy,0.2)
fig, ax =plt.subplots()
ax.imshow(edgy,interpolation='nearest', cmap=plt.cm.gray)
for n, contour in enumerate(contours):
    ax.plot(contour[:,1], contour[:,0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

