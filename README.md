# IA LeafGuard

IA LeafGuard is an AI-powered plant disease recognition API based on a deep learning model. This API, developed with **FastAPI**, utilizes **TensorFlow** to analyze images and predict diseases affecting tomato, pepper, and potato plants.

## Features

- **Image Analysis**: Upload an image and detect plant diseases.
- **REST API**: Endpoint to submit an image and receive a diagnosis.
- **Containerized Deployment**: Docker setup for easy execution.

## Prerequisites

- **Python 3.9+**
- **TensorFlow**
- **FastAPI**
- **Uvicorn**

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/naelbenaissa/IA_LeafGuard.git
   cd ia_leafguard
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

3. **Run the API**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

## Deployment with Docker

1. **Build the Docker image**
   ```bash
   docker build -t ia_leafguard .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 ia_leafguard
   ```

## API Usage

The API provides an endpoint to send an image for analysis:

- **Endpoint**: `POST /predict/`
- **Parameter**: `file` (image to analyze)

### Example usage with `cURL`

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path_to_image.jpg'
```

### Example JSON Response

```json
{
  "maladies": "Tomato - Mosaic Virus",
  "confiance": 0.95
}
```

## Project Structure

```
IA_LeafGuard/
│── model/
│   ├── modele_maladies_plantes.h5  # Pre-trained model
│── PlantVillage/  # Dataset image directory
│── app.py  # Main API script
│── IA_LeafGuard.ipynb  # Model training notebook
│── requirements.txt  # Dependencies
│── Dockerfile  # Docker configuration
```

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request on [GitHub](https://github.com/naelbenaissa/IA_LeafGuard).

---

🚀 **IA LeafGuard - Protect Your Plants with AI!** 🌱

