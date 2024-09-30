import sys
import cv2
import numpy as np
import math

winID = "WIN_MAIN"
window_width = 640
window_height = 480
strWindowTitle = "TITLE_MAIN"
window_posX = 100
window_posY = 100

# Set the background to black
videoBuffer = np.full((window_height, window_width, 3), [0, 0, 0], dtype='uint8')

cv2.namedWindow(winID, cv2.WINDOW_NORMAL)
cv2.resizeWindow(winID, window_width, window_height)
cv2.setWindowTitle(winID, strWindowTitle)
cv2.moveWindow(winID, window_posX, window_posY)

start_point = (window_width // 2, window_height // 2)
angle = 0
rotation_speed = 1  # Set the rotation speed here
fps = 60  # Frames per second
total_frames = 1.5 * fps  # Total frames for 1.5 seconds

def rotate_point(center, angle):
    rad = math.radians(angle)
    cos_rad = math.cos(rad)
    sin_rad = math.sin(rad)

    if cos_rad == 0:
        length = center[1] / abs(sin_rad)
    elif sin_rad == 0:
        length = center[0] / abs(cos_rad)
    else:
        length = min(center[0] / abs(cos_rad), center[1] / abs(sin_rad))

    x = int(center[0] + length * cos_rad)
    y = int(center[1] + length * sin_rad)
    return (x, y)

bAlive = True

while bAlive:
    # Set the background to black
    videoBuffer = np.full((window_height, window_width, 3), [0, 0, 0], dtype='uint8')

    # Draw the middle line with 100% intensity (red)
    end_point = rotate_point(start_point, angle)
    cv2.line(videoBuffer, start_point, end_point, (255, 0, 0), 2)

    # Draw 50 lines with gradient intensity (green) within the same centimeter
    for i in range(1, 51):
        intensity = max(0, 255 - (i * 5))  # Decrease intensity by 5 (2% of 255) each time
        end_point_front = rotate_point(start_point, angle - (i * 0.1))
        end_point_back = rotate_point(start_point, angle + (i * 0.1))
        cv2.line(videoBuffer, start_point, end_point_front, (0, intensity, 0), 2)
        cv2.line(videoBuffer, start_point, end_point_back, (0, intensity, 0), 2)

    cv2.imshow(winID, videoBuffer)
    angle += rotation_speed
    if angle >= 360:
        angle = 0
    key = cv2.waitKey(1000 // fps)
    if key == 27 & 0xff:
        bAlive = False
        pass