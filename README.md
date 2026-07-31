
# Urdu OCR — A Fine-Tuned TrOCR Model for Extracting Text from Urdu Images

## 1. What Problem This Solves and Why It Matters

Millions of documents, signboards, books, and newspapers across Pakistan and the wider Urdu-speaking world exist only as images or scans — with no easy way to search, copy, edit, or digitize the text inside them. Standard OCR tools like Tesseract are built for Latin scripts and struggle badly with Urdu's cursive, connected Nastaliq script, where letters change shape depending on their position in a word (much like joined handwriting). This project builds a custom Optical Character Recognition (OCR) system specifically trained to read Urdu text from real-world images — books, newspapers, signboards, and synthetic samples — turning pictures of Urdu text into actual readable, editable text.

## 2. How It Works

This project uses **TrOCR** (Transformer-based OCR), a deep learning model that combines a Vision Transformer (to "see" the image) with a language decoder (to "write out" the text it recognizes) — think of it as an AI that looks at a picture and reads it aloud, character by character.

Rather than training a model from scratch, this project uses **fine-tuning**: starting with a TrOCR model already pretrained on general OCR tasks, then continuing its training specifically on a custom Urdu dataset. This teaches the model the distinct shapes, joins, and diacritics of Urdu script without needing millions of training examples.

**Pipeline overview:**
1. Collected and labeled 224+ Urdu text images across five categories (books, newspapers, signboards, synthetic, other)
2. Preprocessed images (grayscale, resize, denoise, binarize) to standardize input quality
3. Built a custom PyTorch `UrduOCRDataset` class with `TrOCRProcessor` to feed images and labels into the model
4. Fine-tuned `Hammad712/troce-urdu-model2-v1` over 10 epochs
5. Deployed the trained model behind a simple web interface (Gradio in Colab, then a permanent Streamlit app) so anyone can upload an image and get extracted Urdu text instantly

## 3. Live Demo Link

**(https://urdu-ocr-codesaviours-si26-fatima-few8uhqbwx8w99hug2o4rb.streamlit.app/)**

*(Deployed on Streamlit Community Cloud — Hugging Face Spaces changed their free-tier policy this week, restricting new/free accounts from creating Gradio Spaces without a paid plan. Streamlit provides the same live, permanent, public functionality.)*

## 4. How to Run It Locally

```bash
# 1. Clone the repo
git clone https://github.com/fatimasajid31/urdu-ocr-codesaviours-si26-fatima.git
cd urdu-ocr-codesaviours-si26-fatima

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py       # for the Gradio version
# or
streamlit run streamlit_app.py   # for the Streamlit version
```

The app will download the fine-tuned model automatically on first run and open a local web interface where you can upload a Urdu image and see the extracted text.

## 5. Dataset Details

- **Total images:** 224+ labeled samples
- **Categories:** Books, newspapers, signboards, synthetic text images, and other miscellaneous sources
- **Fonts used (synthetic images):** Noto Nastaliq Urdu and Noto Naskh Arabic
- **Labeling:** Each image paired with its ground-truth Urdu text in a `labels.csv` file
- **Variety:** Mix of real-world photographs (varying lighting, backgrounds, font styles) and computer-generated text to broaden the model's exposure to different visual styles of Urdu script

## 6. Results

After fine-tuning for 10 epochs:
- **Training Character Error Rate (CER):** ~10.2%
- **Training loss:** Dropped significantly across epochs, showing the model was successfully learning Urdu character patterns
- **Exact-match test accuracy:** 0%

**Why exact-match accuracy was 0% despite a low CER:** the CER measures how close the predicted text is character-by-character, and at ~10.2% the model is getting most characters right. However, "exact match" requires the *entire* predicted string to be character-for-character identical to the ground truth — a single extra space, dropped character, or generation-length mismatch fails the whole example. This points to a **generation length/decoding issue** (the model likely wasn't generating sequences of the correct length), rather than the model failing to learn Urdu script itself.

**What I'd do differently with more time:**
- Tune `max_length` and `num_beams` in the model's `.generate()` call to better match expected output lengths
- Add more diverse training examples, especially longer text sequences
- Use a validation-based early stopping strategy to prevent overfitting on the (currently limited) training set
- Explore length-normalized decoding strategies to fix the exact-match generation problem specifically
**Screenshots**
  <img width="1176" height="344" alt="image" src="https://github.com/user-attachments/assets/39d9677d-17ef-463c-bc37-1c59b459bf79" />
  Result of step 1.
- <img width="822" height="341" alt="image" src="https://github.com/user-attachments/assets/849656a6-7fd6-4d8c-a7cd-df204cb233ac" />
deployment step on streamlit because gradio is paid.
<img width="895" height="819" alt="image (1)" src="https://github.com/user-attachments/assets/74b490e3-2633-4ae9-9202-6f31200b4358" />


## 7. Credit
Built during the **Code Saviours ML/AI Internship — Batch SI-26**
**Fatima Sajid** | Roll No. 2023-BS-CS-197 | University of Faisalabad.
GitHub: [fatimasajid31](https://github.com/fatimasajid31)
