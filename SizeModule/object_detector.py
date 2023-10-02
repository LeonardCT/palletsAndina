import cv2

class HomogeneousBgDetector():
    def __init__(self):
        pass

    def detect_objects(self, frame):
        # Convert Image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Create a Mask with adaptive threshold
        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Initialize variables to track the two largest objects
        largest_areas = [0, 0]
        largest_contours = [None, None]

        for cnt in contours:
            area = cv2.contourArea(cnt)

            # If the current contour is larger than the second largest but smaller than the largest, update the second largest
            if area > largest_areas[1]:
                if area > largest_areas[0]:
                    largest_areas[1] = largest_areas[0]
                    largest_contours[1] = largest_contours[0]
                    largest_areas[0] = area
                    largest_contours[0] = cnt
                else:
                    largest_areas[1] = area
                    largest_contours[1] = cnt

        # Return the contours of the two largest objects
        return [contour for contour in largest_contours if contour is not None]
