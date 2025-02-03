import numpy as np
from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
from PIL import Image
import io

# Chargement du modèle
model = tf.keras.models.load_model("model/modele_maladies_plantes.h5")

classification_types = [
    'Poivron - Dépérissement bactérien', 'Poivron - Sain',
    'Pomme de terre - Brûlure précoce', 'Pomme de terre - Brûlure tardive', 'Pomme de terre - Saine',
    'Tomate - Tache bactérienne', 'Tomate - Brûlure précoce', 'Tomate - Brûlure tardive',
    'Tomate - Moisi des feuilles', 'Tomate - Tache septorienne',
    'Tomate - Acariens (Tétranyques à deux points)', 'Tomate - Tache ciblée',
    'Tomate - Virus de l’enroulement jaune des feuilles', 'Tomate - Virus de la mosaïque',
    'Tomate - Saine'
]

# Initialise l'API FastAPI
app = FastAPI()

# Fonction de prédiction
def predict(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((80, 80))  # Ajuste à la taille correcte
    image = np.array(image) / 255.0  # Normalise
    image = np.expand_dims(image, axis=0)  # Ajoute la dimension batch
    
    prediction = model.predict(image)
    predicted_index = np.argmax(prediction)  # Trouve l'indice le plus élevé
    confidence = float(np.max(prediction))  # Probabilité de la prédiction

    return {
        "maladies": classification_types[predicted_index],
        "confiance": confidence
    }

# Endpoint API pour l'analyse d'image
@app.post("/predict/")
async def predict_disease(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict(image_bytes)
    return result
