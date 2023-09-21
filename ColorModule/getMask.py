import cv2
import numpy as np

def crear_mascara_cuadrado(image_path, x1, y1, x2, y2):
    # Cargar la imagen
    imagen = cv2.imread(image_path)
    
    # Crear una máscara del tamaño de la imagen
    x_mask = np.zeros_like(imagen, dtype=np.uint8)

    # Dibujar el rectángulo en la máscara
    x_mask = cv2.rectangle(x_mask, (x1, y1), (x2, y2), (255, 255, 255), -1)

    # Muestra la imagen resultante con el cuadrado seleccionado
    return x_mask

# Cargar la imagen
image_path = 'C:/Users/leonard/Pictures/PalletsNoAndina/palletRed.png'
x1, y1, x2, y2 = 50, 50, 100, 100  # Especifica las coordenadas del cuadrado
x_mask=crear_mascara_cuadrado(image_path, x1, y1, x2, y2)

frame = cv2.imread(image_path)

z=cv2.bitwise_and(frame,frame,mask=x_mask)
cv2.imshow('Imagen con Cuadrado', z)
cv2.waitKey(0)
cv2.destroyAllWindows()                 
        