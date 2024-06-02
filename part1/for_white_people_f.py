import numpy as np
import matplotlib.pyplot as plt


def plot_data(data, title=None):
    x, y = data[:, 0], data[:, 1]
    plt.plot(x, y)
    plt.title(title)
    plt.show()


def rotation(data, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return np.dot(data, rotation_matrix)


def scale(data, scalar):
    center = data.mean(axis=0)

    scale_matrix = np.array([[scalar, 0], [0, scalar]])
    return np.dot(data - center, scale_matrix) + center


def mirror_on_axis(data, axis):
    if axis == 'x':
        return data * np.array([-1, 1])
    return data * np.array([1, -1])


def shear_on_axis(data, axis, angle):
    if axis == 'x':
        shearing_matrix = np.array([[1, np.tan(np.radians(angle))], [0, 1]])
    else:
        shearing_matrix = np.array([[1, 0], [np.tan(np.radians(angle)), 1]])
    return np.dot(data, shearing_matrix)


def custom_transformation(data, transformation_matrix):
    return np.dot(data, transformation_matrix)


def translate(data, x, y):
    return data + np.array([x, y])