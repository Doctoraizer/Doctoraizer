import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils
import math

def prepare_img_keras(path):
    img_path = path
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

def is_chestxray(img):
    model = keras.models.load_model('is_chest.h5')
    result =  model.predict_classes(img)[0]
    if result == 0:
        return 'not_xray'
    elif result == 1:
        return 'xray'

def predict_class(img):
    if is_chestxray(img) == 'xray':
        model = keras.models.load_model('mobileNet_3c.h5')
        predictions = model.predict(img)[0]
        print(predictions)
        result = np.where(predictions == np.amax(predictions))[0]
        # {'COVID-19': 0, 'Normal': 1, 'bacteria': 2}
        if result == 0:
            return 'Pneumonia | COVID-19 Positive'
        elif result == 1:
            return 'No illness detected'
        elif result == 2:
            return 'Pneumonia | Bacteria'
    else:
        return what_is_the_img(img)

def what_is_the_img(img):
        model = keras.models.load_model('mobilenet.h5')
        predictions  =  model.predict(img)
        result = imagenet_utils.decode_predictions(predictions)[0][0][1]
        return f'This is not a Chest-Xray image\n mmm is it a {result} ?'

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
      a = num[:-2-(not dec)]       # integer part
      b = int(num[-2-(not dec)])+1 # decimal part
      return float(a)+b**(-dec+1) if a and b == 10 else float(a+str(b))
    return float(num[:-1])

if __name__ == '__main__':
    path = './assets/person128_bacteria_608.jpeg'
    img = prepare_img_keras(path)
    print(predict_class(img))
