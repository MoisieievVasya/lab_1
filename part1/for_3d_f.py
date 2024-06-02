import numpy as np
import matplotlib.pyplot as plt


def plot_data_3d(data, title):
    x, y, z = data[:, 0], data[:, 1], data[:, 2]
    plt.plot(x, y, z)
    plt.title(title)
    plt.show()

def scale_3d(data, scale_factor):
    return data * scale_factor

def rotate_3d(data, angle , axis):
    angle = np.radians(angle)
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(angle), -np.sin(angle)],
                                    [0, np.sin(angle), np.cos(angle)]])
    elif axis == 'y':
        rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                                    [0, 1, 0],
                                    [-np.sin(angle), 0, np.cos(angle)]])
    else:
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                    [np.sin(angle), np.cos(angle), 0],
                                    [0, 0, 1]])

    return np.dot(data, rotation_matrix)

def mirror_3d(data, axis):
    if axis == 'x':
        mirror_matrix = np.array([[-1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 1]])
    elif axis == 'y':
        mirror_matrix = np.array([[1, 0, 0],
                                  [0, -1, 0],
                                  [0, 0, 1]])
    else:
        mirror_matrix = np.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, -1]])

    return np.dot(data, mirror_matrix)