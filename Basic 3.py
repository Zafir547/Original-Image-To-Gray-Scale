import cv2 #libary import
                            
img = cv2.imread("Boy.jpg") #read an Image

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #color to gray Image

thresImg = cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]

cv2.imwrite("thresholdImage150.jpg",thresImg)

