from keras.models import load_model
from keras.preprocessing import  image as im
import numpy as np
from efficientnet.tfkeras import EfficientNetB4

Classes = [ "no leaf detected",
            "Banana",
            "Corn",
            "Pepper",
            "Rice",
            "Squash",
            "Tomato" 
        ]

def prepare(img):
    x = im.img_to_array(img)
    x = x/255
    return np.expand_dims(x, axis=0)

def modelizer():
	global model
	model = load_model('plantsv2.h5')

def predict(img):
    img = prepare(img)
    modelizer()
    pred = model.predict(img)
    conf = int(pred[0][np.argmax(pred)] * 100)
    return Classes[np.argmax(pred)] + " with " + str(conf) + "% accuracy"