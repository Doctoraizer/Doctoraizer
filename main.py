import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

model = keras.models.load_model('my_modelv2.h5')

def predict(path):

    img_width, img_height = 224, 224
    img = image.load_img(path, target_size = (img_width, img_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)

    result =  model.predict_classes(img)[0]
    if result == 0:
        return 'Normal'
    elif result == 1:
        return 'Pneumonia'


if __name__ == '__main__':
    path = './assets/person326_bacteria_1505.jpeg'
    predict(path)
