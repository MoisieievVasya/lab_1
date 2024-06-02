import cv2
import numpy as np
import matplotlib.pyplot as plt
import open_cv_f as f_2

# part 2

adidas_logo = np.array([[0, 0], [2.4, 3], [4, 0], [0, 0], [6, 5], [9, 7], [13, 0], [9, 0], [6, 5], [13, 8.4], [16, 10], [22, 0], [17, 0], [12.5, 8.1]])


f_2.plot_data(adidas_logo, 'Adidas logo')

rotated_adidas_logo = f_2.rotation(adidas_logo, 45)
f_2.plot_data(rotated_adidas_logo, 'Rotated Adidas Logo')

scaled_adidas_logo = f_2.scale(adidas_logo, 2)
f_2.plot_data(scaled_adidas_logo, 'Scaled Adidas Logo')

mirrored_adidas_logo = f_2.mirror_on_axis(adidas_logo, 'x')
f_2.plot_data(mirrored_adidas_logo, 'Mirrored Adidas Logo')

mirrored_adidas_logo = f_2.mirror_on_axis(adidas_logo, 'y')
f_2.plot_data(mirrored_adidas_logo, 'Mirrored Adidas Logo')

sheared_adidas_logo = f_2.shear_on_axis(adidas_logo, 'x', 45)
f_2.plot_data(sheared_adidas_logo, 'Sheared Adidas Logo')

sheared_adidas_logo = f_2.shear_on_axis(adidas_logo, 'y', 45)
f_2.plot_data(sheared_adidas_logo, 'Sheared Adidas Logo')

transformation_matrix = np.array([[1, 0.5], [0.5, 1]])
custom_transformed_adidas_logo = f_2.custom_transformation(adidas_logo, transformation_matrix)
f_2.plot_data(custom_transformed_adidas_logo, 'Custom Adidas Logo')

