from flask import Flask, request, render_template, request
#The following are for the AI code
# We used keras 2.2.5 and tensorflow version 1.6
from keras.models import load_model
from PIL import Image, ImageFilter
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import keras
from keras import backend as K
import os
import tensorflow as tf

#This is for working with AWS
import boto3

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

# convert number prediction to type of clothing
def convert_number(n):
    switcher = {
        0: "T-shirt",
        1: "Trouser",
        2: "Pullover",
        3: "Dress",
        4: "Coat",
        5: "Sandal",
        6: "Shirt",
        7: "Sneaker",
        8: "Bag",
        9: "Ankle Boot"
    }
    return switcher.get(n, "No prediction")

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['Upload_folder'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init():
   global model,graph
   # load model
   client_s3 = boto3.client("s3")
   result = client_s3.download_file("fashion-model",'fashion_model.h5', "/tmp/model.h5")
   model = load_model("/tmp/model.h5")
   model._make_predict_function()
   graph = tf.get_default_graph()

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/predict', methods=['GET','POST'])
def my_form_post():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(os.path.dirname(__file__) + "/static/uploads", filename))
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28,28))
        img = img_to_array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img.astype('float32')

        #Makes and prints prediction
        pred = model.predict(img)
        mypred = pred.argmax()

        return render_template("result.html", pred_str = convert_number(mypred), filename = "/static/uploads/"+filename)

if __name__ == '__main__':
   print(("* Loading Keras model and Flask starting server..."
      "please wait until server has fully started"))
   init()
   app.run(debug = True)
