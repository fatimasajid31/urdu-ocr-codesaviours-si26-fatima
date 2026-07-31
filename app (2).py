import os
import zipfile
import gdown
import gradio as gr
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

MODEL_DIR = "urdu-ocr-model"
FILE_ID = "14Me4MLVh_KTfRmASV1Z7dwilH0B2sCgb"

# Download and unzip model on first startup
if not os.path.exists(MODEL_DIR):
    zip_path = "model.zip"
    gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", zip_path, quiet=False)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(MODEL_DIR)

processor = TrOCRProcessor.from_pretrained(MODEL_DIR)
model = VisionEncoderDecoderModel.from_pretrained(MODEL_DIR)
model.eval()

def extract_urdu_text(image):
    """Takes an image, returns extracted Urdu text."""
    if image is None:
        return 'Please upload an image'

    pixel_values = processor(image, return_tensors='pt').pixel_values

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)

    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return text if text else 'Could not extract text from this image'

interface = gr.Interface(
    fn=extract_urdu_text,
    inputs=gr.Image(type='pil', label='Upload Urdu Image'),
    outputs=gr.Textbox(label='Extracted Urdu Text'),
    title='Urdu OCR — Code Saviours SI-26',
    description='Upload an image containing Urdu text and get the extracted text.',
    examples=[]
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    interface.launch(server_name="0.0.0.0", server_port=port)
