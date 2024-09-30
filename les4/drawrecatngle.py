import cv2
import numpy as np

# Initialize a blank image
image = np.zeros((480, 640, 3), dtype=np.uint8)
start_point = None
end_point = None
drawing = False

def mouse_callback(event, x, y, flags, param):
    global start_point, end_point, drawing, image

    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_image = image.copy()
            end_point = (x, y)
#            cv2.rectangle(temp_image, start_point, end_point, (255, 0, 0), 2)
#            cv2.imshow('Rectangle Drawing', temp_image)

    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        drawing = False
#        cv2.imshow('Rectangle Drawing', image)
#        print(f"Rectangle: Start Point: {start_point}, End Point: {end_point}")

def main():
    global image
    cv2.namedWindow('Rectangle Drawing')
    cv2.setMouseCallback('Rectangle Drawing', mouse_callback)

    while True:
        # clear the image
        imagenew = image.copy()
        # put background

        # put text
        # draw rectangle
        cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)

        cv2.imshow('Rectangle Drawing', image)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()