import sys
import cv2
import numpy

winID = "WIN MAIN"
window_width = 640
window_height = 480
strWindowTitle = "TITLE_MAIN"
window_posX = 100
window_posY = 100
blue_background = numpy.full((window_height, window_width, 3),[0,255,0], dtype='uint8')

# create the main window
cv2.namedWindow(winID, cv2.WINDOW_NORMAL)
cv2.resizeWindow(winID, window_width, window_height)
cv2.setWindowTitle(winID, strWindowTitle)
cv2.moveWindow(winID,window_posX, window_posY)

bAlive = True
while (bAlive):
    cv2.imshow(winID, blue_background)
    key = cv2.waitKey(30)
    if key == 27 & 0xFF:
        bAlive = False




