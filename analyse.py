# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:16:23 2024

@author: kacem
"""

from PIL import Image
import pytesseract
from spellchecker import SpellChecker
import os
import re
import cv2
import nltk

# Download the nltk punkt package for sentence tokenization
nltk.download('punkt')

# Path to the Tesseract executable (update this with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
myconfig = r"--psm 1 --oem 3"

arabic_words_list = [
    "شكاية",
    "شكايات",
    "يشكو",
    "تشكو",
    "مشكلة",
    "مشكل",
    "يشكل",
    "تشكل",
    "شكوك",
    "يتشكى",
    "شكوان",
    "شكايات",
    "يشكون",
    "تشكون",
    "مشكلات",
    "مشكلا",
    "يشكلون",
    "تشكلون",
    "شكاو",
    "شكوى",
    "يشكوا",
    "تشكوا",
    "مشكلين",
    "مشكلون",
    "يتشكون",
    "تتشكون",
    "مشكلاة",
    "مشكلات",
    "يشكلوا",
    "تشكلوا",
    "الشاكى",
    "الشاكين",
    "الشكوى",
    "الشكوك",
    "الشاكي",
    "الشكايات",
    "الشكي",
    "الشاكيات",
    "الشاكون",
    "الشكاوى",
    "الشاكيات",
    "الشاكوك",
    "الشكلين",
    "الشكون",
    "الشكيل",
    "الشكيلة",
    "الشكيات",
    "الشكلات",
    "الشكاو",
    "الشكليات",
    "الشكواك",
    "المشتكى",
    "المشتكين",
    "المشكوى",
    "المشتكون",
    "المشتكوات",
    "المشتكى عليه",
    "المشتكى إليه",
    "المشتكون به",
    "المشتكيات",
    "المشتكيات به",
    "المشتكى منه",
    "المشتكى عنه",
    "المشتكى لديه",
    "المشتكى به",
    "المشتكون بهم",
    "المشتكى إليها",
    "المشتكى بها",
    "المشتكى فيه",
    "المشتكى منها",
    "المشتكوات به",
    "المشتكى لدى",
]

arabic_words_list_bataqa = [
    "بطاقة",
    "بطاقات",
    "البطاقة",
    "بطاقتك",
    "بطاقته",
    "بطاقتها",
    "بطاقتي",
    "بطاقتهم",
    "بطاقتكم",
    "بطاقتكن",
    "بطاقتكَ",
    "بطاقتهُ",
    "بطاقتها",
    "بطاقتنا",
    "بطاقاتهم",
    "بطاقاتكم",
    "بطاقاتكن",
    "بطاقتكِ",
    "بطاقتهما",
    "بطاقتهن",
    "بطاقتين",
]

# You can use this list in your Python code as needed.

def spelling(text):
    spell = SpellChecker(language='ar')
    return [spell.correction(word) for word in text.split()]


def image_processing(image_path):
    file_path = "results/recognized.txt"
    if os.path.exists(file_path):
        # Remove the file
        os.remove(file_path)

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    
    # Specify structure shape and kernel size. 
    # Kernel size increases or decreases the area 
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect 
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    
    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    
    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                    cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]

        # Open the file in append mode
        file = open("results/recognized.txt", "a",encoding='utf-8')

        text = pytesseract.image_to_string(cropped,lang='ara')
     
        # Appending the text into file
        try:
            file.write(text)
            file.write("\n")
        except:
            pass
        
        # Close the file
        file.close
        
def extract_dates_from_text(text):
    # Define a regular expression pattern for common date formats
    date_pattern = re.compile(r'\b(?:\d{1,4}[-/]\d{1,2}[-/]\d{2,4}|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{1,2}/\d{1,2}/\d{2,4}|\d{2,4}/\d{1,2}/\d{1,2}|\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}/\d{2,4}/\d{1,2}|\d{1,2}/\d{2,4}|\d{1,2}-\d{1,2}-\d{2,4}|\d{1,2}/\w{3,}/\d{2,4}|\w{3,}/\d{1,2}/\d{2,4}|\w{3,}/\d{1,2}/\w{3,}|\d{1,2}/\w{3,}/\w{3,}|\w{3,}/\w{3,}/\d{1,2})\b')

    # Find all matches in the text
    dates_found = re.findall(date_pattern, text)

    standardized_dates = [re.sub(r'\D', '-', date) for date in dates_found]

    return standardized_dates

def extract_phone_numbers(text):
    # Define a regular expression pattern for matching phone numbers
    phone_number_pattern = re.compile(r'\b(?:\d{8}|\d{2}[\s\.]?\d{3}[\s\.]?\d{3})\b')

    # Find all matches in the text
    phone_numbers_found = re.findall(phone_number_pattern, text)

    standardized_numbers = [re.sub(r'\D', '', number) for number in phone_numbers_found]

    return standardized_numbers

def get_similar_words(text, target_word):
    # Use regex to find words similar to the target word in the text
    similar_words = re.findall(r'\b\w{0,2}' + re.escape(target_word) + r'\w{0,2}\b', text, re.IGNORECASE)
    return similar_words

def split_into_sentences(article):
    # Use nltk sentence tokenization
    sentences = nltk.sent_tokenize(article)
    return sentences

def doc_type(text):
    similar_words = []
    # Get similar words in the example text
    for target_word in arabic_words_list:
        similar_words.extend(get_similar_words(text, target_word))

    sentences = []
    for word in similar_words:
        li = (split_into_sentences(text))
        for sentence in li:
            if word in sentence.split():
                return  "Complain"

    similar_words = []
    # Get similar words in the example text
    for target_word in arabic_words_list_bataqa:
        similar_words.extend(get_similar_words(text, target_word))

    sentences = []
    for word in similar_words:
        li = (split_into_sentences(text))
        for sentence in li:
            if word in sentence.split():
                return "Card"
    
    return ''


def run(image_path):

    
    image_processing(image_path)

    # Extract dates from the example text

    with open('results/recognized.txt', 'r', encoding='utf-8') as file:
    # Read the file line by line
        text = ''.join(file.readlines()) 
    
    dates_found = extract_dates_from_text(text)


    eight_digit_numbers_found = extract_phone_numbers(text)

    type_de_document = doc_type(text)

    # Build the report content
    report_content = f"Report:\nDocument Type: {type_de_document}\nDates: {dates_found}\nPhone Numbers: {eight_digit_numbers_found}\nWhole Text: {text}"

    # Save the report to a file
    file_name = "results/report.txt"
    with open(file_name, 'w', encoding='utf-8') as report_file:
        report_file.write(report_content)


#run()