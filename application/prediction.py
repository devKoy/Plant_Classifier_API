from keras.models import load_model
from keras.preprocessing import  image as im
import numpy as np

Classes = [ "no leaf detected",
            "Cordana Leaf Disease Spotted",
            "This Banana is Healthy",
            "Pestalotiopsis Leaf Disease Spotted",
            "Sigatoka Leaf Disease Spotted"]


def prepare(img):
    x = im.img_to_array(img)
    x = x/255
    return np.expand_dims(x, axis=0)

def modelizer():
	global model
	model = load_model('banana.h5')

def predict(img):
    img = prepare(img)
    modelizer()
    pred = model.predict(img)
    conf = int(pred[0][np.argmax(pred)] * 100)
    return Classes[np.argmax(pred)] + " with " + str(conf) + "% accuracy"