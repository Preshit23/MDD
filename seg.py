import cv2
img = cv2.imread('C:\\Users\\Admin\\Downloads\\LEAF.jpg',0)
cv2.imshow("Gray",img)
cv2.waitKey(0)
ret,bw = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Binary",bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

