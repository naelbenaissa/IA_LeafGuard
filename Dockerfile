# Utilise une image Python avec les bibliothèques de base
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers du projet dans le conteneur
COPY . /app/

# Installation des dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080
EXPOSE 8080

# Commande pour démarrer FastAPI avec Uvicorn
ENV PORT=8080
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "$PORT"]
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]
