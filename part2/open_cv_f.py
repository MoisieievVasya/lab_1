import cv2
import numpy as np
import matplotlib.pyplot as plt


def plot_data(data, title=None):
    x, y = data[:, 0], data[:, 1]
    plt.plot(x, y)
    plt.title(title)
    plt.show()


def rotation(data, angle):
    rotation_matrix = cv2.getRotationMatrix2D((0, 0), angle, 1)
    return cv2.transform(data.reshape(-1,1,2), rotation_matrix).squeeze()

def scale(data, scalar):
    center = data.mean(axis=0)

    scale_matrix = np.array([[scalar, 0], [0, scalar]])
    return cv2.transform(data.reshape(-1,1,2), scale_matrix).squeeze()


def mirror_on_axis(data, axis):
    if axis == 'x':
        return cv2.transform(data.reshape(-1,1,2), np.array([-1, 1])).squeeze()
    return cv2.transform(data.reshape(-1,1,2), np.array([1, -1])).squeeze()

def shear_on_axis(data, axis, angle):
    if axis == 'x':
        shearing_matrix = np.array([[1, np.tan(np.radians(angle))], [0, 1]])
    else:
        shearing_matrix = np.array([[1, 0], [np.tan(np.radians(angle)), 1]])
    return cv2.transform(data.reshape(-1,1,2), shearing_matrix).squeeze()

def custom_transformation(data, transformation_matrix):
    return cv2.transform(data.reshape(-1,1,2), transformation_matrix).squeeze()