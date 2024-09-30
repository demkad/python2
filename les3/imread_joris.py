import cv2

# Read the image from file
image = cv2.imread('VUL HET PAD NAAR EIGEN FOTO IN')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original image in a window
    cv2.imshow('Original Image Window', image)
    cv2.moveWindow('Original Image Window', 100, 100)  # Position the first window

    # Display the grayscale image in another window
    cv2.imshow('Grayscale Image Window', gray_image)
    cv2.moveWindow('Grayscale Image Window', 800, 100)  # Position the second window next to the first

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('f'):
            # Convert the image to negative
            negative_image = cv2.bitwise_not(image)
            cv2.imshow('Original Image Window', negative_image)
        elif key == ord('r'):
            # Revert to the original image
            cv2.imshow('Original Image Window', image)
        elif key == 27:  # ESC key to exit
            break

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()