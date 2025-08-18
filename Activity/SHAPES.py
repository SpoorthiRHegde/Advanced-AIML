import cv2
import numpy as np
img = np.ones((400, 600, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (20, 40), (200, 140), (0, 0, 0), 3)
cv2.circle(img, (300, 90), 50, (0, 0, 0), 3)
pts = np.array([[260, 170], [340, 170], [300, 230]], np.int32)
cv2.polylines(img, [pts], isClosed=True, color=(0,0,0), thickness=3)
cv2.imshow('Shapes', img); cv2.waitKey(0); cv2.destroyAllWindows()
