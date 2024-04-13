import uvicorn
from fastapi import FastAPI,HTTPException, File, UploadFile
import tensorflow as tf
import pandas as pd
import numpy as np
import uuid
import io
import PIL
from PIL import Image

#import .h5 model
model = tf.keras.models.load_model('model_trained_effnet.h5')

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to the Garbage Classification API"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    #read the image
    contents = await file.read()
    
    # Convert the content into a bytes stream
    img_stream = io.BytesIO(contents)
    img = Image.open(img_stream).resize((224, 224))

    # img = tf.keras.preprocessing.image.load_img(file_img, target_size=(200, 200))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    garbage_types = [ 'battery', 'biological', 'brown-glass', 'cardboard','clothes', 'green-glass','metal', 'paper', 'plastic','shoes' ,'trash', 'white-glass']
    predicted_class = garbage_types[np.argmax(predictions)]
    # print(f"The predicted class is: {predicted_class}")
    #give confidence score
    confidence = np.max(predictions) * 100
    return {"confidence": confidence, "class": predicted_class}



if __name__== '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)