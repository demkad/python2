import time
import cv2
import numpy as np
buf = np.zeros((480, 640, 3), dtype=np.uint8)
print(buf.shape[0])
print(buf.shape[1])
print(buf.shape[2])
def startWindow(winID):
    cv2.namedWindow(winID, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(winID, buf.shape[1], buf.shape[0])
    cv2.setWindowTitle(winID, 'Test Picture')
    cv2.moveWindow(winID, 100, 100)
def listCameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr
def convertToNegative(image):
    print("Converting to negative")
    return cv2.bitwise_not(image)
def resetWindow(winID, buf):
    print("Resetting window")
    cv2.imshow(winID, buf)
def convertToGrayScale(image):
    print("Converting to grayscale")
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def cameraRunning(cameraIndex, winID, startTime):
    available_cameras = listCameras()
    if cameraIndex >= len(available_cameras):
        print(f"Error: Camera with index {cameraIndex} not found.")
        return
    camera = cv2.VideoCapture(cameraIndex)
    if not camera.isOpened():
        print(f"Error: Camera with index {cameraIndex} not found.")
        return
    current_effect = None
    bRet = True
    while bRet:
        bRet, buf = camera.read()
        if not bRet:
            break
        now = time.time_ns()
        # Add elapsed time
        cv2.putText(buf, str((now - startTime) / 1000000),
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (220, 220, 220),
                    2,
                    1)
        # Add time and date stamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        text_size, _ = cv2.getTextSize(timestamp, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        text_x = buf.shape[1] - text_size[0] - 10
        text_y = buf.shape[0] - 10
        cv2.putText(buf, timestamp,
                    (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    1,
                    cv2.LINE_AA)
        # Apply current effect
        if current_effect == 'grayscale':
            buf = convertToGrayScale(buf)
        elif current_effect == 'negative':
            buf = convertToNegative(buf)
        cv2.imshow(winID, buf)
        k = cv2.waitKey(1) & 0xff
        print(f"Key pressed: {k}")
        if k == 27:
            cv2.destroyAllWindows()
            bRet = False
            break
        elif k == ord('a'):
            current_effect = 'grayscale'
        elif k == ord('f'):
            current_effect = 'negative'
        elif k == ord('r'):
            current_effect = None
if __name__ == '__main__':
    winID = 'Image1'
    startTime = time.time_ns()
    startWindow(winID)
    available_cameras = listCameras()
    if available_cameras:
        cameraRunning(available_cameras[0], winID, startTime)
    else:
        print("No cameras found.")