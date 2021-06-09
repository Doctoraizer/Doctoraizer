import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import math

def prepare_img(path):
    img_width, img_height = 224, 224
    img = image.load_img(path, target_size = (img_width, img_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)
    return img

def predict_pneumonia(img):
    model = keras.models.load_model('my_modelv2.h5')
    result =  model.predict_classes(img)[0]
    if result == 0:
        return 'Normal'
    elif result == 1:
        return 'Pneumonia'

def predict_viral_or_bacteria(img):
    model = keras.models.load_model('my_modelv2.h5')
    result =  model.predict_classes(img)[0]
    if result == 0:
        return 'Bacterial pneumonia'
    elif result == 1:
        return 'Viral pneumonia'

def predict_covid19(img):
    model = keras.models.load_model('mobileNet_covid19.h5')
    result =  model.predict(img)[0]
    result = 'Positive: {} | Negative: {}'.format(proper_round(result[0], 3), proper_round(result[1], 3))
    return result

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
      a = num[:-2-(not dec)]       # integer part
      b = int(num[-2-(not dec)])+1 # decimal part
      return float(a)+b**(-dec+1) if a and b == 10 else float(a+str(b))
    return float(num[:-1])

if __name__ == '__main__':
    path = './assets/test.jpg'
    img = prepare_img(path)
    predict_pneumonia(img)
    predict_viral_or_bacteria(img)
    print(predict_covid19(img))
