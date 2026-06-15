import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_PATH = "dataset/PlantVillage"

datagen = ImageDataGenerator(rescale=1./255)

generator = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)

class_names = list(generator.class_indices.keys())

with open("class_names.json", "w") as f:
    json.dump(class_names, f)

print("class_names.json created successfully!")