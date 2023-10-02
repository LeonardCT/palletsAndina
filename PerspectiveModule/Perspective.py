import cv2
import numpy as np

# Carga la imagen
img = cv2.imread('P_A8.jpeg')

# Convierte la imagen a YCrCb
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Extrae el canal Y (luminancia)
y_channel = ycrcb[:, :, 0]

# Aplica umbralización para separar el fondo del objeto
_, thresholded = cv2.threshold(y_channel, 150, 200, cv2.THRESH_BINARY)

# Encuentra el contorno del objeto después de eliminar el fondo
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibuja los contornos en una imagen en blanco
result = np.zeros_like(img)
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)  # Dibuja los contornos en verde

# Muestra la imagen con el fondo eliminado
cv2.imshow("Fondo Eliminado", result)

# Detectar esquinas con Harris en la imagen filtrada
corners = cv2.cornerHarris(thresholded, 2, 3, 0.04)  # Túneles de detección y otros parámetros

# Dilatar los puntos de esquina para una mejor visualización
corners = cv2.dilate(corners, None)

# Marcar las esquinas en la imagen filtrada
img[corners > 0.01 * corners.max()] = [0, 0, 255]  # Marcar esquinas en rojo

# Muestra la imagen con las esquinas marcadas
cv2.imshow("Esquinas Detectadas", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
