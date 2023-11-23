import os
import cv2

# Parámetros del filtro:
BLUR_K_SIZE = (5,5)
GAUSSIAN_K_SIZE = (5,5)
GAUSSIAN_SIGMA_X = 0
THRESHOLD_THRESH = 128
THRESHOLD_MAX_VALUE = 255
CONTRASTE_ALPHA = 1.5
CONTRASTE_BETA = 30
ESCALA = 2 # Veces que se achicará la imagen
ROTATION = [90, 180]
carpeta_entrada = ''

import numpy as np
from skimage.morphology import skeletonize

def filtro_gaussiano(image):
    return cv2.GaussianBlur(image, GAUSSIAN_K_SIZE, GAUSSIAN_SIGMA_X)

def filtro_adelgazamiento(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    binary = binary / 255  # Convertir a binario (0 o 1)
    skeleton = skeletonize(binary)
    skeleton = skeleton.astype(np.uint8) * 255  # Convertir de nuevo a valores 0-255
    skeleton = cv2.cvtColor(skeleton, cv2.COLOR_GRAY2BGR)
    return skeleton

def filtro_ensanchamiento(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    skeleton = skeletonize(binary)
    skeleton = skeleton.astype(np.uint8) * 255
    skeleton = cv2.cvtColor(skeleton, cv2.COLOR_GRAY2BGR)
    return skeleton

def filtro_blur(image):
    return cv2.blur(image, BLUR_K_SIZE)

def filtro_saturacion(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = 2 * hsv[:, :, 1]
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def filtro_contraste(image):
    return cv2.convertScaleAbs(image, alpha=CONTRASTE_ALPHA, beta=CONTRASTE_BETA)

def filtro_enfoque(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def filtro_segmentacion(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

def filtro_deteccion_bordes(image):
    return cv2.Canny(image, 100, 200)

def original(image):
    return image

# Plantilla #
def nuevo_filtro(image):
    image_filtrada = image
    return image_filtrada
