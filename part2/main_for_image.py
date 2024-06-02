import numpy as np
import cv2
import real_usage_of_opencv as f_3


image = cv2.imread('Apple_logo_black.svg.png')

rotated_image = f_3.rotate(image, 45)
f_3.display(rotated_image, 'Rotated Apple Logo')

scaled_image = f_3.scale(image, 2)
f_3.display(scaled_image, 'Scaled Apple Logo')

mirrored_image = f_3.mirror(image, 'x')
f_3.display(mirrored_image, 'Mirrored Apple Logo')

mirrored_image = f_3.mirror(image, 'y')
f_3.display(mirrored_image, 'Mirrored Apple Logo')

sheared_image = f_3.shear(image, 'x', 45)
f_3.display(sheared_image, 'Sheared Apple Logo')

sheared_image = f_3.shear(image, 'y', 45)
f_3.display(sheared_image, 'Sheared Apple Logo')


