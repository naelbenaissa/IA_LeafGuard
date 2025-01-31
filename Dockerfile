# Utilise une image Python avec les bibliothèques de base
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers du projet dans le conteneur
COPY . /app/

# Installation des dépendances
RUN pip install --no-cache-dir fastapi uvicorn tensorflow pillow numpy

# Exposer le port 8000
EXPOSE 8000

# Commande pour démarrer FastAPI avec Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
