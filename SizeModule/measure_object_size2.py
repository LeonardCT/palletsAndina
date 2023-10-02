import cv2
from object_detector import *
import numpy as np

##Anñadir variable global para tener la etiqueta

# Load Aruco detector
parameters =  cv2.aruco.DetectorParameters()
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)

# Load Object Detector
detector = HomogeneousBgDetector()

# Load Image
path="C:\\Users\\leonard\\palletsAndina\\SizeModule\\P_A4.jpg"

path2="C:\\Users\\leonard\\palletsAndina\\SizeModule\\phone_aruco_marker_2.jpg"
path3="C:\\Users\\leonard\\palletsAndina\\SizeModule\\arucoPalletTest.png"

img = cv2.imread(path3)


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
    # Calculate the area of the object in cm^2
    object_area = cv2.contourArea(cnt) / (pixel_cm_ratio ** 2)

    # Determine if the object has an area greater than 25 cm^2 and label it accordingly
    if object_area > 1000:
        label = "andina"
    else:
        label = "no andina"

    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Get Width and Height of the Objects by applying the Ratio pixel to cm
    object_width = w / pixel_cm_ratio
    object_height = h / pixel_cm_ratio

    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.intp(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Area {} cm^2".format(round(object_area, 1)), (int(x - 100), int(y + 50)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    cv2.putText(img, label, (int(x - 100), int(y + 85)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)