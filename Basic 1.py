import cv2 #import opencv libary

img = cv2.imread("Boy.jpg") #read an image in the name img

cv2.imwrite("BoyCopy.png",img) #save an image with diff. name and ext.name

cv2.imshow("Ai_Master_Class",img) #display an image
cv2.waitKey(0)

cv2.destroyAllWindows()

