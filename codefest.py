import matplotlib.pyplot as plt
import cv2

cv2.imsave('cells.png', face)

face = cv2.imread('cells.png')
type(face)
#'numpy.ndarray'
face.shape, face.dtype
#((768, 1024, 3), dtype('uint8'))

plt.imshow(face, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.axis('off')
#plt.contour(face)
plt.show()
