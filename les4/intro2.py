import cv2
import numpy as np

# Initialize a blank image
image = np.zeros((480, 640, 3), dtype=np.uint8)
xpos = 0
ypos = 0

def mouse_callback(event, x, y, flags, param):
    global image
    global xpos
    global ypos
    xpos = x
    ypos = y
    if event == cv2.EVENT_LBUTTONDOWN:
        image[:] = (0, 255, 0)
    elif event == cv2.EVENT_RBUTTONDOWN:
        image[:] = (0, 0, 255)

def main():
    global image
    cv2.namedWindow('Color Window')
    cv2.setMouseCallback('Color Window', mouse_callback)

    while True:
        strmousepos = f'xpos: {xpos}, ypos: {ypos}'
        image_copy = image.copy()
        cv2.putText(image_copy, strmousepos, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, 1)
        cv2.imshow('Color Window', image_copy)
        # input a text window to show the parameters of the window
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break


    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()