import numpy as np
import cv2

face = cv2.imread('cells.png')
cv2.imshow('image', face)

cv2.waitKey(0)
cv2.destroyAllWindows()
