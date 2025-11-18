from PIL import Image
import random
import numpy as np


def predict_class(image):
    classes = ["dog", "cat", "horse", "bear", "pig"]
    return random.choice(classes)


def resize_image(image, size):
    return image.resize(size)


def convert_to_grayscale(image):
    return image.convert("L")


def normalize_image(image):
    image_array = np.array(image) / 255.0  
    return image_array


