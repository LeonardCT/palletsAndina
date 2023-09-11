import cv2
from PIL import Image

from util import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace

# Cargar la imagen que deseas analizar
image_path = 'C:/Users/leonard/Pictures/PalletsNoAndina/palletRed.png'
frame = cv2.imread(image_path)

hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lowerLimit, upperLimit = get_limits(color=yellow)

mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

mask_ = Image.fromarray(mask)

bbox = mask_.getbbox()

etiqueta = "No Andina"

if bbox is not None:
    x1, y1, x2, y2 = bbox
    frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    ##Pallet andina
    etiqueta = "Andina"
        
    etiqueta_pos = (x1, y1 - 10)  # Ajusta la posición de la etiqueta


if (etiqueta=="Andina"):
    frame = cv2.putText(frame, etiqueta, etiqueta_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()