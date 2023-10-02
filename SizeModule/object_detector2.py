import cv2

class HomogeneousBgDetector():
    def __init__(self):
        pass

    def detect_objects(self, frame):
        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Aplicar umbral adaptativo
        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

        # Aplicar eliminación de ruido (erosión y dilatación)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # Encontrar contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Inicializar variables para el objeto más grande
        largest_area = 0
        largest_contour = None

        for cnt in contours:
            area = cv2.contourArea(cnt)

            # Filtrar contornos pequeños
            if area > 1000:  # Ajusta este valor según tus necesidades
                # Si el área del contorno actual es mayor que el área del objeto más grande encontrado hasta ahora
                if area > largest_area:
                    largest_area = area
                    largest_contour = cnt

        # Devolver el contorno del objeto más grande (puede ser None si no se encontraron contornos)
        return largest_contour
