
import warnings
warnings.simplefilter(action='ignore', category=Warning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import easyocr
from filters import *

filtros = [filtro_gaussiano, filtro_blur, filtro_contraste, filtro_enfoque, filtro_segmentacion, original]

def detectar_texto_y_verificar(imagen):
    cv2.imwrite('temp_image.png', imagen)
    reader = easyocr.Reader(['en'])
    resultados_easyocr = reader.readtext('temp_image.png',rotation_info=ROTATION)
    texto_detectado_easyocr = ' '.join([resultado[1] for resultado in resultados_easyocr])
    os.remove('temp_image.png')
    texto_detectado = texto_detectado_easyocr.lower()
    palabras_clave = ['ccu', 'cu', 'cc', 'cmf', 'cm', 'cf', 'cmf', 'mf','c','u','m','f']
    contador = 0
    for palabra in palabras_clave:
        if palabra in texto_detectado:
            contador += 1
    return contador >= 1 , texto_detectado

def isCCU(img):
    ruta_imagen = img
    imagen_original = cv2.imread(ruta_imagen)
    alto, ancho = imagen_original.shape[:2]
    imagen_ampliada = cv2.resize(imagen_original, (ancho * ESCALA, alto * ESCALA))
    detected = False
    for filtro in filtros:
        imagen_filtrada = filtro(imagen_ampliada)
        resultado,txt = detectar_texto_y_verificar(imagen_filtrada)
        if resultado:
            return True
    return detected