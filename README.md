# tradrly

Certainly! Here's an updated README with the additional code and explanations:

```markdown
# Flask Image Text Extraction App

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
   python app.py
   ```

   The application will be accessible at [http://localhost:5000](http://localhost:5000).

6. Upload an image file using the provided file upload form. After the upload, the app will process the image, and a message will be displayed indicating the success or failure of the process.

7. If the image is successfully processed, a button labeled "Download Report" will appear. Clicking this button will trigger the download of a report file (`/results/report.txt`) containing the extracted text, dates, phone numbers, and document type.

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

## License

This project is licensed under the [MIT License](LICENSE).
```

Remember to replace `[Any other dependencies used in your 'analyse' module.]` with the actual dependencies used in the `analyse` module. Adjust the information according to your specific application.