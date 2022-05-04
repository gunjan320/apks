#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(plant):
  test_image = load_img(plant, target_size = (128, 128)) # load image
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==0:
      return "Apple__Apple_scab Disease", 'Apple__Apple_scab.html'
  elif pred==1:
      return "Apple__Black_rot Disease", 'Apple__Black_rot.html'
  elif pred==2:
      return "Apple__Cedar_apple_rust Disease" , 'Apple__Cedar_apple_rust.html'
  elif pred==3:
      return "Apple_Healthy ", 'Apple_Healthy.html'
  elif pred==4:
      return "Corn_(maize)__Cercospora_leaf_spot Gray_leaf_spot Disease ",'Corn_(maize)__Cercospora_leaf_spot Gray_leaf_spot.html'
  elif pred==5:
      return "Corn_(maize)__Common_rust Disease ",'Corn_(maize)__Common_rust.html'
  elif pred==6:
      return "Corn_(maize)__Healthy" , 'Corn_(maize)__Healthy.html'
  elif pred==7:
       return "Corn_(maize)__Northern_Leaf_Blight",'Corn_(maize)__Northern_leaf_Blight.html'
  elif pred==8:
      return "Potato__Early_blight Disease", 'Potato__Early_blight.html'
  elif pred==9:
      return "Potato__Healthy",'Potato__Healthy.html'
  elif pred==10:
      return "Potato__Late_blight Disease",'Potato__Late_blight.html'
  elif pred==11:
      return "Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'
       
  elif pred==12:
      return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'
        
  elif pred==13:
      return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html'
        

  elif pred==14:
      return "Tomato - Leaf Mold Disease", 'Tomato - Leaf_Mold.html'
        
  elif pred==15:
      return "Tomato - Septoria Leaf Spot Disease", 'Tomato - Septoria_leaf_spot.html'
        

  elif pred==16:
      return "Tomato - Tomoato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'
  elif pred==17:
      return "Tomato - Tomato Mosaic Virus Disease", 'Tomato - Tomato_mosaic_virus.html'
        
  elif pred==18:
      return "Tomato - Two Spotted Spider Mite Disease", 'Tomato - Two-spotted_spider_mite.html'

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('E:/pplant/static/upload', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
    
    
