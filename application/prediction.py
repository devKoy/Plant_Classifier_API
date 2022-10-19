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
def predict(path):
    result = {
       "accuracy" : 0,
       "diseases" :
       {
         0 : "!!",
         1 : "",
         2 : "",
       }
    }
    img = prepare(path)
    modelizer()
    prediction = model.predict(img)
    maxPredict = np.argmax(prediction)
    result["accuracy"] = round(prediction [0][maxPredict] * 100)   
    if(prediction[0][maxPredict] * 100 > 70 ):
       result["diseases"][0] = Classes[maxPredict]
    else:
       res = prediction[0].argsort()[-3:][::-1]
       counter = 0;
       for i in res:
          result["diseases"][counter] = Classes[i]
	      counter++;
    return str(result)
