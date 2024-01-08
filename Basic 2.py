import cv2 #library import

img = cv2.imread("Boy.jpg") #read an image

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # color to gray Image

cv2.imwrite("grayImage.png",grayImg) # save an Image

cv2.imshow("Orig",img)
cv2.imshow("Gray",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
