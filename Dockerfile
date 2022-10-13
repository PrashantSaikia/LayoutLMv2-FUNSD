FROM python:3.9
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
ADD . /app
# Install dependencies
RUN pip install -r requirements.txt
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
# Expose port 
EXPOSE 5000
# Run the application:
CMD ["python", "app.py"]
