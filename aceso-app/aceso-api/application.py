# Load libraries\
#####
import flask
import numpy as np
import cv2
import glob, os
from PIL import Image, ImageFile
import io, base64
from io import BytesIO
from keras.preprocessing.image import img_to_array
import tensorflow as tf
import keras
from keras.models import load_model

# instantiate flask 
app = flask.Flask(__name__)

# we need to redefine our metric function in order 
# to use it when loading the model 
def auc(y_true, y_pred):
    auc = tf.metrics.auc(y_true, y_pred)[1]
    keras.backend.get_session().run(tf.local_variables_initializer())
    return auc

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
print(os.listdir())
model = load_model('cells.h5', custom_objects={'auc': auc})
modelp = load_model('spiral.h5', custom_objects={'auc':auc})
# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    ImageFile.LOAD_TRUNCATED_IMAGES = True

    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, return a prediction
    if (params != None):
        if flask.request.form.get("image"):
        #    # read the image in PIL format
            image = flask.request.form.get("image")
            print(type(image))
            img = base64.b64decode(image)
            print(type(img))
            image = Image.open(io.BytesIO(img))
        #    #print(image)
            
        

        open_cv_image = np.array(image)
        print(open_cv_image.shape) 
        #image = open_cv_image[:, :, ::-1].copy() 
        
        im = open_cv_image
        img_ = Image.fromarray(im, 'RGB')
        image = img_.resize((50, 50))
        image = np.array(image)
        image = image/255
        label=1
        a=[]
        a.append(image)
        a=np.array(a)
        with graph.as_default():
            pred = None

            score=model.predict(a)
            print(score)
            label_index=np.argmax(score)
            print(label_index)
            acc=np.max(score)

            if label_index == 0:
                pred = 'Malaria Detected'
            if label_index == 1:
                pred = 'Clean'
            data["prediction"] =  { "prediction": pred, "acccuracy": str(score[0].max()) }, 
            data["success"] = True

    # return a response in json format 
    return flask.jsonify(data)    

@app.route("/predictp", methods=["GET", "POST"])
def predictp():
    data = {"success": False}

    params = flask.request.json
    if (params==None):
        params = flask.request.args

    if (params != None):
        if flask.request.form.get("image"):
            image = flask.request.form.get("image")
            img = base64.b64decode(image)
            image = Image.open(io.BytesIO(img))

    open_cv_image = np.array(image)

    im = open_cv_image
    img_ = Image.fromarray(im, 'RGB')
    image = img_.resize((50, 50))
    image = np.array(image)
    image = image/255
    label = 1
    a = []
    a.append(image)
    a = np.array(a)
    with graph.as_default():
        pred = None

        score = modelp.predict(a)
        label_index= np.argmax(score)
        acc = np.max(score)

        if label_index == 0:
            pred = 'Healthy'
        if label_index == 1:
            pred = 'Parkinsons Detetced'
        data["prediction"] = { "prediction" : pred, "accuracy" : str(score[0].max()) },
        data["success"] = True
    print(data)
    return flask.jsonify(data)

# start the flask app, allow remote connections 
app.run(host='0.0.0.0', port=80)
