# 🌿 PlantGuard AI - Plant Disease Detection System

> An AI-powered plant disease detection system that helps farmers and gardeners identify crop diseases instantly using deep learning.
---

## 📖 Overview

PlantGuard AI is an intelligent web application that detects diseases in plant leaves using Deep Learning and Computer Vision.

The system analyzes a leaf image uploaded by the user and provides:

- 🦠 Disease Name
- 🎯 Confidence Score
- 📋 Symptoms
- 💊 Treatment Suggestions
- 🛡 Prevention Tips
- 🌐 Bilingual Output (English + Hindi)

The goal is to assist farmers and agricultural workers in identifying diseases early and taking corrective action.

---

## ✨ Features

### 🔍 Disease Detection
Detects multiple diseases affecting:

- 🍅 Tomato
- 🥔 Potato
- 🫑 Bell Pepper

### 🤖 AI-Powered Analysis
Uses Transfer Learning with MobileNetV2 for fast and accurate predictions.

### 🌐 Dual Language Support
Displays results in:

- English 🇬🇧
- Hindi 🇮🇳

### 📊 Confidence Score
Provides prediction confidence percentage for better reliability.

### 💡 Disease Guidance
Offers:

- Symptoms
- Treatment Methods
- Prevention Measures

### ⚡ Real-Time Predictions
FastAPI backend ensures quick inference and response.

---

## 🧠 AI Model

### Model Architecture

MobileNetV2 (Transfer Learning)

Why MobileNetV2?

- Lightweight
- Fast Inference
- High Accuracy
- Suitable for Real-Time Applications

### Training Details

| Parameter | Value |
|------------|--------|
| Dataset | PlantVillage |
| Image Size | 224 × 224 |
| Batch Size | 32 |
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Validation Accuracy | 91.39% |

---

## 📂 Supported Classes

### Bell Pepper

- Bacterial Spot
- Healthy

### Potato

- Early Blight
- Late Blight
- Healthy

### Tomato

- Bacterial Spot
- Early Blight
- Late Blight
- Leaf Mold
- Septoria Leaf Spot
- Spider Mites
- Target Spot
- Tomato Mosaic Virus
- Tomato Yellow Leaf Curl Virus
- Healthy

---

## 🛠 Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- FastAPI
- Uvicorn

### AI & Machine Learning

- TensorFlow
- Keras
- MobileNetV2
- NumPy
- OpenCV

---

## 📸 Application Workflow

```text
Upload Leaf Image
        ↓
Image Preprocessing
        ↓
MobileNetV2 Model
        ↓
Disease Prediction
        ↓
Confidence Calculation
        ↓
Disease Information
        ↓
Display Results
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/plant-disease-detection.git
cd plant-disease-detection
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows:

```bash
env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
cd backend
uvicorn main:app --reload
```

### Open Frontend

Open:

```text
index.html
```

in your browser.

---

## 📊 Sample Output

```text
🦠 Disease
Tomato Spider Mites

🎯 Confidence
87.17%

📋 Symptoms
Yellow speckles and fine webbing on leaves.

💊 Treatment
Use Neem oil or approved miticides.

🛡 Prevention
Maintain humidity and inspect plants regularly.
```

---

## 🎯 Future Improvements

- 📷 Live Camera Detection
- 🎤 Voice Assistant
- 🌦 Weather-Based Disease Prediction
- 🌱 Fertilizer Recommendations
- 🤖 Farmer Chatbot
- 📄 PDF Report Generation
- ☁ Cloud Deployment

---
## 📸 Screenshots

### 🏠 Home Page

![Home Page](./screenshots/home.png)

---

### 📤 Upload Screen

![Upload Screen](./screenshots/upload.png)

---

### 🦠 Disease Detection Result

![Detection Result](./screenshots/result.png)


## 👩‍💻 Author

### Shreya Singh

B.Tech Student | AI & ML Enthusiast

Passionate about applying Artificial Intelligence to solve real-world agricultural problems.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share with others

---

**"Empowering Agriculture with Artificial Intelligence 🌾🤖"**
