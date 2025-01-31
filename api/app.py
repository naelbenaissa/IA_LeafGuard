from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Chargement du modèle entraîné
model = tf.keras.models.load_model("../model/modele_maladies_plantes.h5")

# Initialise l'API FastAPI
app = FastAPI()

# Fonction pour traiter l'image et faire une prédiction
def predict(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((224, 224))  # Adapte à la taille du modèle
    image = np.array(image) / 255.0  # Normalise les valeurs de pixel
    image = np.expand_dims(image, axis=0)  # Ajoute une dimension batch
    prediction = model.predict(image)
    return prediction

# Endpoint API pour l'analyse d'image
@app.post("/predict/")
async def predict_disease(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict(image_bytes)
    return {"prediction": result.tolist()}
