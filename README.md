Urdu OCR Project | Code Saviours SI-26 | Fatima Sajid
**What is OCR (Optical Character Recognition)?**
OCR is technology that reads text from images or photos and turns it into real text you can copy and edit. For example, when you scan a book page, OCR converts the picture into actual readable text instead of just an image.

**Why is Urdu OCR harder than English OCR?**
Urdu letters connect together in a cursive style and change shape depending on their position in a word, similar to joined handwriting. English letters, on the other hand, stay separate and keep the same shape. Urdu is also written right-to-left, and there is much less training data available for it compared to English.

**What are 2 real-world situations where Urdu OCR would be useful?**
Urdu OCR can be used to scan old Urdu books and newspapers and turn them into digital, searchable text for archiving. It can also be used to read Urdu signboards or official documents automatically, which is helpful for translation apps or digitizing government paperwork.
## Why We Need a Better Model

| Image | Actual Text | Tesseract Output | Correct? |
|-------|------------|-------------------|----------|
| urdu_1.png | اردو ایک خوبصورت زبان ہے | garbled dots/symbols | ❌ |
| urdu_15.png | پانی زندگی کی نہایت ضروری ہے | "27" + random characters | ❌ |
| urdu_6.png | سورج مشرق سے طلوع ہوتا ہے | single dot/mark | ❌ |
| urdu_14.png | درخت لگانا ایک نیک عمل ہے | ".8" random symbols | ❌ |
| urdu_16.png | اساتذہ کا احترام کرنا چاہیے | "xx" + scrambled characters | ❌ |

**Result: 0 out of 5 images read correctly.**
Tesseract fails on Urdu because Urdu uses a cursive Nastaliq script where letters connect and change shape depending on their position in a word — very different from the separated Latin letters Tesseract was mainly designed for. Urdu is also written right-to-left, adding another layer of complexity. In our test of 5 preprocessed images, Tesseract correctly read 0 out of 5 sentences, producing garbled symbols, random numbers, or mostly empty output instead of real Urdu words. This shows that off-the-shelf OCR tools are not reliable for Urdu text, which is exactly the gap our project aims to address by building a custom Urdu OCR model.


