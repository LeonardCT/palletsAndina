import cv2
import numpy as np

# Lee la imagen
imagen = cv2.imread('FALLA_TABLA6.jpeg')

# Convierte la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplica un filtro de suavizado
imagen_suavizada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)

# Aplica un umbral para segmentar el objeto del fondo
_, imagen_umbral = cv2.threshold(imagen_suavizada, 120, 255, cv2.THRESH_BINARY)

# Encuentra los contornos en la imagen umbral
contornos, jerarquia = cv2.findContours(imagen_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Encuentra el contorno deseado (por ejemplo, el contorno más grande)
contorno_objeto = max(contornos, key=cv2.contourArea)

# Dibuja el contorno en la imagen original
cv2.drawContours(imagen, [contorno_objeto], -1, (0, 255, 0), 2)

# Crea una máscara para el objeto y aplícala a la imagen original
mascara = np.zeros_like(imagen_gris)
cv2.drawContours(mascara, [contorno_objeto], 0, 255, -1)
objeto_extraido = cv2.bitwise_and(imagen, imagen, mask=mascara)

# Muestra la imagen con el objeto extraído
cv2.imshow('Objeto Extraido', objeto_extraido)
cv2.waitKey(0)
cv2.destroyAllWindows()
