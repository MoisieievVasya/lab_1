import numpy as np
from part1 import for_white_people_f as f

# part 1

mcdonalds_logo_detailed = np.array([[0, 0], [1, 2], [2, 4], [2.5, 6], [3, 4], [4, 2], [5, 0], [5, 0], [6, 2], [7, 4], [7.5, 6], [8, 4], [9, 2], [10, 0]])
adidas_logo = np.array([[0, 0], [2.4, 3], [4, 0], [0, 0], [6, 5], [9, 7], [13, 0], [9, 0], [6, 5], [13, 8.4], [16, 10], [22, 0], [17, 0], [12.5, 8.1]])
f.plot_data(adidas_logo, 'Adidas Logo')

rotated_adidas_logo = f.rotation(adidas_logo, 45)
f.plot_data(rotated_adidas_logo, 'Rotated Adidas Logo')

multiplied_adidas_logo = f.scale(adidas_logo, 2)
f.plot_data(multiplied_adidas_logo, 'Scaled Adidas Logo')

mirrored_adidas_logo = f.mirror_on_axis(adidas_logo, 'x')
f.plot_data(mirrored_adidas_logo, 'Mirrored Adidas Logo')

mirrored_adidas_logo = f.mirror_on_axis(adidas_logo, 'y')
f.plot_data(mirrored_adidas_logo, 'Mirrored Adidas Logo')

incline_adidas_logo = f.shear_on_axis(adidas_logo, 'x', 45)
f.plot_data(incline_adidas_logo, 'Inclined Adidas Logo')

incline_adidas_logo = f.shear_on_axis(adidas_logo, 'y', 45)
f.plot_data(incline_adidas_logo, 'Inclined Adidas Logo')

transformation_matrix = np.array([[1, 0.5], [0.5, 1]])

custom_transformed_adidas_logo = f.custom_transformation(adidas_logo, transformation_matrix)
f.plot_data(custom_transformed_adidas_logo, 'Custom Adidas Logo')

reflection_across_a_line = np.array([[np.cos(np.radians(45)), np.sin(np.radians(45))], [np.sin(np.radians(45)), -np.cos(np.radians(45))]])

custom_transformed_adidas_logo = f.custom_transformation(adidas_logo, reflection_across_a_line)
f.plot_data(custom_transformed_adidas_logo, 'Reflected on 45 degrees Adidas Logo')

identity_matrix = np.identity(2)
custom_transformed_adidas_logo = f.custom_transformation(adidas_logo, identity_matrix)
f.plot_data(custom_transformed_adidas_logo, 'Identity Adidas Logo')

