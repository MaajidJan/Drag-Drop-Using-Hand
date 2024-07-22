import cv2
import numpy as np
from HandTrackingModule import HandDetector

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set frame width
cap.set(4, 720)  # Set frame height
detector = HandDetector(detectionCon=0.8)  # Initialize hand detector

# Define color for rectangles
colorR = (255, 0, 255)


class DragRect:
    def __init__(self, pos_center, size=[200, 200]):
        """
        Initialize a draggable rectangle.

        :param pos_center: Initial position of the rectangle's center (x, y)
        :param size: Size of the rectangle [width, height]
        """
        self.pos_center = pos_center
        self.size = size

    def update(self, cursor):
        """
        Update rectangle position if cursor is inside the rectangle.

        :param cursor: Current cursor position (x, y)
        """
        cx, cy = self.pos_center
        w, h = self.size

        # Check if the cursor is within the bounds of the rectangle
        if (cx - w // 2 < cursor[0] < cx + w // 2 and
                cy - h // 2 < cursor[1] < cy + h // 2):
            self.pos_center = cursor


# Create a list of draggable rectangles
rect_list = [DragRect([x * 250 + 150, 150]) for x in range(5)]

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Flip the image horizontally
    img = detector.findHands(img)  # Detect hands in the image
    lm_list, _ = detector.findPosition(img)  # Find landmarks

    if lm_list:
        # Get distance between thumb and index finger
        distance, _, _ = detector.findDistance(8, 12, img, draw=False)
        if distance < 40:
            cursor = lm_list[8][1:]  # Get index finger tip position

            # Update rectangles based on cursor position
            for rect in rect_list:
                rect.update(cursor)

    # Draw rectangles with transparency effect
    img_new = np.zeros_like(img, np.uint8)
    for rect in rect_list:
        cx, cy = rect.pos_center
        w, h = rect.size
        cv2.rectangle(img_new, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
        # Draw rectangle corners
        cv2.rectangle(img_new, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), colorR, 2)

    # Blend the original image with the transparent rectangles
    alpha = 0.5
    mask = img_new.astype(bool)
    out = img.copy()
    out[mask] = cv2.addWeighted(img, alpha, img_new, 1 - alpha, 0)[mask]

    # Display the resulting image
    cv2.imshow("Image", out)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on 'ESC' key
        break

cap.release()
cv2.destroyAllWindows()
