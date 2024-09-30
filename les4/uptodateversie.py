import sys
import ctypes
import cv2
import numpy as np
 
bMouse = False
xMouse = 0
yMouse = 0
xClickUp = 0
yClickUp = 0
xClickDown = 0
yClickDown = 0
color = [128, 128, 128]  # Startkleur (grijs)
 
# muisklik event
def on_mouse(event, x, y, flags, param):
    global xMouse, yMouse, color, xClickDown, yClickDown, bMouse, xClickUp, yClickUp
    xMouse = x
    yMouse = y
    if event == cv2.EVENT_LBUTTONDOWN:
        color = [0, 0, 255]  # Maak het venster rood
        xClickDown = x
        yClickDown = y
        bMouse = True
       
    elif event == cv2.EVENT_RBUTTONDOWN:
        color = [0, 255, 0]  # Maak het venster groen
       
    if event == cv2.EVENT_LBUTTONUP:
        xClickUp = x
        yClickUp = y
        bMouse = False
       
 
winID = "WIN_MAIN"
window_width = 640
window_height = 480
strWindowTitle = "TITLE_MAIN"
window_posX = 100
window_posY = 100
 
# Maak een grijze afbeelding
originalBuffer = np.full((window_height, window_width, 3), [128, 128, 128], dtype='uint8')
videoBuffer = originalBuffer.copy()
 
# Maak het hoofdvenster
cv2.namedWindow(winID, cv2.WINDOW_NORMAL)
cv2.resizeWindow(winID, window_width, window_height)
cv2.setWindowTitle(winID, strWindowTitle)
cv2.moveWindow(winID, window_posX, window_posY)
 
bAlive = True
while bAlive:
    # Reset de buffer naar de originele grijze afbeelding
    videoBuffer[:] = color  # Gebruik de opgeslagen kleur
   
    # Voeg de muispositie tekst toe
    strMousePost = f"x:{xMouse}, y:{yMouse}"
    cv2.putText(videoBuffer, strMousePost, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
   
    # Teken een rechthoek rond de muispositie
    cv2.rectangle(videoBuffer, (xClickDown, yClickDown), (xClickUp, yClickUp), (255, 255, 255), 2)
   
    # Stel de muisklik event in
    cv2.setMouseCallback(winID, on_mouse)
   
    # Toon de videoBuffer (initiële afbeelding)
    cv2.imshow(winID, videoBuffer)
   
    # Wacht 30ms op een toetsdruk
    key = cv2.waitKey(30)
    if key == 27 & 0xFF:  # ESC key to break
        bAlive = False
 
cv2.destroyAllWindows()