import cv2

image = cv2.VideoCapture("C://Users//kadirvm//Documents//Projects//python_2//python2//les3//WIN_20240916_21_04_30_Pro.jpg")

cv2.imshow('Image Window', image)
cv2.moveWindow('Image Window',100,100)

bAlive = True
while bAlive:
    key = cv2.waitKey(1) 
    if key == 27 & 0xFF:
        bAlive = False