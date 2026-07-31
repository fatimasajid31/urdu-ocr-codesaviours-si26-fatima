import os
import zipfile
import gdown
import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

MODEL_DIR = "urdu-ocr-model"
FILE_ID = "14Me4MLVh_KTfRmASV1Z7dwilH0B2sCgb"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_DIR):
        zip_path = "model.zip"
        gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", zip_path, quiet=False)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(MODEL_DIR)
    processor = TrOCRProcessor.from_pretrained(MODEL_DIR)
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_DIR)
    model.eval()
    return processor, model

st.title("Urdu OCR — Code Saviours SI-26")
st.write("Upload an image containing Urdu text and get the extracted text.")

processor, model = load_model()

uploaded_file = st.file_uploader("Upload Urdu Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text"):
        with st.spinner("Extracting text..."):
            pixel_values = processor(image, return_tensors="pt").pixel_values
            with torch.no_grad():
                generated_ids = model.generate(pixel_values)
            text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
            if not text:
                text = "Could not extract text from this image"
        st.text_area("Extracted Urdu Text", text, height=100)
