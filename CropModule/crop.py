import cv2
import numpy as np


def recortar_imagen(imagen, bounding_box):
    x, y, w, h = bounding_box
    imagen_recortada = imagen[y : y + h, x : x + w]
    return imagen_recortada


def enmascarar_imagen(imagen, bounding_box):
    x, y, w, h = bounding_box
    mascara = np.zeros(imagen.shape[:2], dtype=np.uint8)
    mascara[y : y + h, x : x + w] = 255
    imagen_enmascarada = cv2.bitwise_and(imagen, imagen, mask=mascara)
    return imagen_enmascarada


def enmascarar_con_fondo_blanco(imagen, bounding_box):
    x, y, w, h = bounding_box
    imagen_enmascarada = np.ones_like(imagen) * 255
    imagen_enmascarada[y : y + h, x : x + w] = imagen[y : y + h, x : x + w]
    return imagen_enmascarada


# Ejemplo CROP:
imagen = cv2.imread("test.png")
bounding_box = (350, 150, 400, 380)
imagen_recortada = recortar_imagen(imagen, bounding_box)
cv2.imwrite("imagen_recortada.png", imagen_recortada)


# Ejemplo MASCARA NEGRA:
imagen = cv2.imread("test.png")
bounding_box = (350, 150, 400, 380)
imagen_enmascarada = enmascarar_imagen(imagen, bounding_box)
cv2.imwrite("imagen_enmascarada.png", imagen_enmascarada)


# Ejemplo MASCARA BLANCA:
imagen = cv2.imread("test.png")
bounding_box = (350, 150, 400, 380)
imagen_blanca = enmascarar_con_fondo_blanco(imagen, bounding_box)
cv2.imwrite("imagen_enmascarada_blanca.png", imagen_blanca)
