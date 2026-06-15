from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
import json
import cv2
import time

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from disease_info import disease_info

app = FastAPI()

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# LOAD MODEL
# =========================
MODEL_PATH = r"C:\Users\Shreya Singh\OneDrive\Desktop\plant-disease-detection\plant_disease_model.h5"

model = tf.keras.models.load_model(MODEL_PATH)

# Warm up model (removes first prediction delay)
dummy = np.zeros((1, 224, 224, 3), dtype=np.float32)
dummy = preprocess_input(dummy)
model.predict(dummy, verbose=0)

# =========================
# LOAD CLASS NAMES
# =========================
with open("class_names.json", "r") as f:
    class_names = json.load(f)

print("Model Loaded Successfully")
print("Number of Classes:", len(class_names))


# =========================
# PREDICT ENDPOINT
# =========================
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:

        # Read image
        image_bytes = await file.read()

        image_np = np.frombuffer(image_bytes, np.uint8)

        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        if image is None:
            return {"error": "Invalid image"}

        # Resize
        image = cv2.resize(image, (224, 224))

        # Convert to float32
        img_array = image.astype(np.float32)

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        # IMPORTANT: same preprocessing used during training
        img_array = preprocess_input(img_array)

        # Prediction
        start_time = time.time()

        predictions = model.predict(img_array, verbose=0)[0]

        prediction_time = round(time.time() - start_time, 3)

        predicted_index = int(np.argmax(predictions))

        predicted_class = class_names[predicted_index]

        confidence = float(np.max(predictions)) * 100

        print("\n====================")
        print("Disease:", predicted_class)
        print("Confidence:", round(confidence, 2), "%")
        print("Prediction Time:", prediction_time, "seconds")
        print("====================\n")

        info = disease_info.get(
            predicted_class,
            {
                "name_english": predicted_class,
                "name_hindi": predicted_class,
                "symptoms_en": "Not available",
                "symptoms_hi": "उपलब्ध नहीं",
                "treatment_en": "Not available",
                "treatment_hi": "उपलब्ध नहीं",
                "prevention_en": "Not available",
                "prevention_hi": "उपलब्ध नहीं"
            }
        )

        return {
            "disease_en": info.get("name_english", predicted_class),
            "disease_hi": info.get("name_hindi", predicted_class),

            "symptoms_en": info.get("symptoms_en", ""),
            "symptoms_hi": info.get("symptoms_hi", ""),

            "treatment_en": info.get("treatment_en", ""),
            "treatment_hi": info.get("treatment_hi", ""),

            "prevention_en": info.get("prevention_en", ""),
            "prevention_hi": info.get("prevention_hi", ""),

            "confidence": round(confidence, 2)
        }

    except Exception as e:
        return {
            "error": str(e)
        }