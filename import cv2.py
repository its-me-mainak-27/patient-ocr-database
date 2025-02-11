import cv2
import pytesseract
import easyocr
import json

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

def preprocess_image(image_path):
    """Preprocess the image to improve OCR accuracy."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Thresholding
    return thresh

def extract_text(image_path, method='tesseract'):
    """Extract text from an image using OCR."""
    processed_image = preprocess_image(image_path)

    if method == 'tesseract':
        text = pytesseract.image_to_string(processed_image)
    else:
        results = reader.readtext(processed_image)
        text = ' '.join([res[1] for res in results])

    return text

if __name__ == "__main__":
    image_path = "patient_form.jpg"  # Change this to your image path
    text = extract_text(image_path, method='easyocr')
    print("Extracted Text:\n", text)
