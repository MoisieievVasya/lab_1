import cv2
import numpy as np

def rotate (image, angle):
    rows, cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    return cv2.warpAffine(image, rotation_matrix, (cols, rows))

def scale(image, scalar):
    return cv2.resize(image, None, fx=scalar, fy=scalar)

def mirror(image, axis):
    return cv2.flip(image, 1 if axis == 'x' else 0)

def shear(image, axis, angle):
    rows, cols = image.shape[:2]
    shear_matrix = np.array([[1, np.tan(np.radians(angle))], [np.tan(np.radians(angle)), 1]])
    return cv2.warpAffine(image, shear_matrix, (cols, rows))

def display(image, text_for = 'image'):
    cv2.imshow(f'{text_for}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()