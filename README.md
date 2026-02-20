# 🖼️ Visual Question Answering (VQA) using BLIP & Streamlit

An interactive Visual Question Answering (VQA) web application built using 
Salesforce BLIP (Bootstrapping Language-Image Pre-training) and Streamlit. 
The system allows users to upload an image and ask natural language questions 
to receive AI-generated answers based on visual understanding.

---

## 🚀 Project Overview
This project implements a multimodal AI system that combines computer vision 
and natural language processing to answer questions about images. It leverages 
a pre-trained BLIP VQA model from Hugging Face Transformers for high-quality 
image understanding and reasoning.

Users can:
- Upload custom images
- Select demo images from sidebar
- Ask natural language questions about the image
- View real-time AI-generated answers
- Track Q&A history within the session

---

## 🧠 Model Used
- **Model:** BLIP VQA (Bootstrapping Language-Image Pre-training)
- **Processor:** `Salesforce/blip-vqa-base`
- **Model:** `Salesforce/blip-vqa-large`
- Framework: Hugging Face Transformers + PyTorch

---

## 🎥 Demo

### 🖼️ Visual Question Answering using BLIP
The application allows users to:
- Upload an image
- Ask natural language questions
- Receive AI-generated answers using BLIP VQA model

### Example:
**Question:** What is this?  
**Answer:** Dog  

![Demo Screenshot](demo_blip_vqa.png)

---

## 🛠️ Tech Stack
- Python
- Streamlit (Web App)
- Hugging Face Transformers
- BLIP (Vision-Language Model)
- PyTorch
- PIL (Image Processing)
- Requests (Image Fetching)

---

## 📂 Features
- Interactive web interface using Streamlit
- Image upload support (JPG, PNG, JPEG)
- Demo image selection via sidebar
- Real-time Visual Question Answering
- Session-based Q&A history tracking
- Cached model loading for faster performance

---

## 🖥️ Application Workflow
1. User uploads an image or selects a demo image
2. User enters a question about the image
3. BLIP model processes image + text input
4. Model generates contextual answer
5. Answer and history are displayed in UI

---

## 📸 Demo Use Cases
- Object recognition in images
- Scene understanding
- Visual reasoning
- Caption-based question answering
- Multimodal AI applications

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME

### 2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

---

📊 Project Structure

```
Visual-Question-Answering/
│
├── app.py                # Streamlit application
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
└── demo_assets/          # (Optional demo images)
```

---

⚠️ Limitations

- Model performance depends on image quality
- Large model size may require GPU for faster inference
- Internet required for first-time model download

---

🌟 Future Improvements

- Add image captioning module
-Deploy on Hugging Face Spaces / Streamlit Cloud
-Add speech-to-question input
-Support multiple VQA models for comparison
-GPU acceleration support

---

👩‍💻 Author

AI/ML Student | Multimodal AI & Time-Series Forecasting Projects
Focused on Machine Learning, NLP, and Applied AI Systems.
