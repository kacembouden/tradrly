FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev &&\
    apt-get install tesseract-ocr-ara

CMD ["python", "api.py"]