import cv2
from object_detector import *
import numpy as np

# Load Aruco detector

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
parameters =  cv2.aruco.DetectorParameters()
#detector = cv.aruco.ArucoDetector(aruco_dict, parameters)

# Load Object Detector
detector = HomogeneousBgDetector()

# Load Image
img = cv2.imread("phone_aruco_marker_2.jpg")

# Get Aruco marker
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

# Draw polygon around the marker
int_corners = np.intp(corners)
cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

# Aruco Perimeter
aruco_perimeter = cv2.arcLength(corners[0], True)

# Pixel to cm ratio
pixel_cm_ratio = aruco_perimeter / 20

contours = detector.detect_objects(img)

# Draw objects boundaries
for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Get Width and Height of the Objects by applying the Ratio pixel to cm
    object_width = w / pixel_cm_ratio
    object_height = h / pixel_cm_ratio

    # Check if either width or height is greater than 10 cm


##Changes===> poner que cumpla con el tamaño y un umbral, modularizar esto.


    if object_width > 10 or object_height > 10:
        size_label = "Bad size"
    else:
        size_label = "Good size(andina)"

    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.intp(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, size_label, (int(x - 100), int(y + 50)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


cv2.imshow("Image", img)
cv2.waitKey(0)