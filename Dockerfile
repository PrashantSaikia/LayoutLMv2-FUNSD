FROM python:3.9

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
ADD . /app

# Install dependencies
RUN apt-get update
RUN apt-get install -y tesseract-ocr

RUN pip install -r requirements.txt

RUN git clone https://github.com/facebookresearch/detectron2.git
RUN python -m pip install -e detectron2

# Expose port 
EXPOSE 5000

# Run the application:
CMD ["python", "app.py"]
