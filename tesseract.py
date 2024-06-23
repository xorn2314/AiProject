from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\xorn2\AppData\Local\tesseract.exe'
def extract_text_from_image(image_path):
    # 이미지에서 텍스트 추출
    text = pytesseract.image_to_string(Image.open(image_path))
    return text