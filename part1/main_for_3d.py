import numpy as np
import for_3d_f as f_3d

data = np.array([
    [0, 0, 0],
    [3, 0, 0],
    [2, 3, 0],
    [1, 2, 3],
    [3, 1, 2],
    [0, 3, 1],
    [2, 2, 1],
    [1, 0, 3],
    [3, 3, 2],
    [0, 2, 2]
])

scaled_data = f_3d.scale_3d(data, 2)
f_3d.plot_data_3d(scaled_data, 'Scaled Data')

rotated_data = f_3d.rotate_3d(data, 45, 'x')
f_3d.plot_data_3d(rotated_data, 'Rotated Data')

rotated_data = f_3d.rotate_3d(data, 45, 'y')
f_3d.plot_data_3d(rotated_data, 'Rotated Data')

rotated_data = f_3d.rotate_3d(data, 45, 'z')
f_3d.plot_data_3d(rotated_data, 'Rotated Data')

mirrored_data = f_3d.mirror_3d(data, 'x')
f_3d.plot_data_3d(mirrored_data, 'Mirrored Data')

mirrored_data = f_3d.mirror_3d(data, 'y')
f_3d.plot_data_3d(mirrored_data, 'Mirrored Data')

mirrored_data = f_3d.mirror_3d(data, 'z')
f_3d.plot_data_3d(mirrored_data, 'Mirrored Data')






