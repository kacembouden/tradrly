# tradrly

This is a Flask web application that allows users to upload an image file, extracts text from the image using the `analyse` module, and displays a message with the result on the webpage. Additionally, the application provides a button to download a report in the `/results.txt` file.

## How to Use

1. Ensure you have Flask installed:

   ```bash
   pip install Flask
   ```

2. Install the required Python packages:

   ```bash
   pip install Pillow pytesseract spellchecker opencv-python nltk
   ```

3. Download the NLTK punkt package for sentence tokenization:

   ```python
   import nltk
   nltk.download('punkt')
   ```

4. Install Tesseract OCR and specify its path in the `analyse.py` file:

   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

5. Run the Flask app:

   ```bash
   python api.py
   ```

   The application will be accessible at [http://localhost:5000](http://localhost:5000).

6. Upload an image file using the provided file upload form. After the upload, the app will process the image, and a message will be displayed indicating the success or failure of the process.

7. If the image is successfully processed, report file (`/results/report.txt`) containing the extracted text, dates, phone numbers, and document type.


## OR you can just use docker

1. install docker 

2. Navigate to Your Project Directory:
Open a terminal or command prompt and navigate to the root directory of your project.

cd /path/to/your/tradrly

3. Build Docker Images :

docker build --tag python-docker .

4. Run Docker Compose:

docker run -d -p 5000:5000 python-docker


## Project Structure

- `app.py`: The main Flask application file.
- `analyse.py`: Module containing the image-to-text extraction functionality, date and phone number extraction, document type detection, and other processing functions.
- `templates/upload.html`: HTML template for the file upload page.

## Dependencies

- Flask: Web framework for building the application.
- Pillow: Image processing library for working with images.
- pytesseract: Python wrapper for Tesseract OCR.
- spellchecker: Spellchecking library for correcting words.
- opencv-python: Computer vision library for image processing.
- nltk: Natural Language Toolkit for language processing.

## How to Extend

Feel free to extend this application by adding additional features or improving the image-to-text extraction functionality in the `analyse` module.
