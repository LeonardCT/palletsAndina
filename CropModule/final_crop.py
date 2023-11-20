import cv2

def recortar_imagen(imagen, bounding_box):
    x, y, w, h = bounding_box
    imagen_recortada = imagen[y : y + h, x : x + w]
    return imagen_recortada
