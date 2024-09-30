import sys
import cv2
import numpy

winID = "WIN MAIN"
window_width = 640
window_height = 480
strWindowTitle = "TITLE_MAIN"
window_posX = 100
window_posY = 100

# create the main window
cv2.namedWindow(winID, cv2.WINDOW_NORMAL)
cv2.resizeWindow(winID, window_width, window_height)
cv2.setWindowTitle(winID, strWindowTitle)
cv2.moveWindow(winID,window_posX, window_posY)

videobuffer = numpy.full((480,640,3),[255,255,255], dtype = 'uint8')

bAlive = True
while (bAlive):
    cv2.imread(".\downloaden.png")

#    to draw a line 
#    for h in range(0,480):
#        for w in range(0,640):
#            if h == w:
#                videobuffer[h][w] = [0,0,0]
#    for w in range(0,640):
#        cv2.line(videobuffer,(340,220),(w,220),(0,0,0),2)

    key = cv2.waitKey(30)
    if key == 27 & 0xFF:
        bAlive = False