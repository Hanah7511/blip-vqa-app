import streamlit as st
from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import requests
import torch

# Load model & processor
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
    model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-large")
    return processor, model

processor, model = load_model()

# App title
st.title("🖼️ BLIP Visual Question Answering")
st.write("Upload an image and ask a question about it!")

# Sidebar with demo images
st.sidebar.header("📂 Demo Images")
demo_images = {
    "lady with dog": "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg",
    "Dog": "https://images.unsplash.com/photo-1560807707-8cc77767d783",
    "beach": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
}
choice = st.sidebar.selectbox("Or choose a demo image:", ["None"] + list(demo_images.keys()))

# Image uploader
uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])
if choice != "None":
    image = Image.open(requests.get(demo_images[choice], stream=True).raw)
elif uploaded_file:
    image = Image.open(uploaded_file)
else:
    image = None

# Display image
if image:
    st.image(image, caption="Your selected image", use_column_width=True)

    # Question input
    question = st.text_input("❓ Ask a question about the image:")

    if question:
        # Preprocess input
        inputs = processor(image, question, return_tensors="pt")
        out = model.generate(**inputs)
        answer = processor.decode(out[0], skip_special_tokens=True)

        # Save Q&A in session state
        if "qa_history" not in st.session_state:
            st.session_state.qa_history = []
        st.session_state.qa_history.append((question, answer))

        # Display answer
        st.markdown(f"**Q:** {question}")
        st.markdown(f"**A:** {answer}")

        # Show history
        st.subheader("📝 Previous Questions & Answers")
        for q, a in st.session_state.qa_history:
            st.write(f"- **Q:** {q} | **A:** {a}")
