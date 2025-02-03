# Utilise une image Python avec les bibliothèques de base
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers du projet dans le conteneur
COPY . /app/

# Installation des dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Exposer le port 8000
EXPOSE 8000

# Commande pour démarrer FastAPI avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]