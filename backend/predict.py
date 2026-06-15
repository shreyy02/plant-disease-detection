import tensorflow as tf
import numpy as np
import json
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

model = tf.keras.models.load_model("plant_disease_model.h5")

with open("class_names.json", "r") as f:
    class_names = json.load(f)

img = image.load_img("test_leaf.jpg", target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# 🔥 MUST BE THIS
img_array = preprocess_input(img_array)

predictions = model.predict(img_array)[0]

print("RAW:", predictions)

predicted_index = np.argmax(predictions)
confidence = float(np.max(predictions)) * 100

print("CLASS:", class_names[predicted_index])
print("CONFIDENCE:", confidence)